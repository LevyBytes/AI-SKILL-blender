# bpy.ops.mesh.sort_elements

bpy.ops.mesh. sort_elements ( * , type = '`VIEW_ZAXIS`' , elements = {'VERT'} , reverse = False , seed = 0 ) 

Rearrange chosen elements, based on a given technique

Parameters :

- type ( Literal [ '`VIEW_ZAXIS`' , '`VIEW_XAXIS`' , '`CURSOR_DISTANCE`' , 'MATERIAL' , 'SELECTED' , 'RANDOMIZE' , 'REVERSE' ] ) – Type, Which sorting to perform (optional)

- `VIEW_ZAXIS`
View Z Axis – Arrange by depth in the viewport, farthest ahead.

- `VIEW_XAXIS`
View X Axis – Arrange horizontally in the viewport.

- `CURSOR_DISTANCE`
Cursor Distance – Arrange by space to the 3D pointer.

- MATERIAL
Material – Arrange face regions by slot index, smallest ahead.

- SELECTED
Selected – Put marked components first, keeping their sequence.
Warning: This affects unmarked parts' positions too.

- RANDOMIZE
Randomize – Rearrange in random sequence.

- REVERSE
Reverse – Flip the current sequence.

- elements ( set [ Literal [ 'VERT' , 'EDGE' , 'FACE' ] ] ) – Elements, What to rearrange (points, edges and/or regions) (optional)

- reverse ( bool ) – Reverse, Reverse the sorting effect (optional)

- seed ( int ) – Seed, Seed for random-based work (in [0, inf], optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
