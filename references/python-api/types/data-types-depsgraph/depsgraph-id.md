# bpy.types.Depsgraph: id_eval_get, id_type_updated

id_eval_get ( id )

id_eval_get

Parameters :

id (ID) – Original ID to get evaluated complementary part for

Returns :

Evaluated ID for the given original one

Return type :

ID
id_type_updated ( id_type )

id_type_updated

Parameters :

id_type (Literal[Id Type Items]) – ID Type

Returns :

Updated, True if any data-block with this type was added, updated or removed

Return type :

bool

[Related references](INDEX.md).
