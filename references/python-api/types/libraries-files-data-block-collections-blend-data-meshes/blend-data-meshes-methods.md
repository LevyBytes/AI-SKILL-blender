# bpy.types.BlendDataMeshes: methods

## BlendDataMeshes(bpy_prop_collection)

Registry of implicit surface blob objects.

base classes — bpy_prop, bpy_prop_collection
class bpy.types. BlendDataMeshes ( bpy_prop_collection )

Collection of meshes
new ( name ) 

Create a mesh in the database

Parameters :

name ( str ) – New name for the data-block (never None)

Returns :

New mesh data-block

Return type :

Mesh
new_from_object ( object , * , preserve_all_data_layers = False , depsgraph = None ) 

Add a mesh derived from a scene element (returns unevaluated geometry from original, or final evaluated geometry with all modifications applied to evaluated variant)

Parameters :

- object (Object) – Object to create mesh from (never None)

- preserve_all_data_layers ( bool ) – Preserve all data layers in the mesh, like UV maps and vertex groups. By default Blender only computes the subset of data layers needed for viewport display and rendering, for better performance. (optional)

- depsgraph (Depsgraph) – Dependency Graph, Evaluated dependency graph which is required when preserve_all_data_layers is true (optional)

Returns :

Mesh created from object, remove it if it is only used for export

Return type :

Mesh
remove ( mesh , * , do_unlink = True , do_id_user = True , do_ui_user = True ) 

Unload a mesh from the current file

Parameters :

- mesh (Mesh) – Mesh to remove (never None)

- do_unlink ( bool ) – Break all references to this mesh before deletion (WARNING: will also delete objects instancing that mesh data) (optional)

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
