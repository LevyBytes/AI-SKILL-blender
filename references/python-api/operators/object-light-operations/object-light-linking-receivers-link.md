# bpy.ops.object.light_linking_receivers_link

bpy.ops.object. light_linking_receivers_link ( * , link_state = 'INCLUDE' ) 

Tie the chosen illuminated objects to the current light emitter

Parameters :

link_state ( Literal [ 'INCLUDE' , 'EXCLUDE' ] ) – Link State, Light connection mode (optional)
- INCLUDE
Include – Add selected receivers to light-receiving from the active emitter.

- EXCLUDE
Exclude – Prevent selected receivers from light-receiving from the active emitter.

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
