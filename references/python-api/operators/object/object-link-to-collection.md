# bpy.ops.object.link_to_collection

bpy.ops.object. link_to_collection ( * , collection_uid = -1 , is_new = False , new_collection_name = '' ) 

Attach objects to a grouping container

Parameters :

- collection_uid ( int ) – Collection UID, Session UID of the collection to link to (in [-1, inf], optional)

- is_new ( bool ) – New, Attach objects to a newly created collection (optional)

- new_collection_name ( str ) – Name, Title for the freshly added collection (optional, never None)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
