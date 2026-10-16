# bpy.types.ToolSettings: use_keyframe_cycle_aware, use_keyframe_insert_auto, use_keyframe_insert_keyingset

use_keyframe_cycle_aware 

On channels with cyclic extrapolation, inserted keyframes are remapped into the cycle’s time range and the ends are kept matched. Curves freshly added to actions that use a Manual Frame Range with Cyclic Animation become cyclic automatically. (default False)

Type :

bool
use_keyframe_insert_auto 

Insert keyframes automatically when properties change (default True)

Type :

bool
use_keyframe_insert_keyingset 

Use only the active Keying Set for automatic keyframe insertion (default False)

Type :

bool

[Related references](INDEX.md).
