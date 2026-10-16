# bpy.types.CameraDOFSettings: properties

## CameraDOFSettings(bpy_struct)

### CameraDOFSettings(bpy_struct)

base class — bpy_struct
class bpy.types. CameraDOFSettings ( bpy_struct )

Depth of Field configuration
aperture_blades

Blade count for bokeh shape (minimum 3) (in [0, 16], default 0)

Type :

int
aperture_fstop

F-number (lower = more blur, higher = sharper) (in [0, inf], default 2.8)

Type :

float
aperture_ratio

Anamorphic bokeh distortion (in [0.01, inf], default 1.0)

Type :

float
aperture_rotation

Blade rotation angle (in [-3.14159, 3.14159], default 0.0)

Type :

float
focus_distance

Distance from camera to focal plane (in [0, inf], default 10.0)

Type :

float
focus_object

Object to use as focus point

Type :

Object
focus_subtarget

Armature bone or deforming group for focus (default "", never None)

Type :

str
use_dof

Activate depth of field (default False)

Type :

bool

[Related references](INDEX.md).
