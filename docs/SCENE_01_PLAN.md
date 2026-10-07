# Scene 1 plan (Metro platform)

Plate: `art/backgrounds/metro_platform/metro_platform_v2.png` (2752 x 1536).
Plan overlay (round 2, measured): `art/backgrounds/metro_platform/metro_platform_v2_plan_r2.png`.
First-pass overlay, kept as history: `metro_platform_v2_plan.png`.

| Colour | Meaning | Items |
| --- | --- | --- |
| Green | Walkable floor | Platform tiles, stopping at the yellow safety line |
| Amber | Blocked | Bench, five column bases |
| Pink | Walk behind | Five columns (cut-outs are in the game repo) |
| Blue | Animation slots | Screens, centre sign, tall shaft (glyph rain, grin) |
| White | Exits | Stairs up, tunnel on the right |

The matching Godot scene is `scenes/rooms/metro_platform.tscn` in the game repo.
Measured values are in `docs/SUBWAY_BOUNDARIES.md` in the game repo. Untested in Godot.

The other five rooms each have a `*_plan_r2.png` beside their plate.
Plans for the two new districts: `SCENE_PACK_2_CITY_CENTRE.md` and `SCENE_PACK_3_OLD_CITY.md`.
