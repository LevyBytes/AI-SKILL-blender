# bpy.ops.curves.snap_curves_to_surface

**bpy.ops.curves.snap_curves_to_surface**( * , attach_mode = 'NEAREST' )

Position curves so their starting points rest on a surface mesh.

Parameters:
- attach_mode ( Literal [ 'NEAREST' , 'DEFORM' ] ) – Attach Mode, How to find the point on the surface to attach to (optional)

- NEAREST
Nearest – Find the closest point on the surface for the root point of every curve and move the root there.

- DEFORM
Deform – Re-attach curves to a deformed surface using the existing attachment information. This only works when the topology of the surface mesh has not changed.

Returns: Result of the operator call.
Return type: set[Literal[Operator Return Items]]

[Related references](INDEX.md).
