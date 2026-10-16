# bpy.types.BevelModifier: limit_method

limit_method 

(default 'ANGLE' )

- NONE
None – Apply bevel uniformly across all edges.

- ANGLE
Angle – Restrict beveling to edges with sufficient angle between faces.

- WEIGHT
Weight – Use per-edge weights to control bevel depth.

- VGROUP
Vertex Group – Use group membership to determine what gets beveled.

Type :

Literal['NONE', 'ANGLE', 'WEIGHT', 'VGROUP']

[Related references](INDEX.md).
