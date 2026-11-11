# Multiversal Gateway

Technical runbook for Slate’s Mystaria and Portia’s Fantasia projects.

## Architecture

One authenticated OpenAI tunnel runs one MCP gateway process. All calls, including status and plain tests, require a `campaign` field. The gateway selects the matching local directory before reading configuration or looking up a card. A missing or unknown campaign, mismatched player configuration, or unavailable card returns an error. There is no active campaign variable or default campaign.

| Campaign | Player | Pilot cards | NPC draft budget | Canon repository |
|---|---|---|---:|---|
| `slate` | Lillia | Dusk, Peri | 512 tokens | `MyStalker/mystaria-codex` |
| `portia` | Sky | Beatrice | 1,024 tokens | `MyStalker/fantasia-campaign` |

The staged Windows workspace folder is `Multiversal Gateway`. It contains `multiversal_gateway.py`, `engine.py`, the tests, and separate `campaigns/slate` and `campaigns/portia` folders. Each has its own `settings.json`, `cards/`, and local `protected-names.txt`. Card files were copied byte-for-byte. The legacy installations remain available for rollback.

The local `legacy` folder also contains launchable copies for Slate v0.5.1 and Portia v0.5.4. Slate’s snapshot was assembled from the archived v0.5.1 code and settings and the existing Slate cards. Both snapshots passed MCP initialization. Use the historical tunnel settings with the corresponding snapshot only when rolling back.

Both routes send independent prompts to Oobabooga on `http://127.0.0.1:5000/v1/completions` using the loaded Gemma 4 GGUF. Each request sends temperature 0.6, top-p 0.9, top-k 64, min-p 0.05, and repetition penalty 1.1. The gateway uses Gemma 4 turns and an empty thought prefix, strips emitted thought blocks, and stops at a turn boundary or an NPC reply switching to the player's speaker label. Plain tests use a 512-token limit. Oobabooga owns the model context window.

The gateway keeps no conversation history and holds no GitHub credentials. Project instructions fix the campaign ID, source repository, and player for each project. Each request carries only the selected project's confirmed scene and relevant history. For GitHub excerpts, pair `canon_context` with up to four `canon_sources` objects, each with `repository`, `path`, and a full commit SHA in `revision`. Slate accepts its campaign tree and numbered root canon files. Portia accepts its active checkpoint and canon, characters, history, quests, mechanics, and encounters folders.

The gateway checks declared source scope and looks for recognizable foreign identities in NPC input and output. Source references are assertions from the calling project. The gateway cannot verify that a caller's pasted prose actually came from those references, and the identity check cannot recognize every cross-world detail. Always fetch the referenced revision from the correct GitHub repository and pass only reviewed, NPC-appropriate material. Omit drafts and DM-only secrets. The shared endpoint does not authenticate which ChatGPT project supplied a campaign ID.

## Startup and one-time cutover

1. Start Oobabooga with its existing loopback API configuration and load `Gemma4-12B-QAT-Uncensored-HauhauCS-Balanced-Q4_K_M.gguf` once. Leave that process running. Use the existing `MYSTARIA_OOBA_KEY` environment variable if your local API requires one.
2. In the Multiversal Gateway folder, run `py -B -m unittest discover -v`. Keep the legacy gateway folders and their existing tunnel launch configuration available.
3. Register a separate shared tunnel in OpenAI Tunnels management with Tunnels Read and Manage permissions. Configure a runtime key with Tunnels Read and Use permissions. Set `CONTROL_PLANE_TUNNEL_ID` to the **new** tunnel ID in the launch shell and supply the runtime key via `CONTROL_PLANE_API_KEY` using your existing secret setup. Keep credentials, local protected-name lists, and cards out of this runbook and source-control changes.
4. From the Multiversal Gateway folder, run the following in a dedicated PowerShell window. Use the executable's actual local path if it differs.

   ```powershell
   & "$env:USERPROFILE\Desktop\Harmless File\tunnel-client.exe" run --mcp-command "py -B -u multiversal_gateway.py" --health.listen-addr 127.0.0.1:0
   ```

5. Register the same shared tunnel as a ChatGPT app and enable it in both projects. Refresh its tools once and verify that each tool exposes a required `campaign` argument. Keep the old connector available for legacy chats. In the two projects, use the shared app for ordinary play.
6. From the Slate project call `gateway_status` with `{"campaign":"slate"}`. Expect v1.0.0, Lillia, Dusk and Peri. From Portia use `{"campaign":"portia"}`. Expect Sky and Beatrice. Both should show the same model and sampler settings. Run a two-sentence plain test and one hypothetical NPC draft from each project. Alternate projects and repeat status. Normal switching requires only the campaign argument.

## Project instructions

**Slate** — Always pass `campaign: slate` to the Multiversal Gateway. The player is Lillia. Fetch relevant approved lore and the latest confirmed scene through the GitHub app from `MyStalker/mystaria-codex`. If you include canon, cite the retrieved commit SHA and repository-relative path with each source. Keep Lillia's response and voluntary actions open.

**Portia** — Always pass `campaign: portia` to the Multiversal Gateway. Use Sky in dialogue and narration and keep protected names and unrevealed identities out of the prompt. Fetch relevant approved lore and the latest confirmed scene through the GitHub app from `MyStalker/fantasia-campaign`. Cite the retrieved commit SHA and repository-relative path with each source. Keep Sky's response and voluntary actions open.

In both projects, model output is a noncanonical draft. Continue the existing GitHub archival workflow only with the DM's final sent text and the actual player's reply. The gateway cannot write either repository or advance a scene.

## Troubleshooting and rollback

- **The tool asks for no campaign, or reports v0.5.x.** The project is using the legacy app or an old tool schema. Select the shared app, refresh once, and recheck both project status calls.
- **Unknown campaign or card.** Check the exact campaign ID and its local card folder. Add only a verified card export belonging to that campaign. The gateway will never search another directory for a match.
- **Wrong source or identity error.** Rebuild the request from the selected project's confirmed context and verify its source references. If a legitimate same-world use of a common term triggers the identity check, review the request and refine the guard before sending it.
- **Oobabooga unreachable or model mismatch.** Check the loopback API, the inherited key if used, and the loaded model shown in status. Leave the gateway and project connection up while restoring the model.
- **Player agency.** A clean test does not guarantee every draft respects agency. If a draft decides the player's action, dialogue, or consent, discard or edit it before the DM sends anything.
- **Rollback.** Select the previous campaign-specific connector and launch its original command if needed. The staged pilot did not replace any legacy script, setting, card, tunnel, or chronology file.

## Pilot verification

The local MCP process used the same running Oobabooga instance for both routes. Both plain tests returned two sentences. In alternating NPC calls, Peri and Dusk addressed Lillia, and Beatrice addressed Sky. The drafts exposed no thinking markers and left the player's reply open. Automated tests exercised required IDs, foreign card rejection, source-scope rejection, payload formatting, sampler values, and reasoning cleanup. Shared ChatGPT registration and project-to-project tests are the remaining cutover checks.
