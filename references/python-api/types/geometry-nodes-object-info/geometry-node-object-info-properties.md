# bpy.types.GeometryNodeObjectInfo: properties

## GeometryNodeObjectInfo(GeometryNode)

### GeometryNodeObjectInfo(GeometryNode) 

base classes — bpy_struct, Node, NodeInternal, GeometryNode
class bpy.types. GeometryNodeObjectInfo ( GeometryNode ) 

Pull data out of an object.
transform_space 

Sets the frame the vector and geometry outputs are expressed in (default 'ORIGINAL' )

- ORIGINAL
Original – Give back the geometry in the input object's own transform, with location, rotation and scale measured against the world origin.

- RELATIVE
Relative – Pull the input object's geometry, location, rotation and scale into the modified object while preserving the two objects' relative placement in the scene.

Type :

Literal[‘ORIGINAL’, ‘RELATIVE’]

[Related references](INDEX.md).
