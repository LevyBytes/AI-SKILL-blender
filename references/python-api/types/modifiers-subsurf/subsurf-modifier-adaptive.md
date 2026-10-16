# bpy.types.SubsurfModifier: adaptive_object_edge_length, adaptive_pixel_size, adaptive_space

adaptive_object_edge_length

Target object space edge length for adaptive subdivision (in [0.0001, 1000], default 0.01)

Type :

float
adaptive_pixel_size

Target polygon pixel size for adaptive subdivision (in [0.1, 1000], default 1.0)

Type :

float
adaptive_space

How to adaptively subdivide the mesh (default 'PIXEL' )

- PIXEL
Pixel – Subdivide polygons to reach a specified pixel size on screen.

- OBJECT
Object – Subdivide to reach a specified edge length in object space. This is required to use adaptive subdivision for instanced meshes.

Type :

Literal[‘PIXEL’, ‘OBJECT’]

[Related references](INDEX.md).
