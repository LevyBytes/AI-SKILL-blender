# bpy.types.GeometryNodeCollectionInfo: properties

## GeometryNodeCollectionInfo(GeometryNode)

### GeometryNodeCollectionInfo(GeometryNode)

base classes — bpy_struct, Node, NodeInternal, GeometryNode
class bpy.types. GeometryNodeCollectionInfo ( GeometryNode )

Pull instances of geometry out of a collection.
transform_space

Controls how the output instances are placed in space; the geometry stored internally is left untouched (default 'ORIGINAL' )

- ORIGINAL
Original – Emit the geometry positioned against the collection's own offset.

- RELATIVE
Relative – Pull the collection geometry into the modified object while preserving how the source objects sit relative to one another in the scene.

Type :

Literal[‘ORIGINAL’, ‘RELATIVE’]

[Related references](INDEX.md).
