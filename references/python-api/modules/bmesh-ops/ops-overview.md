# bmesh.ops: overview

[Open the complete example modules](../../examples/bmesh-chain/INDEX.md).
- matrix (mathutils.Matrix) – Matrix defining rotation.

- verts (list[bmesh.types.BMVert]) – Input vertices.

- space (mathutils.Matrix) – Matrix to define the space (typically object matrix).

- use_shapekey ( bool ) – Transform shape keys too.
- steps ( int ) – Number of steps.

- use_merge ( bool ) – Merge first/last when the angle is a full revolution.

- use_normal_flip ( bool ) – Create faces with reversed direction.

- use_duplicate ( bool ) – Duplicate the geometry, otherwise extrude.

Returns :

- geom_last :
Result of last step.

type list[bmesh.types.BMVert | bmesh.types.BMEdge | bmesh.types.BMFace]

Return type :

dict[str, Any]

[Related references](INDEX.md).
