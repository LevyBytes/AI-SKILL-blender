# bpy.types.VertexWeightProximityModifier: falloff_type

falloff_type 

The mapping from old weights to their new values (default 'LINEAR' )

- LINEAR
Linear – Null action.

- CURVE
Custom Curve.

- SHARP
Sharp.

- SMOOTH
Smooth.

- ROOT
Root.

- `ICON_SPHERECURVE`
Sphere.

- RANDOM
Random.

- STEP
Median Step – Map all values below 0.5 to 0.0, and all others to 1.0.

Type :

Literal['LINEAR', 'CURVE', 'SHARP', 'SMOOTH', 'ROOT', '`ICON_SPHERECURVE`', 'RANDOM', 'STEP']

[Related references](INDEX.md).
