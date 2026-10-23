# bpy.types.GeometryNodeSampleCurve: properties

## GeometryNodeSampleCurve(GeometryNode)

### GeometryNodeSampleCurve(GeometryNode)

base classes: bpy_struct, Node, NodeInternal, GeometryNode
class bpy.types. GeometryNodeSampleCurve ( GeometryNode )

Read data at a point that lies a given distance along a curve from its start
data_type

(default 'FLOAT' )

Type :

Literal[Attribute Type Items]
mode

Method for sampling input (default 'FACTOR' )

- FACTOR
Factor – Locate sample positions along the curve as a fraction of its full length.

- LENGTH
Length – Locate sample positions along the curve as a distance measured from its start.

Type :

Literal[‘FACTOR’, ‘LENGTH’]
use_all_curves

Base the sample lengths on the combined length of every curve instead of measuring within each selected curve (default False)

Type :

bool

[Related references](INDEX.md).
