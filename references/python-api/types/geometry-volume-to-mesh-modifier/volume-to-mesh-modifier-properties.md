# bpy.types.VolumeToMeshModifier: properties

## VolumeToMeshModifier(Modifier)

### VolumeToMeshModifier(Modifier)

base classes — bpy_struct, Modifier
class bpy.types. VolumeToMeshModifier ( Modifier )
adaptivity

Cuts the final face count by thinning out geometry wherever detail isn't required (in [0, 1], default 0.0)

Type :

float
grid_name

Which grid inside the volume object gets turned into a mesh (default "", never None)

Type :

str
object

Object

Type :

Object
resolution_mode

How the target voxel size gets specified (default 'GRID' )

- GRID
Grid – Adopt the resolution of the volume grid.

- `VOXEL_AMOUNT`
Voxel Amount – Target a voxel count along a single axis.

- `VOXEL_SIZE`
Voxel Size – Target a specific voxel edge length.

Type :

Literal['GRID', '`VOXEL_AMOUNT`', '`VOXEL_SIZE`']
threshold

Voxels above this value end up inside the resulting mesh (in [0, inf], default 0.0)

Type :

float
use_smooth_shade

Emit smooth-shaded faces in place of flat-shaded ones (default False)

Type :

bool
voxel_amount

Roughly how many voxels lie along one axis (in [0, inf], default 0)

Type :

int
voxel_size

The smaller this is, the finer the output resolution (in [0, inf], default 0.0)

Type :

float

[Related references](INDEX.md).
