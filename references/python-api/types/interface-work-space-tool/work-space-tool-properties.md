# bpy.types.WorkSpaceTool: properties

## WorkSpaceTool(bpy_struct)

### WorkSpaceTool(bpy_struct) 

base class: bpy_struct
class bpy.types. WorkSpaceTool ( bpy_struct )
brush_type 

For brush-using tools restricted to one brush kind, the identifier of that brush kind (default 'DEFAULT' , readonly)

Type :

Literal[‘DEFAULT’]
has_datablock 

(default False, readonly)

Type :

bool
idname 

(default “”, never None)

Type :

str
idname_fallback 

(default “”, never None)

Type :

str
index 

(in [-inf, inf], default 0, readonly)

Type :

int
mode 

(default 'DEFAULT' , readonly)

Type :

Literal[‘DEFAULT’]
space_type 

(default 'EMPTY' , readonly)

Type :

Literal[Space Type Items]
use_brushes 

(default False, readonly)

Type :

bool
use_paint_canvas 

Whether the tool operates on a paint canvas (default False, readonly)

Type :

bool
widget 

(default “”, readonly, never None)

Type :

str

[Related references](INDEX.md).
