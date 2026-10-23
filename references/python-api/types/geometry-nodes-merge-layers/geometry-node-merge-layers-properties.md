# bpy.types.GeometryNodeMergeLayers: properties

## GeometryNodeMergeLayers(GeometryNode)

### GeometryNodeMergeLayers(GeometryNode) 

base classes: bpy_struct, Node, NodeInternal, GeometryNode
class bpy.types. GeometryNodeMergeLayers ( GeometryNode ) 

Fold several Grease Pencil layers together into a single layer.
mode 

Sets the rule used to decide which layers get folded together (default '`MERGE_BY_NAME`' )

- `MERGE_BY_NAME`
By Name – Fold together every layer that shares the same name.

- `MERGE_BY_ID`
By Group ID – Assign your own group ID per layer; any layers carrying the same ID end up merged into one.

Type :

Literal[‘`MERGE_BY_NAME`’, ‘`MERGE_BY_ID`’]

[Related references](INDEX.md).
