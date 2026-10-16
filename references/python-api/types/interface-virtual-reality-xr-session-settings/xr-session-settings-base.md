# bpy.types.XrSessionSettings: base_pose_angle, base_pose_location, base_pose_object, base_pose_type, base_scale

base_pose_angle 

Z-axis rotation that the VR headset's rotation deltas are applied on top of (in [-inf, inf], default 0.0)

Type :

float
base_pose_location 

Origin point that the headset's translation deltas are added to (array of 3 items, in [-inf, inf], default (0.0, 0.0, 0.0))

Type :

mathutils.Vector
base_pose_object 

Object whose location and rotation the headset's translation and rotation deltas build upon

Type :

Object
base_pose_type 

Source of the VR view's base location and rotation, onto which the headset's translation and rotation deltas are added (default '`SCENE_CAMERA`' )

- `SCENE_CAMERA`
Scene Camera – Follow the active scene camera to define the VR view’s base pose.

- OBJECT
Object – Follow the transformation of an object to define the VR view’s base pose.

- CUSTOM
Custom – Follow a custom transformation to define the VR view’s base pose.

Type :

Literal[‘`SCENE_CAMERA`’, ‘OBJECT’, ‘CUSTOM’]
base_scale 

Uniform scale of the base pose used for the VR view (in [1e-06, inf], default 1.0)

Type :

float

[Related references](INDEX.md).
