# bpy.ops.object.align

bpy.ops.object. align ( * , bb_quality = True , align_mode = '`OPT_2`' , relative_to = '`OPT_4`' , align_axis = set() ) 

Position entities consistently

Parameters :

- bb_quality ( bool ) – High Quality, Enables high quality but slow calculation of the bounding box for perfect results on complex shape meshes with rotation/scale (optional)

- align_mode ( Literal [ '`OPT_1`' , '`OPT_2`' , '`OPT_3`' ] ) – Align Mode, Side of object to use for alignment (optional)

- relative_to ( Literal [ '`OPT_1`' , '`OPT_2`' , '`OPT_3`' , '`OPT_4`' ] ) – Relative To, Reference location to align to (optional)

- `OPT_1`
Scene Origin – Use the scene origin as the position for the selected objects to align to.

- `OPT_2`
3D Cursor – Use the 3D cursor as the position for the selected objects to align to.

- `OPT_3`
Selection – Use the selected objects as the position for the selected objects to align to.

- `OPT_4`
Active – Use the active object as the position for the selected objects to align to.

- align_axis ( set [ Literal [ 'X' , 'Y' , 'Z' ] ] ) – Align, Align to axis (optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

File :

startup/bl_operators/object_align.py:386

[Related references](INDEX.md).
