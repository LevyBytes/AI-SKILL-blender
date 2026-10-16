# bpy.ops.pose.select_grouped

bpy.ops.pose. select_grouped ( * , extend = False , type = 'COLLECTION' ) 

Highlight all visible bones organized by matching properties

Parameters :

- extend ( bool ) – Extend, Extend selection instead of deselecting everything first (optional)

- type ( Literal [ 'COLLECTION' , 'COLOR' , 'KEYINGSET' , 'CHILDREN' , '`CHILDREN_IMMEDIATE`' , 'PARENT' , 'SIBLINGS' ] ) – Type, (optional)

- COLLECTION
Collection – Same collections as the active bone.

- COLOR
Color – Same color as the active bone.

- KEYINGSET
Keying Set – All bones affected by active Keying Set.

- CHILDREN
Children – Select all children of currently selected bones.

- `CHILDREN_IMMEDIATE`
Immediate Children – Select direct children of currently selected bones.

- PARENT
Parents – Select the parents of currently selected bones.

- SIBLINGS
Siblings – Select all bones that have the same parent as currently selected bones.

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]
bpy.ops.pose. select_grouped ( * , extend = False , type = 'COLLECTION' )
Selects all visible bones grouped by similar properties.
Parameters:
- extend ( bool ) – Extend, Extend selection instead of deselecting everything first (optional)
- type ( Literal [ 'COLLECTION' , 'COLOR' , 'KEYINGSET' , 'CHILDREN' , '`CHILDREN_IMMEDIATE`' , 'PARENT' , 'SIBLINGS' ] ) – Type, (optional)
- COLLECTION — Collection: same collections as the active bone.
- COLOR — Color: same color as the active bone.
- KEYINGSET — Keying Set: all bones affected by the active Keying Set.
- CHILDREN — Children: select all children of the currently selected bones.
- `CHILDREN_IMMEDIATE` — Immediate Children: select direct children of the currently selected bones.
- PARENT — Parents: select the parents of the currently selected bones.
- SIBLINGS — Siblings: select all bones that have the same parent as the currently selected bones.
Returns: The operator's result.
Return type: set[Literal[Operator Return Items]]

[Related references](INDEX.md).
