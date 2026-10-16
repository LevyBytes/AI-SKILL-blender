# bpy.ops.outliner.liboverride_troubleshoot_operation

bpy.ops.outliner. liboverride_troubleshoot_operation ( * , type = '`OVERRIDE_LIBRARY_RESYNC_HIERARCHY`' , selection_set = 'SELECTED' )

Sophisticated operations throughout vault modification to facilitate fix harmed pathways

Parameters :

- type ( Literal [ '`OVERRIDE_LIBRARY_RESYNC_HIERARCHY`' , '`OVERRIDE_LIBRARY_RESYNC_HIERARCHY_ENFORCE`' , '`OVERRIDE_LIBRARY_DELETE_HIERARCHY`' ] ) – Library Override Troubleshoot Operation, (optional)

- `OVERRIDE_LIBRARY_RESYNC_HIERARCHY`
Resync – Rebuild the chosen household adjustments from their transmitted references, with their progressions of connections.

- `OVERRIDE_LIBRARY_RESYNC_HIERARCHY_ENFORCE`
Resync Enforce – Rebuild the chosen household adjustments from their transmitted references, with their progressions of connections, compelling these progressions to correspond to the transmitted information (specifically overlooking persisting adjustments on information-block indicator attributes).

- `OVERRIDE_LIBRARY_DELETE_HIERARCHY`
Delete – Erase the chosen household adjustments (plus their progressions of modification connections) and relink their employments to the transmitted information-blocks.

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
