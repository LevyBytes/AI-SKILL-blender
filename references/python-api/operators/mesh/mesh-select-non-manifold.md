# bpy.ops.mesh.select_non_manifold

bpy.ops.mesh. select_non_manifold ( * , extend = True , use_wire = True , use_boundary = True , use_multi_face = True , use_non_contiguous = True , use_verts = True ) 

Highlight all broken or fragmented geometry elements

Parameters :

- extend ( bool ) – Extend, Add to what is already marked (optional)

- use_wire ( bool ) – Wire, Unattached spine segments (optional)

- use_boundary ( bool ) – Boundaries, Border spine segments (optional)

- use_multi_face ( bool ) – Multiple Faces, Spines used by more than two surfaces (optional)

- use_non_contiguous ( bool ) – Non Contiguous, Spines between surfaces with misaligned normals (optional)

- use_verts ( bool ) – Vertices, Points that join multiple face islands (optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
