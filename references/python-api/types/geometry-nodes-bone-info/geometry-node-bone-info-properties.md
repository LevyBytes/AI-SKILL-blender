# bpy.types.GeometryNodeBoneInfo: properties

## GeometryNodeBoneInfo(GeometryNode)

### GeometryNodeBoneInfo(GeometryNode)

base classes — bpy_struct, Node, NodeInternal, GeometryNode
class bpy.types. GeometryNodeBoneInfo ( GeometryNode )

Pulls information about the bones of an armature.
transform_space

How the vector and geometry outputs are transformed (default 'ORIGINAL' )

- ORIGINAL
Original – Give the bone pose measured against the armature object's transform.

- RELATIVE
Relative – Express the pose within the coordinate frame of the modified object.

Type :

Literal[‘ORIGINAL’, ‘RELATIVE’]

[Related references](INDEX.md).
