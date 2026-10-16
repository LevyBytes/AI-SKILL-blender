# bpy.ops.object.lattice_add_to_selected

bpy.ops.object. lattice_add_to_selected ( * , fit_to_selected = True , radius = 1.0 , margin = 0.0 , add_modifiers = True , resolution_u = 2 , resolution_v = 2 , resolution_w = 2 , enter_editmode = False , align = 'WORLD' , location = (0.0, 0.0, 0.0) , rotation = (0.0, 0.0, 0.0) , scale = (0.0, 0.0, 0.0) ) 

Create a deformable lattice grid and apply it to shape selected geometry

Parameters :

- fit_to_selected ( bool ) – Fit to Selected, Extend lattice boundaries to encompass the selected deformable objects (optional)

- radius ( float ) – Radius, (in [0, inf], optional)

- margin ( float ) – Margin, Expand lattice size around geometry (in [0, inf], optional)

- add_modifiers ( bool ) – Add Modifiers, Automatically attach lattice deformation modifiers to selected objects (optional)

- resolution_u ( int ) – Resolution U, Lattice density along U direction (in [1, 64], optional)

- resolution_v ( int ) – V, Lattice density along V direction (in [1, 64], optional)

- resolution_w ( int ) – W, Lattice density along W direction (in [1, 64], optional)

- enter_editmode ( bool ) – Enter Edit Mode, Switch to edit mode immediately after creation (optional)

- align ( Literal [ 'WORLD' , 'VIEW' , 'CURSOR' ] ) – Align, Direction the inserted object will face (optional)

- WORLD
World – Orient the object to global axes.

- VIEW
View – Orient the object to match the camera view.

- CURSOR
3D Cursor – Use the 3D cursor's orientation for the object.

- location (mathutils.Vector) – Location, Placement point for the newly inserted object (array of 3 items, in [-inf, inf], optional)

- rotation (mathutils.Euler) – Rotation, Orientation to apply when inserting the object (array of 3 items, in [-inf, inf], optional)

- scale (mathutils.Vector) – Scale, Size scaling during insertion (array of 3 items, in [-inf, inf], optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
