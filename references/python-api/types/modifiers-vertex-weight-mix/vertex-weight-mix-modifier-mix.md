# bpy.types.VertexWeightMixModifier: mix_mode, mix_set

mix_mode 

The way VGroup B's weights modify those of VGroup A (default 'SET' )

- SET
Replace – Replace VGroup A's weights by VGroup B's ones.

- ADD
Add – Add VGroup B's weights to VGroup A's ones.

- SUB
Subtract – Subtract VGroup B's weights from VGroup A's ones.

- MUL
Multiply – Multiply VGroup A's weights by VGroup B's ones.

- DIV
Divide – Divide VGroup A's weights by VGroup B's ones.

- DIF
Difference – Difference between VGroup A's and VGroup B's weights.

- AVG
Average – Average value of VGroup A's and VGroup B's weights.

- MIN
Minimum – Minimum of VGroup A's and VGroup B's weights.

- MAX
Maximum – Maximum of VGroup A's and VGroup B's weights.

Type :

Literal['SET', 'ADD', 'SUB', 'MUL', 'DIV', 'DIF', 'AVG', 'MIN', 'MAX']
mix_set 

The set of vertices to act on (default 'AND' )

- ALL
All – Affect all vertices (might add some to VGroup A).

- A
VGroup A – Affect vertices in VGroup A.

- B
VGroup B – Affect vertices in VGroup B (might add some to VGroup A).

- OR
VGroup A or B – Affect vertices in at least one of both VGroups (might add some to VGroup A).

- AND
VGroup A and B – Affect vertices in both groups.

Type :

Literal['ALL', 'A', 'B', 'OR', 'AND']

[Related references](INDEX.md).
