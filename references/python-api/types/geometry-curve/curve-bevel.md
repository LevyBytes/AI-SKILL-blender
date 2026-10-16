# bpy.types.Curve: bevel_depth, bevel_factor_end, bevel_factor_mapping_end, bevel_factor_mapping_start, bevel_factor_start, bevel_mode, bevel_object, bevel_profile, bevel_resolution

bevel_depth

How wide the bevel geometry reaches, before any extrusion is added (in [-inf, inf], default 0.0)

Type :

float
bevel_factor_end

Set the point along the spline where the curve geometry stops (0 at the start, 1 at the end) (in [0, 1], default 1.0)

Type :

float
bevel_factor_mapping_end

Pick how the end factor for the geometry is projected onto a spline (default 'RESOLUTION' )

- RESOLUTION
Resolution – Tie the geometry factor to a spline's subdivision count (its U resolution).

- SEGMENTS
Segments – Tie the geometry factor both to a segment's length and to how many subdivisions that segment has.

- SPLINE
Spline – Tie the geometry factor to the overall length of a spline.

Type :

Literal['RESOLUTION', 'SEGMENTS', 'SPLINE']
bevel_factor_mapping_start

Pick how the start factor for the geometry is projected onto a spline (default 'RESOLUTION' )

- RESOLUTION
Resolution – Tie the geometry factor to a spline's subdivision count (its U resolution).

- SEGMENTS
Segments – Tie the geometry factor both to a segment's length and to how many subdivisions that segment has.

- SPLINE
Spline – Tie the geometry factor to the overall length of a spline.

Type :

Literal['RESOLUTION', 'SEGMENTS', 'SPLINE']
bevel_factor_start

Set the point along the spline where the curve geometry begins (0 at the start, 1 at the end) (in [0, 1], default 0.0)

Type :

float
bevel_mode

Pick the method used to build the curve's bevel geometry (default 'ROUND' )

- ROUND
Round – Shape the bevel cross-section as a circle.

- OBJECT
Object – Drive the bevel cross-section from a chosen object.

- PROFILE
Profile – Apply a custom profile across each quarter of the bevel geometry.

Type :

Literal['ROUND', 'OBJECT', 'PROFILE']
bevel_object

The name of the Curve object that defines the bevel shape

Type :

Object
bevel_profile

The path for the curve's custom profile (readonly)

Type :

CurveProfile
bevel_resolution

How many segments make up each quarter-circle of the bevel (in [0, 32], default 4)

Type :

int

[Related references](INDEX.md).
