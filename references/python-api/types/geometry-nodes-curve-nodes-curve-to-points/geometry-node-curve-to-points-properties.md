# bpy.types.GeometryNodeCurveToPoints: properties

## GeometryNodeCurveToPoints(GeometryNode)

### GeometryNodeCurveToPoints(GeometryNode)

base classes — bpy_struct, Node, NodeInternal, GeometryNode
class bpy.types. GeometryNodeCurveToPoints ( GeometryNode )

Sample positions along curves to build a point cloud.
mode

Picks the way points are produced from the input curve (default 'COUNT' )

- EVALUATED
Evaluated – Reuse the curve's evaluated points, which for NURBS and Bézier splines follow the resolution attribute.

- COUNT
Count – Spread the requested number of points evenly along each spline.

- LENGTH
Length – Cut each spline into segments of the requested length and sample those.

Type :

Literal[‘EVALUATED’, ‘COUNT’, ‘LENGTH’]

[Related references](INDEX.md).
