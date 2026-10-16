# bpy.types.XrActionMapBinding: properties

## XrActionMapBinding(bpy_struct)

### XrActionMapBinding(bpy_struct) 

base class — bpy_struct
class bpy.types. XrActionMapBinding ( bpy_struct ) 

A binding belonging to an XR action map item
axis0_region 

Which region of the first input axis triggers the action (default 'ANY' )

- ANY
Any – Use any axis region for operator execution.

- POSITIVE
Positive – Use positive axis region only for operator execution.

- NEGATIVE
Negative – Use negative axis region only for operator execution.

Type :

Literal[‘ANY’, ‘POSITIVE’, ‘NEGATIVE’]
axis1_region 

Which region of the second input axis triggers the action (default 'ANY' )

- ANY
Any – Use any axis region for operator execution.

- POSITIVE
Positive – Use positive axis region only for operator execution.

- NEGATIVE
Negative – Use negative axis region only for operator execution.

Type :

Literal[‘ANY’, ‘POSITIVE’, ‘NEGATIVE’]
component_paths 

The OpenXR component paths for this binding (default None, readonly)

Type :

XrComponentPaths[XrComponentPath]
name 

The action map binding's name (default “”, never None)

Type :

str
pose_location 

(array of 3 items, in [-inf, inf], default (0.0, 0.0, 0.0))

Type :

mathutils.Vector
pose_rotation 

(array of 3 items, in [-inf, inf], default (0.0, 0.0, 0.0))

Type :

mathutils.Euler
profile 

The OpenXR interaction-profile path (default “”, never None)

Type :

str
threshold 

Trigger threshold for button or axis actions (in [0, 1], default 0.0)

Type :

float

[Related references](INDEX.md).
