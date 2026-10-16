# bpy.ops.mesh.normals_tools

bpy.ops.mesh. normals_tools ( * , mode = 'COPY' , absolute = False )

Manipulate custom normals via Normal Vector from UI

Parameters :

- mode ( Literal [ 'COPY' , 'PASTE' , 'ADD' , 'MULTIPLY' , 'RESET' ] ) – Mode, Mode of tools taking input from interface (optional)

- COPY
Copy Normal – Copy normal to the internal clipboard.

- PASTE
Paste Normal – Paste normal from the internal clipboard.

- ADD
Add Normal – Add normal vector with selection.

- MULTIPLY
Multiply Normal – Multiply normal vector with selection.

- RESET
Reset Normal – Reset the internal clipboard and/or normal of selected element.

- absolute ( bool ) – Absolute Coordinates, Copy Absolute coordinates of Normal vector (optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
