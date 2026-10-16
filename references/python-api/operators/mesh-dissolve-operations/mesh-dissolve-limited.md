# bpy.ops.mesh.dissolve_limited

bpy.ops.mesh. dissolve_limited ( * , angle_limit = 0.0872665 , use_dissolve_boundaries = False , delimit = {'NORMAL'} )

Demolish chosen edges and vertices constrained by surrounding geometry angles

Parameters :

- angle_limit ( float ) – Max Angle, Angle limit (in [0, 3.14159], optional)

- use_dissolve_boundaries ( bool ) – All Boundaries, Dissolve all vertices in between face boundaries (optional)

- delimit (set[Literal[Mesh Delimit Mode Items]]) – Delimit, Delimit dissolve operation (optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
