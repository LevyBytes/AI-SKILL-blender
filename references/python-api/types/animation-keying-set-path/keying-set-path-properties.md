# bpy.types.KeyingSetPath: properties

## KeyingSetPath(bpy_struct)

### KeyingSetPath(bpy_struct) 

base class: bpy_struct
class bpy.types. KeyingSetPath ( bpy_struct ) 

Points at a single setting that a Keying Set targets
array_index 

For settings that apply, this selects which individual entry is used (in [-inf, inf], default 0)

Type :

int
data_path 

RNA path identifying the property being keyed (default “”, never None)

Type :

str
group 

Action Group name that this path's keyframes get filed under (default “”, never None)

Type :

str
group_method 

Chooses how the Group name for this path is determined (default 'NAMED' )

Type :

Literal[Keyingset Path Grouping Items]
id 

The ID-Block whose keyframes the Keying Set writes to (relevant only for Absolute Keying Sets)

Type :

ID
id_type 

Which kind of ID-block is permitted here (default 'OBJECT' )

Type :

Literal[Id Type Items]
use_entire_array 

For an 'array/vector' property such as Location, Rotation, or Color, key the whole array at once (default False)

Type :

bool
use_insertkey_needed 

Restrict insertion to the F-Curves that actually require a new keyframe (default False)

Type :

bool
use_insertkey_override_needed 

Replace the default so that keyframes go only where the relevant F-Curves call for them (default False)

Type :

bool
use_insertkey_override_visual 

Replace the default so that keyframes capture 'visual transforms' (default False)

Type :

bool
use_insertkey_visual 

Record keyframes from 'visual transforms' (default False)

Type :

bool

[Related references](INDEX.md).
