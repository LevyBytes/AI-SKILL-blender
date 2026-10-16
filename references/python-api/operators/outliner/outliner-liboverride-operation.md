# bpy.ops.outliner.liboverride_operation

bpy.ops.outliner. liboverride_operation ( * , type = '`OVERRIDE_LIBRARY_CREATE_HIERARCHY`' , selection_set = 'SELECTED' ) 

Establish, restart or drop vault modification pathways

Parameters :

- type ( Literal [ '`OVERRIDE_LIBRARY_CREATE_HIERARCHY`' , '`OVERRIDE_LIBRARY_RESET`' , '`OVERRIDE_LIBRARY_CLEAR_SINGLE`' ] ) – Library Override Operation, (optional)

- `OVERRIDE_LIBRARY_CREATE_HIERARCHY`
Make – Establish a household alteration of the chosen transmitted information-blocks, and their progression of connections.

- `OVERRIDE_LIBRARY_RESET`
Reset – Restore the chosen household adjustments to their transmitted references quantities.

- `OVERRIDE_LIBRARY_CLEAR_SINGLE`
Clear – Erase the chosen household adjustments and relink their employments to the transmitted information-blocks when feasible, or else restart them and indicate them as non alterable.

- selection_set ( Literal [ 'SELECTED' , 'CONTENT' , '`SELECTED_AND_CONTENT`' ] ) – Selection Set, Throughout which portion of the arrangement pieces to implement the operation (optional)

- SELECTED
Selected – Execute the operation throughout chosen information-blocks merely.

- CONTENT
Content – Execute the operation throughout substance of the chosen pieces merely (the information-blocks in their sub-pathway).

- `SELECTED_AND_CONTENT`
Selected & Content – Execute the operation throughout chosen information-blocks and every their connections.

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
