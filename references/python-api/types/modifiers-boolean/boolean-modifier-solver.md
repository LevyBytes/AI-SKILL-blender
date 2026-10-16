# bpy.types.BooleanModifier: solver

solver

Which algorithm computes the Boolean result (default 'EXACT' )

- FLOAT
Float – A lightweight, fast solver that cannot cope with overlapping geometry.

- EXACT
Exact – A slower solver that handles coplanar faces most accurately.

- MANIFOLD
Manifold – The quickest solver; it requires manifold meshes but produces higher-quality output.

Type :

Literal['FLOAT', 'EXACT', 'MANIFOLD']

[Related references](INDEX.md).
