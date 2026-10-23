# bpy.types.BlendDataMaterials: methods

class bpy.types. BlendDataMaterials ( bpy_prop_collection )

Collection of materials
## BlendDataMaterials(bpy_prop_collection)

Registry of polygon geometry objects.

base classes: bpy_prop, bpy_prop_collection
new ( name ) 

Create a material in the database

Parameters :

name ( str ) – New name for the data-block (never None)

Returns :

New material data-block

Return type :

Material
create_gpencil_data ( material ) 

Add hand-drawn tool properties to a material

Parameters :

material (Material) – Material (never None)
remove_gpencil_data ( material ) 

Delete hand-drawn tool properties from a material

Parameters :

material (Material) – Material (never None)
remove ( material , * , do_unlink = True , do_id_user = True , do_ui_user = True ) 

Erase a material from the current file

Parameters :

- material (Material) – Material to remove (never None)

- do_unlink ( bool ) – Break all references to this material before deletion (optional)

- do_id_user ( bool ) – Reduce user count for all data-blocks used (optional)

- do_ui_user ( bool ) – Ensure the interface is updated (optional)
tag ( value ) 

tag

Parameters :

value ( bool ) – Value
classmethod bl_rna_get_subclass ( id , default = None , / ) 

Parameters :

- id ( str ) – The RNA type identifier.

- default (bpy.types.Struct | None) – The value to return when not found.

Returns :

The RNA type or default when not found.

Return type :

bpy.types.Struct
classmethod bl_rna_get_subclass_py ( id , default = None , / ) 

Parameters :

- id ( str ) – The RNA type identifier.

- default ( type | None ) – The value to return when not found.

Returns :

The class or default when not found.

Return type :

type

[Related references](INDEX.md).
