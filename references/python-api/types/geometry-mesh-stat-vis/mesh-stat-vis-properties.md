# bpy.types.MeshStatVis: properties

## MeshStatVis(bpy_struct)

### MeshStatVis(bpy_struct)

base class — bpy_struct
class bpy.types. MeshStatVis ( bpy_struct )
distort_max

Maximum angle to display (in [0, 3.14159], default 0.785398)

Type :

float
distort_min

Minimum angle to display (in [0, 3.14159], default 0.0872665)

Type :

float
overhang_axis

(default '`NEG_Z`' )

Type :

Literal[Object Axis Items]
overhang_max

Maximum angle to display (in [0, 3.14159], default 0.785398)

Type :

float
overhang_min

Minimum angle to display (in [0, 3.14159], default 0.0)

Type :

float
sharp_max

Maximum angle to display (in [-3.14159, 3.14159], default 3.14159)

Type :

float
sharp_min

Minimum angle to display (in [-3.14159, 3.14159], default 1.5708)

Type :

float
thickness_max

Maximum for measuring thickness (in [0, 1000], default 0.1)

Type :

float
thickness_min

Minimum for measuring thickness (in [0, 1000], default 0.0)

Type :

float
thickness_samples

Number of samples to test per face (in [1, 32], default 1)

Type :

int
type

Type of data to visualize/check (default 'OVERHANG' )

Type :

Literal[‘OVERHANG’, ‘THICKNESS’, ‘INTERSECT’, ‘DISTORT’, ‘SHARP’]

[Related references](INDEX.md).
