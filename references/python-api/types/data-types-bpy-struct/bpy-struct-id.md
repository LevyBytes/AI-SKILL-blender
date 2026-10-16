# bpy.types.bpy_struct: id_properties_clear, id_properties_ensure, id_properties_ui

id_properties_clear ( )

Drops the parent group holding an RNA struct's custom IDProperties.
id_properties_ensure ( )

Returns :

the parent group for an RNA struct's custom IDProperties.

Return type :

idprop.types.IDPropertyGroup
id_properties_ui ( key , / )

Parameters :

key ( str ) – String name of the property.

Returns :

An object used to manage an IDProperty's UI data.

Return type :

bpy.types.IDPropertyUIManager

[Related references](INDEX.md).
