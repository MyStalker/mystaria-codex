# Mystaria elemental enchantment study

**EXPERIMENTAL DRAFT. Every recommendation requires author approval.**

Read `Mystaria_Elemental_Enchantment_Balance_DRAFT.md` for findings, assumptions,
complete tables and the individual author decisions.

The source snapshot is Mystaria main commit
`930efc89269da5cc266976861fc5215b32c1a0b6`. `sources.json` identifies the references.
The embedded fixtures permit offline reproduction without downloading canon again.

## Reproduce

Use Python 3.10 or later and a compatible NumPy 2.x release. The recorded run used
Python 3.15 and NumPy 2.5.5. From this directory, run the following commands.

```sh
python run_study.py
python report.py
python verify_results.py
```

The complete run evaluates thousands of fixtures at 12,000 trials each and takes
substantial CPU time. Paired precision checks use 60,000 trials and three extra
seeds. The code makes no network requests or canon edits.

## Files

- `fixtures.py` holds progression, legal equipment tables and resource costs.
- `calibration.py` implements exact contact histories and joint numerical fitting.
- `simulate.py` implements the explicit scenario mechanics and unresolved choices.
- `run_study.py` defines the populations, sensitivities and invariant checks.
- `report.py` builds the report from the generated data.
- `verify_results.py` checks bounds and replays 30 selected fixtures against the source.
- `parameters.json` records the candidate, seed, sample sizes and runtime version.
- `results/*.csv` hold summarized trial results, exact calculations and exclusions.
- `results/calibration.json` holds the final constrained joint fit.
- `results/calibration_pass1.json`, when included, preserves the earlier looser VI fit.
- `results_manifest.json` records checksums for the distributed result files.

The repository copy includes the report, executable source, parameters and selected
summary tables. The companion reproduction archive includes every result CSV.
Running the scripts regenerates those full tables locally.

## Interpretation

Ordinary tests use five attack rounds and observe eight rounds. The VI second-use
test allows ten attack rounds and observes twelve. The initial attack precedes the
defender's turn. The duration includes the application-turn tick.

The dataset separates isolated elemental delivery from integrated physical weapon
attacks. The source main's approved physical formula and archived experimental
Candidate C are both evaluated. Results are conditional scenario outcomes. They
do not establish campaign win rates or finalize open mechanics.

Shared seeded histories make contrasts reproducible. Scenario-trials are correlated
across fixtures. Treat per-fixture uncertainty and the paired precision checks
according to their stated sample sizes.
