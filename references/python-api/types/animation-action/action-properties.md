# bpy.types.Action: properties

## Action(ID)

### Action(ID)

base classes: bpy_struct, ID
class bpy.types.Action(ID)

A set of F-Curves for keyframe animation
curve_frame_range

The combined frame range across all F-Curves in this action (array of 2 items, [-inf, inf], default (0.0, 0.0), readonly)

Type: mathutils.Vector
frame_end

The final frame of the manually configured playback range ([-1.04857e+06, 1.04857e+06], default 0.0)

Type: float
frame_range

The intended playback frame span of this action, using manual range if set, otherwise combining all F-Curve ranges; assignment sets the manual range (array of 2 items, [-inf, inf], default (0.0, 0.0))

Type: mathutils.Vector
frame_start

The first frame of the manually configured playback range ([-1.04857e+06, 1.04857e+06], default 0.0)

Type: float
is_action_layered

Returns whether this is a layered Action. Since version 4.4, all actions become layered through automatic upgrading, so this always returns true (default False, readonly)

Type: bool
is_action_legacy

Returns whether this is a legacy Action without layers or slots. Legacy Actions only appear on newly created empty actions, as Blender 4.4+ automatically converts them. This returns true only for unused actions (default False, readonly)

Type: bool
is_empty

False when any Layer, Slot, or legacy F-Curve exists (default False, readonly)

Type: bool
layers

A list of animation layers comprising this Action (default None, readonly)

Type: ActionLayers[ActionLayer]
pose_markers

Markers assigned to this action for identifying key poses (default None, readonly)

Type: ActionPoseMarkers[TimelineMarker]
slots

A list of slots in this Action (default None, readonly)

Type: ActionSlots[ActionSlot]
use_cyclic

This action is intended to cycle over its manually set playback range (enabling does not auto-loop; it is a hint to tools) (default False)

Type: bool
use_frame_range

Manually configure the playback frame range (used by some tools but does not affect evaluation) (default False)

Type: bool

[Related references](INDEX.md).
