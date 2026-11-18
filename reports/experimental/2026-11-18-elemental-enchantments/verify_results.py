"""Check result bounds and replay selected fixtures against the delivered code."""

import csv
import hashlib
import json
from dataclasses import fields
from pathlib import Path

from run_study import SEED, TRIALS, ice_parties, invariants, qualifies
from simulate import Scenario, simulate

ROOT=Path(__file__).resolve().parent
RESULTS=ROOT/'results'


def scenario_from_row(row):
    args={}
    for field in fields(Scenario):
        value=row.get(field.name,field.default)
        if field.name=='attackers':
            value=tuple(value.split('+'))
        elif field.type is bool:
            value=value=='True' if isinstance(value,str) else value
        elif field.type in (int,float):
            value=field.type(value)
        args[field.name]=value
    return Scenario(**args)


def main():
    parameters=json.loads((ROOT/'parameters.json').read_text())
    invariants(tuple(parameters['recommended']))
    probability=('meaningful','fire_wound','freeze','entomb','shocked','stunned',
                 'tail','defender_down','attacker_down','drained_out')
    counts=[]
    replayed=[]
    for path in sorted(RESULTS.glob('*.csv')):
        with path.open(encoding='utf-8') as handle:
            rows=list(csv.DictReader(handle))
        if not rows or 'n' not in rows[0] or 'total' not in rows[0]:
            continue
        counts.append(dict(batch=path.name,fixtures=len(rows),
                           scenario_trials=sum(int(row['n']) for row in rows)))
        for row in rows:
            for key in probability:
                assert -1e-10<=float(row[key])<=1+1e-10,(path.name,key,row[key])
            assert 0<=float(row['total'])<=5,(path.name,'total')
            assert float(row['MP'])<=float(row['available_mp'])+1e-8,(path.name,'MP')
            assert float(row['max_AR_removed'])<=float(row['ar'])+1e-8,(path.name,'AR')
            assert float(row['max_MR_removed'])<=float(row['mr'])+1e-8,(path.name,'MR')
        for index in sorted({0,len(rows)//2,len(rows)-1}):
            old=rows[index]
            new,_=simulate(scenario_from_row(old),int(old['n']),SEED)
            for key in ('total','physical','fire','hex','air','MP','Leywell',
                        'lightning_denied','ice_denied','contact','natural_mp','available_mp'):
                assert abs(float(old[key])-new[key])<1e-10,(path.name,index,key,old[key],new[key])
            replayed.append(dict(batch=path.name,index=index))
    # Append the separately run concentrated-party exclusion rows once.
    missing=[dict(batch='ice_parties',**vars(s)) for s in ice_parties(parameters['recommended'])
             if not qualifies(s)]
    with (RESULTS/'unqualified.csv').open(encoding='utf-8') as handle:
        excluded=list(csv.DictReader(handle))
    if missing and not any(row['batch']=='ice_parties' for row in excluded):
        from run_study import write_csv
        write_csv('unqualified',[*excluded,*missing])
    manifest={path.name:dict(bytes=path.stat().st_size,
                            sha256=hashlib.sha256(path.read_bytes()).hexdigest())
              for path in sorted(RESULTS.glob('*'))}
    (ROOT/'results_manifest.json').write_text(json.dumps(manifest,indent=2),encoding='utf-8')
    validation=dict(bounds='passed',replays='passed',fixtures_replayed=len(replayed),
                    batches=counts,total_scenario_trials=sum(row['scenario_trials'] for row in counts))
    (ROOT/'validation.json').write_text(json.dumps(validation,indent=2),encoding='utf-8')
    print(json.dumps(validation,indent=2))


if __name__=='__main__':
    main()
