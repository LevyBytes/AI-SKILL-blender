# bpy.types.USDHook: Context Classes

### Context Classes

The callbacks receive instances of the built-in classes listed below as their arguments.


#### USDSceneExportContext

Argument for on_export.

Methods:

- get_stage() : returns the USD stage to be saved

- get_depsgraph() : returns the Blender scene dependency graph

- get_prim_map() returns a dict where the key is an exported USD Prim path and the value a list
of the IDs associated with that prim.


#### USDMaterialExportContext

Argument for on_material_export.

Methods:

- get_stage() : returns the USD stage to be saved

- export_texture(image: bpy.types.Image) : Returns the USD asset path for the given texture image

Depending on the active USD export options, export_texture writes out in-memory images and may also duplicate texture assets. By default, for instance, a call to export_texture(/foo/bar.png) copies the file into a textures directory beside the exported USD and hands back the relative path ./textures/bar.png .


#### USDSceneImportContext

Argument for on_import.

Methods:

- get_prim_map() returns a dict where the key is an imported USD Prim path and the value a list
of the IDs created by the imported prim.

- get_stage() returns the USD stage which was imported.


#### USDMaterialImportContext

Argument for material_import_poll and on_material_import.

Methods:

- get_stage() :
returns the USD stage to be saved.

- import_texture(asset_path: str) :
for the given USD texture asset path, returns a tuple[str, bool] ,
containing the asset’s local path and a bool indicating whether the path references a temporary file.

Depending on the current USD Import Textures options, import_texture may pull the texture onto the local file system when the supplied asset path is a package-relative path inside a USDZ archive. With the Import Textures mode set to Packed , the texture lands in a temporary spot and the returned tuple’s second element is True to flag the file as temporary, which may mean you need to pack the image. If the asset path already points at a local file, or if no local copy could be made, the original path comes back unchanged.

[Related references](INDEX.md).
