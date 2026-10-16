# bpy_extras.mesh_utils: bpy_extras.mesh_utils. ngon_tessellate ( from_data , indices , fix_loops = True , debug_print = True )

bpy_extras.mesh_utils. ngon_tessellate ( from_data , indices , fix_loops = True , debug_print = True ) 

Accepts a poly-line of indices (an ngon) and gives back a list of face
index lists. Intended for importers that need ngon indices in order to build
faces from existing verts.

Parameters :

- from_data (bpy.types.Mesh | list[Sequence[float]] | tuple[Sequence[float]]) – Either a mesh, or a list/tuple of 3D vectors.

- indices ( list [ int ] ) – a list of indices to use.
This list is the ordered closed poly-line to fill, and can be a subset of the data given.

- fix_loops ( bool ) – If this is enabled poly-lines
that use loops to make multiple
poly-lines are dealt with correctly.

- debug_print ( bool ) – Print debug information to the console.

Returns :

Tessellated faces as a list of triangle index tuples.

Return type :

list[tuple[int, int, int]]

[Related references](INDEX.md).
