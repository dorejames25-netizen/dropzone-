# dropzone- (Nightmare Frequency art and story)

The art master, prompts and story for **Nightmare Frequency**, a cyberpunk-gothic noir
adventure. The game itself lives in the companion repository, `project-nightmare-frequency`.
Only finished, game-ready files are copied from here into the game.

## Folder guide

| Folder | What goes there |
| --- | --- |
| `story/` | The story and world guide (PDF), plus the script that builds it in `story/tools/` |
| `prompts/` | Image-generator prompts, including the project brief that opens every session |
| `art/references/` | Style references we judge new art against |
| `art/backgrounds/<room>/` | Final room plates and plans, one folder per room |
| `art/sprites/` | `player`, `enemies`, `npcs` |
| `art/fx/` | Effect art, including `glyph_rain` |
| `art/ui/` | HUD and menu art |
| `third-party/` | Third-party packs, each with its own licence file beside it |
| `docs/` | Style standard and notes |

## Rules

- Large files (png, jpg, psd, pdf, models, audio) go through Git LFS, set in `.gitattributes`.
- Keep raw exports out of the repo. Put them in `raw/`, which is ignored.
- Name files `room_or_asset_v1.png`, then `v2` and so on. Do not overwrite a locked version.
- Original names and designs only. No real brands, logos or characters, and no real-world religious symbols.

## Ownership

Copyright (c) 2026 James Dore. All rights reserved. See `LICENSE`.
