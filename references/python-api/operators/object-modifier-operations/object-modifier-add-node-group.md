# bpy.ops.object.modifier_add_node_group

bpy.ops.object. modifier_add_node_group ( * , asset_library_type = 'LOCAL' , asset_library_identifier = '' , relative_asset_identifier = '' , session_uid = 0 , use_selected_objects = False ) 

Attach a deformation/effect modifier to the current object

Parameters :

- asset_library_type (Literal[Asset Library Type Items]) – Asset Library Type, (optional)

- asset_library_identifier ( str ) – Asset Library Identifier, (optional, never None)

- relative_asset_identifier ( str ) – Relative Asset Identifier, (optional, never None)

- session_uid ( int ) – Session UID, Session UID of the data-block to use by the operator (in [-inf, inf], optional)

- use_selected_objects ( bool ) – Selected Objects, Affect all selected objects instead of just the active object (optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
