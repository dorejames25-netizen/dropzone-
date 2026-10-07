# Room layout (first section)

Locked plates, all 2752 x 1536, modern lighting. Plans sit beside each plate: `*_plan_r2.png` is the measured round 2 plan, `*_plan.png` is the first pass.

| Room | Plate | Key colour |
| --- | --- | --- |
| Metro platform (start) | `art/backgrounds/metro_platform/metro_platform_v2.png` | magenta |
| Station concourse | `art/backgrounds/station_concourse/station_concourse_v1.png` | emerald green |
| Street at night | `art/backgrounds/street_night/street_night_v1.png` | teal |
| Service corridor | `art/backgrounds/service_corridor/service_corridor_v1.png` | amber LED with magenta |
| Control room | `art/backgrounds/control_room/control_room_v1.png` | cold blue with magenta |
| The tunnel | `art/backgrounds/tunnel/tunnel_v1.png` | magenta fog with green |

`metro_platform_v1.png` (old lantern lighting) is superseded and kept only as history.

## How the rooms connect

```
                    street (alley, right doorway, tower district: not built)
                       |
 platform --stairs-- concourse --service passage-- service corridor -- control room -- stairs up (not built)
    |                                                    |
    +------tunnel------ ladder up ----------------------+
                  |
             sealed gate (locked)
```

| From | Exit | To |
| --- | --- | --- |
| Metro platform | Stairs | Station concourse |
| Metro platform | Tunnel | The tunnel |
| Station concourse | Stairs | Metro platform |
| Station concourse | Street doors | Street at night |
| Station concourse | Service passage | Service corridor |
| Street at night | Bottom edge | Station concourse |
| Street at night | Alley, right doorway, tower district | Not built |
| Service corridor | Far steel door | Control room |
| Service corridor | Side door | Station concourse |
| Control room | Door | Service corridor |
| Control room | Stairs up | Not built |
| The tunnel | Ladder | Service corridor |
| The tunnel | Sealed gate | Locked |
| The tunnel | Back to platform | Metro platform |

The same data is in `data/rooms/rooms.json` in the game repo.

## Rooms still to make

1. **Upper control level**: where the control room's stairs go. No art yet.
2. **Neon-door lobby / tower district**: the street's right doorway and far tower. Candidates now exist in scene pack 2 (`lobby_front`, `pillar_hall`, `tower_approach`, `alley_gate`).

## Next sections (candidates, nothing locked)

| Section | Images | Plan doc |
| --- | --- | --- |
| City centre | 13 exports, 11 usable as rooms or views | `docs/SCENE_PACK_2_CITY_CENTRE.md` |
| Old city | 10 exports, 7 usable as rooms, 3 need work | `docs/SCENE_PACK_3_OLD_CITY.md` |

Room names in those docs are proposals. A room joins the table above only when its plate is locked at 2752 x 1536.
