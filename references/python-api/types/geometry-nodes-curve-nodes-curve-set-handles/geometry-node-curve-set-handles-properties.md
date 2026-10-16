# bpy.types.GeometryNodeCurveSetHandles: properties

## GeometryNodeCurveSetHandles(GeometryNode)

### GeometryNodeCurveSetHandles(GeometryNode)

base classes — bpy_struct, Node, NodeInternal, GeometryNode
class bpy.types. GeometryNodeCurveSetHandles ( GeometryNode )

Assign the handle type to the control points belonging to a Bézier curve.
handle_type

(default 'FREE' )

- FREE
Free – This handle is freely positionable and leaves the point's opposite handle alone.

- AUTO
Auto – Blender computes the position on its own to keep the curve smooth.

- VECTOR
Vector – The position is derived so the handle aims at the neighboring control point on either side.

- ALIGN
Align – The position is locked to face directly opposite the point's other handle.

Type :

Literal[‘FREE’, ‘AUTO’, ‘VECTOR’, ‘ALIGN’]
mode

Selects whether the left handle, the right handle, or both get updated (default set())

Type :

set[Literal[Node Geometry Curve Handle Side Items]]

[Related references](INDEX.md).
