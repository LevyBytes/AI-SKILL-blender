# bpy.types.GreasePencilDashModifierSegment: properties

## GreasePencilDashModifierSegment(bpy_struct)

### GreasePencilDashModifierSegment(bpy_struct)

base class: bpy_struct
class bpy.types. GreasePencilDashModifierSegment ( bpy_struct )

Settings that define one dash segment.
dash

How many points in a row from the source stroke this segment keeps (in [1, 32767], default 2)

Type :

int
gap

How many points get skipped once this segment ends (in [0, 32767], default 1)

Type :

int
material_index

Index of the material applied to the generated segment; -1 keeps the existing material. (in [-1, 32767], default -1)

Type :

int
name

Name of the dash segment (default “”, never None)

Type :

str
opacity

Scale applied to the source point’s opacity when creating the new points (in [0, 1], default 1.0)

Type :

float
radius

Scale applied to the source point’s radius when creating the new points (in [0, 1], default 1.0)

Type :

float
use_cyclic

Make individual stroke dashes cyclic (default False)

Type :

bool

[Related references](INDEX.md).
