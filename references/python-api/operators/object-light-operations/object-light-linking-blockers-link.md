# bpy.ops.object.light_linking_blockers_link

bpy.ops.object. light_linking_blockers_link ( * , link_state = 'INCLUDE' ) 

Tie the chosen shadow-blocking objects to the current light emitter

Parameters :

link_state ( Literal [ 'INCLUDE' , 'EXCLUDE' ] ) – Link State, Shadow connection mode (optional)

- INCLUDE
Include – Add selected blockers to shadow-casting from the active emitter.

- EXCLUDE
Exclude – Prevent selected blockers from shadow-casting from the active emitter.

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
