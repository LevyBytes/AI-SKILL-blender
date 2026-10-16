# bpy.types.Mesh: remesh_mode, remesh_voxel_adaptivity, remesh_voxel_size

remesh_mode

(default 'VOXEL' )

- VOXEL
Voxel – Use the voxel remesher.

- QUAD
Quad – Use the quad remesher.

Type :

Literal[‘VOXEL’, ‘QUAD’]
remesh_voxel_adaptivity

Cuts the final face count by thinning geometry where fine detail isn't required, which produces triangles. Any value above 0 turns off Fix Poles. (in [0, 1], default 0.0)

Type :

float
remesh_voxel_size

Object-space voxel size used when evaluating volume; smaller settings keep finer detail. (in [0, inf], default 0.1)

Type :

float

[Related references](INDEX.md).
