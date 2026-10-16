# bpy.types.XrSessionState: properties

## XrSessionState(bpy_struct)

### XrSessionState(bpy_struct) 

base class — bpy_struct
class bpy.types. XrSessionState ( bpy_struct ) 

Live state details for the current VR session
actionmaps 

(default None, readonly)

Type :

XrActionMaps[XrActionMap]
active_actionmap 

(in [-inf, inf], default 0)

Type :

int
navigation_location 

Positional offset added to the base pose when working out the viewer's location (array of 3 items, in [-inf, inf], default (0.0, 0.0, 0.0))

Type :

mathutils.Vector
navigation_rotation 

Rotational offset added to the base pose when working out the viewer's rotation (array of 4 items, in [-inf, inf], default (0.0, 0.0, 0.0, 0.0))

Type :

mathutils.Quaternion
navigation_scale 

Scale multiplier used when working out the viewer's scale (in [-inf, inf], default 0.0)

Type :

float
selected_actionmap 

(in [-inf, inf], default 0)

Type :

int
viewer_pose_location 

Most recent world-space location of the viewer pose (midpoint between the eyes) (array of 3 items, in [-inf, inf], default (0.0, 0.0, 0.0), readonly)

Type :

mathutils.Vector
viewer_pose_rotation 

Most recent world-space rotation of the viewer pose (midpoint between the eyes) (array of 4 items, in [-inf, inf], default (0.0, 0.0, 0.0, 0.0), readonly)

Type :

mathutils.Quaternion
viewer_scale 

VR viewer scale, derived from the navigation scale, the view-scale session setting, and the active scene's unit scale (in [-inf, inf], default 0.0, readonly)

Type :

float

[Related references](INDEX.md).
