# bmesh.ops: bmesh.ops. mesh_to_bmesh ( bm , mesh , object , use_shapekey = False )

bmesh.ops. mesh_to_bmesh ( bm , mesh , object , use_shapekey = False ) 

Mesh to BMesh.

Load the contents of a mesh into the bmesh. this BMOP is private, it's
reserved exclusively for entering edit-mode.

Parameters :

- bm (bmesh.types.BMesh) – The bmesh to operate on.

- mesh (bpy.types.Mesh) – The mesh to read from.

- object (bpy.types.Object) – The object.

- use_shapekey ( bool ) – Load active shapekey coordinates into verts.

[Related references](INDEX.md).
