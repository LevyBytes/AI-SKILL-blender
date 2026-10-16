# bpy.types.FreestyleLineStyle: thickness, thickness_modifiers, thickness_position, thickness_ratio

thickness 

Starting line thickness, which thickness modifiers may further adjust (in [0, 10000], default 3.0)

Type :

float
thickness_modifiers 

The set of line thickness modifiers attached to this style (default None, readonly)

Type :

LineStyleThicknessModifiers[LineStyleThicknessModifier]
thickness_position 

Where thickness sits relative to silhouette and border edges, used when plain chaining runs with Same Object (default 'CENTER' )

- CENTER
Center – Silhouettes and border edges are centered along stroke geometry.

- INSIDE
Inside – Silhouettes and border edges are drawn inside of stroke geometry.

- OUTSIDE
Outside – Silhouettes and border edges are drawn outside of stroke geometry.

- RELATIVE
Relative – Silhouettes and border edges are shifted by a user-defined ratio.

Type :

Literal[‘CENTER’, ‘INSIDE’, ‘OUTSIDE’, ‘RELATIVE’]
thickness_ratio 

A value from 0 (inside) to 1 (outside) that places the stroke thickness relative to the line (in [0, 1], default 0.5)

Type :

float

[Related references](INDEX.md).
