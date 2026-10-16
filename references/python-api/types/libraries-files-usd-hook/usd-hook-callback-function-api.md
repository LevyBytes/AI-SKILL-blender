# bpy.types.USDHook: Callback Function API

### Callback Function API

Inside a USDHook subclass you can define as many or as few of the callback functions below as you need.


#### on_export

Runs just ahead of the USD export wrapping up, giving you a chance to tweak the USD stage right before it gets written out.

Args:

- export_context (USDSceneExportContext): Provides access to the stage and dependency graph

Returns:

- True on success or False if the operation was bypassed or otherwise failed to complete


#### on_material_export

Runs once per exported material, giving you a chance to alter the USD material — for example to build shaders.

Args:

- export_context (USDMaterialExportContext): Provides access to the stage and a texture export utility function

- bl_material ( bpy.types.Material ): The source Blender material

- usd_material ( pxr.UsdShade.Material ): The target USD material to be exported

Returns:

- True on success or False if the operation was bypassed or otherwise failed to complete

Keep in mind that the destination USD material may already carry shaders wired up by the USD exporter itself or by other material-export hooks.


#### on_import

Runs once the USD import has wrapped up.

Args:

- import_context (USDSceneImportContext):
Provides access to the stage and a map associating USD prim paths and Blender IDs

Returns:

- True on success or False if the operation was bypassed or otherwise failed to complete


#### material_import_poll

Runs to decide whether this USDHook implementation is able to convert a particular USD material.

Args:

- import_context (USDMaterialImportContext): Provides access to the stage and a texture import utility function

- usd_material ( pxr.UsdShade.Material ): The source USD material to be exported

Returns:

- True if the hook can convert the material or False otherwise

Should any hook answer True to material_import_poll , the USD importer bypasses its built-in USD Preview Surface and MaterialX handling and instead calls that hook’s on_material_import method to do the conversion.

#### on_material_import

Runs once per imported material so you can turn the USD material into nodes on the Blender material. For this to be invoked, the hook also has to supply a material_import_poll() callback that answers True for the material in question.

Args:

- import_context (USDMaterialImportContext): Provides access to the stage and a texture import utility function

- bl_material ( bpy.types.Material ): The target Blender material with an empty node tree

- usd_material ( pxr.UsdShade.Material ): The source USD material to be imported

Returns:

- True on success or False if the conversion failed or otherwise did not complete

[Related references](INDEX.md).
