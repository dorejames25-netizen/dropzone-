# Scene pack 2: city centre (first-pass plan)

Source: `PROJECT-NIGHTMARE-FREQUENCY-ART/city-centre-scene-pack-2/` (local staging, not committed).
13 exports, all **2755 x 1540**. None is locked. Names below are proposals; James decides.

Status of every row: **candidate**. To lock one: export or crop to 2752 x 1536, save as
`art/backgrounds/<room>/<room>_v1.png`, then make the measured plan (`<room>_v1_plan.png`).

Plans here are written from reduced-size views. They list what the measured plan must mark,
not pixel positions.

## Catalogue

| # | Proposed room | Key colour | What it is | Verdict |
| --- | --- | --- | --- | --- |
| 1 | `neon_boulevard` | magenta | Wide avenue between glass towers, arcades both sides, bridge arch at the far end | Good room. Teal signs are strong; still reads magenta |
| 2 | `split_junction` | magenta + teal | Fork in the road, two corner buildings, left branch magenta, right branch teal | Good hub. Breaks "one key colour" on purpose (two districts meet). Needs James's OK |
| 3 | `lobby_front` | magenta | Stone frontage with three arched glass doors and a blank sign | Good room. Fits the street's "neon-lit double doors" |
| 4 | `tower_approach` | violet | Street running to a glowing gate far off, blank screens both sides | Good room. Fits the street's "tower district" exit |
| 5 | `alley_gate` | teal | Narrow alley, teal arch gateway, fuse box on the right wall | Good room. Fits the street's "alley" exit |
| 6 | `grand_stairs` | violet | Wide staircase up to a teal arch, big blank screen on the right | Good room. Floor is mostly steps, so walk area is small |
| 7 | `side_court` | teal | Raised terrace, door on the left, lit arch at the back, steps down in front | Good room. Three exits |
| 8 | `vista_city_magenta` | magenta | City skyline seen through a stone window | Not a walk room. Use as a look-out view or cutscene |
| 9 | `vista_city_teal` | teal | Second skyline through a window, river and bridges | Same as 8. Pick one, or use both in different rooms |
| 10 | `old_line_platform` | amber + green fog | A second metro platform, amber vault ribs, track on the right | Belongs with the subway set, not the city. Possible second station |
| 11 | `pillar_hall` | teal | Symmetrical hall of columns, arched door at the back, glowing floor disc | Good room. Candidate for the lobby interior |
| 12 | `arcade_avenue` | magenta | Long straight arcade, teal floor lines, arch at the far end | Good room, but close to 1. Keep one as the main street |
| 13 | `bridge_gate` | violet | Bridge with glass rails leading through a tall gothic arch | Good room. Natural link from city centre to old city |

## Corrections made (2026-10-07)

- **Size: fixed.** Named 2752 x 1536 copies are in `city-centre-scene-pack-2/sized_2752x1536/` as
  `<room>_candidate_v01.png`. Centre crop only (3 px off the width, 4 px off the height), no resampling. Originals untouched.
- Grid floors and the two-colour junction are style decisions, not errors. Left for James.

## Checks against the style standard

- Size: all 13 source exports are 2755 x 1540, not 2752 x 1536 (corrected copies above).
- Lighting: modern in every image (LED strips, neon tubes, bollard lights, ring lights). Pass.
- People, text, logos: none seen. Pass.
- Screens: blank black glass with thin frames. Pass.
- Floors: several have a glowing grid drawn into the tiles (1, 4, 6, 11, 12, 13). The six locked
  plates do not. James to decide if the grid is the city-centre look or drift.
- Line and texture: cleaner and less grimy than the subway plates. Judge at full size.

## First-pass plans

Colours as in the round 2 plans: green walkable, amber blocked, pink walk behind, blue animation, white exits.

### 1 `neon_boulevard`
- Walkable: the tiled road from the bottom edge to the bridge arch.
- Blocked: both arcades' column lines (floor stops at the kerb), low floor lights are not blockers.
- Walk behind: nearest arcade column on each side.
- Animation: four large tower screens (two left, two right), teal sign stacks, sky gap above the bridge.
- Exits: bridge arch (far), bottom edge, arcade openings left and right.

### 2 `split_junction`
- Walkable: the dark foreground road and both branches up to the fog line.
- Blocked: centre building wedge between the branches, kerbs, bollard bases.
- Walk behind: front bollards left and right.
- Animation: two tall violet door panels, two ring lights, far archway glow, puddle reflections.
- Exits: left branch (magenta), right branch (teal), centre far arch, bottom edge.

### 3 `lobby_front`
- Walkable: the pavement strip in front of the doors.
- Blocked: the wall line, the stone pier on the right.
- Walk behind: front bollard (left), right stone pier.
- Animation: blank sign above the doors, light panel on the right pier, three door glasses.
- Exits: left double doors (main), centre and right doors (locked or spare), left and right pavement edges.

### 4 `tower_approach`
- Walkable: the grid road between the two bollard rows, up to the fog.
- Blocked: bollard rows (as two lines), wall bases.
- Walk behind: the two nearest bollards.
- Animation: four framed screens on the right, two on the left, the far gate glow, sky gap.
- Exits: far gate (tower district), barred door on the left (locked), bottom edge.

### 5 `alley_gate`
- Walkable: the cobbled alley floor from the bottom edge to the gateway.
- Blocked: buttress on the left, wall and pipes on the right, bollards.
- Walk behind: front-left bollard, left buttress.
- Animation: wall screen on the right, fuse box light, gateway opening, floor up-lights.
- Exits: teal gateway (far), bottom edge. Only two; the fuse box can be an interaction point.

### 6 `grand_stairs`
- Walkable: the landing in front, the stair run (as one slope), the top landing.
- Blocked: both balustrades.
- Walk behind: left newel post and bollards.
- Animation: big screen on the right wall, small violet panels on both walls, blank sign over the arch.
- Exits: top arch, bottom edge.
- Note: scale changes a lot up the stairs. Needs a strong depth rule.

### 7 `side_court`
- Walkable: the upper terrace, the steps, the lower strip at the bottom.
- Blocked: terrace edge outside the steps, handrail, bollard line.
- Walk behind: left column, handrail.
- Animation: screen on the right wall, magenta wall panels, lit arch fog, left door glass.
- Exits: left door, back arch, steps down (bottom edge), right edge.

### 8 and 9 `vista_city_*`
- No walk area. One full-screen animation layer inside the window frame (glyph rain on the skyline).
- Use: a look-out the player triggers from another room. Returns to that room.

### 10 `old_line_platform`
- Walkable: platform floor up to the platform edge.
- Blocked: track bed (right), bench, wall line.
- Walk behind: front-left column with gargoyle, second column.
- Animation: hanging sign, three wall panels, tunnel mouth.
- Exits: tunnel (far right), arched doorway with stairs (centre back), bottom edge.

### 11 `pillar_hall`
- Walkable: the centre floor between the two colonnades.
- Blocked: column bases on both sides, the centre floor disc until its use is decided.
- Walk behind: front column on each side.
- Animation: two tall panels beside the door, door opening, ceiling light panels, floor disc.
- Exits: back arch door, bottom edge, side aisles left and right.
- Note: same open question as the control-room disc (pit, hologram or lift).

### 12 `arcade_avenue`
- Walkable: the centre lane between the two teal floor lines.
- Blocked: arcade column lines, bollards.
- Walk behind: front arch pier on each side.
- Animation: roof screens left and right, far arch, shop openings.
- Exits: far arch, bottom edge, arcade openings.

### 13 `bridge_gate`
- Walkable: the bridge deck from the bottom edge through the arch.
- Blocked: glass rails both sides, stone parapet in the foreground.
- Walk behind: foreground parapet, the arch itself (player passes under it).
- Animation: teal panel in the arch, wall screen on the left building, sky.
- Exits: through the arch, bottom edge.

## Proposed connections (not final)

```
 street_night --alley-------- alley_gate ---- side_court
      |
      +--right doorway------- lobby_front --- pillar_hall
      |
      +--tower district------ tower_approach
                                   |
 neon_boulevard --- split_junction-+--- grand_stairs --- (vista)
        |
   bridge_gate ------------------------------> old city (pack 3)
```
