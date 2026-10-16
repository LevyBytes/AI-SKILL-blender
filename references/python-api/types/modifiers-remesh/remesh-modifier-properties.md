# bpy.types.RemeshModifier: properties

## RemeshModifier(Modifier)

### RemeshModifier(Modifier) 

base classes — bpy_struct, Modifier
class bpy.types. RemeshModifier ( Modifier ) 

Build a fresh surface with even topology that conforms to the input mesh's shape
adaptivity 

Lowers the final face count by simplifying areas that need little detail, producing triangles. Any value above 0 turns off Fix Poles. (in [-inf, inf], default 0.0)

Type :

float
mode 

(default 'VOXEL' )

- BLOCKS
Blocks – Output a blocky surface with no smoothing.

- SMOOTH
Smooth – Output a smooth surface with no sharp-features detection.

- SHARP
Sharp – Output a surface that reproduces sharp edges and corners from the input mesh.

- VOXEL
Voxel – Output a mesh corresponding to the volume of the original mesh.

Type :

Literal[‘BLOCKS’, ‘SMOOTH’, ‘SHARP’, ‘VOXEL’]
octree_depth 

The octree resolution; larger values yield finer detail (in [1, 24], default 4)

Type :

int
scale 

How the model's largest dimension compares to the grid size (in [0, 0.99], default 0.9)

Type :

float
sharpness 

How much outliers are tolerated; smaller values cut noise while larger ones track input edges more closely (in [-inf, inf], default 1.0)

Type :

float
threshold 

When stripping out disconnected pieces, the smallest component size to keep, given as a fraction of the polygon count of the largest component (in [0, 1], default 1.0)

Type :

float
use_remove_disconnected 

(default True)

Type :

bool
use_smooth_shade 

Produce smooth-shaded faces in place of flat-shaded ones (default False)

Type :

bool
voxel_size 

The voxel size, in object space, used to evaluate the volume. Smaller values keep finer detail. (in [0, inf], default 0.1)

Type :

float

[Related references](INDEX.md).
