# bpy.types.GeometryNodeSetGreasePencilColor: properties

## GeometryNodeSetGreasePencilColor(GeometryNode)

### GeometryNodeSetGreasePencilColor(GeometryNode) 

base classes: bpy_struct, Node, NodeInternal, GeometryNode
class bpy.types. GeometryNodeSetGreasePencilColor ( GeometryNode ) 

Writes color and opacity attributes onto Grease Pencil geometry.
mode 

(default 'STROKE' )

- STROKE
Stroke – Applies the color and opacity to the individual points making up a stroke.

- FILL
Fill – Applies the color and opacity to the fills enclosed by strokes.

Type :

Literal[‘STROKE’, ‘FILL’]

[Related references](INDEX.md).
