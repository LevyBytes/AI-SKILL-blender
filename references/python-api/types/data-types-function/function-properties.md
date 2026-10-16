# bpy.types.Function: properties

## Function(bpy_struct)

### Function(bpy_struct) 

base class — bpy_struct
class bpy.types. Function ( bpy_struct ) 

The definition of an RNA function
description 

Text explaining what the function is for (default “”, readonly, never None)

Type :

str
identifier 

The unique name the function carries in code and scripting (default “”, readonly, never None)

Type :

str
is_registered 

Whether the function was registered as a callback during type registration (default False, readonly)

Type :

bool
is_registered_optional 

Whether the function was optionally registered as a callback during type registration (default False, readonly)

Type :

bool
parameters 

The arguments this function accepts (default None, readonly)

Type :

bpy_prop_collection[Property]
use_self 

The function omits itself as an argument, turning into a static method in Python (default False, readonly)

Type :

bool
use_self_type 

The function receives its own type as an argument, turning into a class method in Python when use_self is false (default False, readonly)

Type :

bool

[Related references](INDEX.md).
