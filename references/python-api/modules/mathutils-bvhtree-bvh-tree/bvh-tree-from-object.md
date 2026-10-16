# mathutils.bvhtree.BVHTree: classmethod FromObject ( object , depsgraph , * , deform = True , cage = False , epsilon = 0.0 )

classmethod FromObject ( object , depsgraph , * , deform = True , cage = False , epsilon = 0.0 )

Build a BVH tree out of Object data.

Parameters :

- object ( Object ) – Mesh object.

- depsgraph ( Depsgraph ) – Depsgraph to use for evaluating the mesh.

- deform ( bool ) – Use mesh with deformations.

- cage ( bool ) – Use modifiers cage.

- epsilon ( float ) – Increase the threshold for detecting overlap and raycast hits.

Returns :

BVHTree from Object data.

Return type :

BVHTree

[Related references](INDEX.md).
