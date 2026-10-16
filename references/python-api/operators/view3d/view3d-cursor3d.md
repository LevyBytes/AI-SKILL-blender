# bpy.ops.view3d.cursor3d

bpy.ops.view3d. cursor3d ( * , use_depth = True , orientation = 'VIEW' ) 

Positions the 3D cursor

Parameters :

- use_depth ( bool ) – Surface Project, Project onto the surface (optional)

- orientation ( Literal [ 'NONE' , 'VIEW' , 'XFORM' , 'GEOM' ] ) – Orientation, Preset viewpoint to use (optional)

- NONE
None – Keep the orientation as it is.

- VIEW
View – Match the viewport orientation.

- XFORM
Transform – Match the active transform setting.

- GEOM
Geometry – Follow the surface normal.

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
