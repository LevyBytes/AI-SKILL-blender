# bpy.ops.paint.weight_from_bones

bpy.ops.paint. weight_from_bones ( * , type = 'AUTOMATIC' ) 

Distribute weights across vertex groups based on the armature's active bones, using bone-to-vertex proximity

Parameters :

type ( Literal [ 'AUTOMATIC' , 'ENVELOPES' ] ) – Type, Method to use for assigning weights (optional)

- AUTOMATIC
Automatic – Calculates weights from bones automatically.

- ENVELOPES
From Envelopes – Uses bone envelopes with adjustable radius for weight assignment.

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
