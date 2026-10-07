# Scene pack 3: old city (first-pass plan)

Source: `PROJECT-NIGHTMARE-FREQUENCY-ART/old-city-scene-pack-3/` (local staging, not committed).
10 exports, all **2755 x 1540**. None is locked. Names below are proposals; James decides.

Status of every row: **candidate**. To lock one: export or crop to 2752 x 1536, save as
`art/backgrounds/<room>/<room>_v1.png`, then make the measured plan (`<room>_v1_plan.png`).

Plans here are written from reduced-size views. They list what the measured plan must mark,
not pixel positions.

District look: red stone, with green and violet neon as second colours.

## Catalogue

| # | Proposed room | Key colour | What it is | Verdict |
| --- | --- | --- | --- | --- |
| 1 | `back_alley` | red | Dead-end alley, barred double gate under a neon arch, crates, wall monitor | Good room |
| 2 | `old_street` | red | Street of gothic fronts, booth on the left, archway on the right | Good room, **one fix needed** (the booth, see below) |
| 3 | `ruin_court` | red + violet | Roofless courtyard, tall arch at the back, green gate left, steps right | Good room. Three exits |
| 4 | `cloister` | red | Vaulted corridor, red door left, green door right, portcullis at the end | Good room |
| 5 | `cathedral_front` | violet | Outside of the great hall, double doors, wide steps | Good room. Establishing shot |
| 6 | `cathedral_nave` | violet | Inside: columns, bench rows, tall arch at the back, side doors | Good room |
| 7 | `vault_room` | red + green | Small vaulted room, stone bench, three doors | Good room. Works as a safe room or puzzle room |
| 8 | `stair_landing` | red | Stair landing seen at a steep tilt | **Fails the camera rule** (not eye height, tilted). Cutscene only, or redo |
| 9 | `vista_old_city_violet` | violet | Old-city roofs through a window, three gargoyles | Not a walk room. **Not full frame** (black margins) |
| 10 | `vista_old_city_green` | green | Courtyard and far towers through a glazed window | Not a walk room. **Not full frame** (black margins) |

## Corrections made (2026-10-07)

- **Size: fixed.** Named 2752 x 1536 copies are in `old-city-scene-pack-3/sized_2752x1536/` as
  `<room>_candidate_v01.png`. Centre crop only (3 px off the width, 4 px off the height), no resampling. Originals untouched.
- **#2 kiosk and #8 camera: not fixable by cropping.** Firefly prompts are in `prompts/pack_3_fixes.md`.
- **#9, #10 framing:** margins measured at about 100 px (#9) and 215 px (#10) each side. Left as they are; fine for a view.

## Checks against the style standard

- Size: all 10 source exports are 2755 x 1540, not 2752 x 1536 (corrected copies above).
- **#2 booth:** it is a red telephone kiosk with crown emblems, which reads as a real-world design.
  The standing rule is original designs only. Regenerate or paint out the crowns and change the shape.
- **#8:** tilted camera. Standard says standing eye height.
- **#9, #10:** image does not fill the frame. Fine for a vista layer if cropped; not usable as plates as they are.
- Lighting: neon tubes, LED strips, ring lights and caged work lights. Modern. Pass.
  The caged lights in 1, 2, 4 and 7 are white; the standard asks for the room's own colours. Minor.
- Religious symbols: none seen at full size on the #1 gate. The hall in 5 and 6 is gothic architecture
  only. Check 5 and 6 once more at full size before locking.
- People, text, logos: none seen, apart from the crowns in #2.
- Texture: red stone is grimier than pack 2 and closer to the subway plates.

## First-pass plans

Colours as in the round 2 plans: green walkable, amber blocked, pink walk behind, blue animation, white exits.

### 1 `back_alley`
- Walkable: the flagstone floor from the bottom edge to the gate.
- Blocked: crates and barrel (right of the gate), pipe wall on the left, cable wall on the right.
- Walk behind: left pipe stack, foreground crate corner (bottom right).
- Animation: wall monitor (right), fuse box (left), ring light above the gate, puddles.
- Exits: barred gate (locked at first), bottom edge. Needs a second exit; the dark opening above the gate wall could be a ladder.

### 2 `old_street`
- Walkable: the paved road, and the raised pavement on the right.
- Blocked: booth, iron railings, kerb edge on the right, building fronts.
- Walk behind: booth, right archway pier.
- Animation: booth glass, ring above the booth, panel on the right pier, far-end glow.
- Exits: far end of the street, right archway, bottom edge.

### 3 `ruin_court`
- Walkable: the courtyard flagstones.
- Blocked: wall bases, steps on the right (as a slope to the door).
- Walk behind: left wall buttress.
- Animation: tall centre arch opening, violet panel (left wall), small window lights, open sky.
- Exits: centre arch, green gate (left), stepped door (right), bottom edge.

### 4 `cloister`
- Walkable: the corridor floor to the portcullis.
- Blocked: wall lines only. Clear room.
- Walk behind: front arch piers left and right.
- Animation: small wall panels (four), door openings.
- Exits: red door (left), green door (right), portcullis (far, locked at first), bottom edge.

### 5 `cathedral_front`
- Walkable: the forecourt and the steps up to the doors.
- Blocked: building line, tower bases.
- Walk behind: none needed. Optional foreground kerb.
- Animation: round window, door glass, four side windows, sky, tower masts.
- Exits: main doors, left and right forecourt edges, bottom edge.

### 6 `cathedral_nave`
- Walkable: the centre aisle and the front cross-aisle.
- Blocked: both bench blocks, column bases.
- Walk behind: front column on each side.
- Animation: tall back arch, vault ribs, bench screens (blank dark tops), ring lights on the columns.
- Exits: back arch, green side door (left), red side door (right), bottom edge.

### 7 `vault_room`
- Walkable: the whole floor.
- Blocked: stone bench at the back wall.
- Walk behind: left front arch pier.
- Animation: red wall panel, ceiling rings, green window (right).
- Exits: violet door (left), green door (back), bottom edge. The green window is a view, not an exit.

### 8 `stair_landing`
- No plan until the camera is decided. If kept, use as a transition still between `cloister` and an upper floor.

### 9 and 10 `vista_old_city_*`
- No walk area. One animation layer inside the window frame. Crop to the window before use.

## Proposed connections (not final)

```
 bridge_gate (pack 2) --- old_street --- back_alley
                              |
                          ruin_court --- cloister --- vault_room
                              |              |
                       cathedral_front   stair_landing --- (vista)
                              |
                        cathedral_nave
```
