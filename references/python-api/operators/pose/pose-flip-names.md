# bpy.ops.pose.flip_names

bpy.ops.pose. flip_names ( * , do_strip_numbers = False ) 

Corrects and reverses the axis tags in the names of selected bones

Parameters :

do_strip_numbers ( bool ) – Strip Numbers, Try to remove right-most dot-number from flipped names.Warning: May result in incoherent naming in some cases(optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]
bpy.ops.pose. flip_names ( * , do_strip_numbers = False )
Flips (and corrects) the axis suffixes in the names of the selected bones.
Parameters: do_strip_numbers ( bool ) – Strip Numbers, Try to remove right-most dot-number from flipped names. Warning: May result in incoherent naming in some cases (optional)
Returns: The operator's result.
Return type: set[Literal[Operator Return Items]]

[Related references](INDEX.md).
