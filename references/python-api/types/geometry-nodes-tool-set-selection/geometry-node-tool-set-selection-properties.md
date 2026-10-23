# bpy.types.GeometryNodeToolSetSelection: properties

## GeometryNodeToolSetSelection(GeometryNode)

### GeometryNodeToolSetSelection(GeometryNode)

base classes: bpy_struct, Node, NodeInternal, GeometryNode
class bpy.types. GeometryNodeToolSetSelection ( GeometryNode )

During a tool run, writes the selection state back onto the geometry being edited.
domain

(default 'POINT' )

Type :

Literal[Attribute Domain Point Edge Face Curve Items]
selection_type

(default 'BOOLEAN' )

- BOOLEAN
Boolean – Keeps the selection as true/false values while in edit mode.

- FLOAT
Float – Keeps the selection as floating-point values; on mesh geometry these are held inverted and used as the sculpt-mode mask.

Type :

Literal[‘BOOLEAN’, ‘FLOAT’]

[Related references](INDEX.md).
