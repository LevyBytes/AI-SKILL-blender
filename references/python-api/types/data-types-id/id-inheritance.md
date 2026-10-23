# bpy.types.ID: inheritance

## ID(bpy_struct)

### ID(bpy_struct)

base class: bpy_struct

subclasses —
Action, Annotation, Armature, Brush, CacheFile, Camera, Collection, Curve, Curves, FreestyleLineStyle, GreasePencil, Image, Key, Lattice, Library, Light, LightProbe, Mask, Material, Mesh, MetaBall, MovieClip, NodeTree, Object, PaintCurve, Palette, ParticleSettings, PointCloud, Scene, Screen, Sound, Speaker, Text, Texture, VectorFont, Volume, WindowManager, WorkSpace, World
class bpy.types. ID ( bpy_struct )

The shared base for data-blocks: gives each a unique name, cross-library linking, and reference counting.
### Inherited Properties

| Members | Members |
| --- | --- |
| bpy_struct.id_data | |
### Inherited Functions

| Members | Members |
| --- | --- |
| bpy_struct.as_pointer bpy_struct.driver_add bpy_struct.driver_remove bpy_struct.get bpy_struct.id_properties_clear bpy_struct.id_properties_ensure bpy_struct.id_properties_ui bpy_struct.is_property_hidden bpy_struct.is_property_overridable_library bpy_struct.is_property_readonly bpy_struct.is_property_set bpy_struct.items | bpy_struct.keyframe_delete bpy_struct.keyframe_insert bpy_struct.keys bpy_struct.path_from_id bpy_struct.path_from_module bpy_struct.path_resolve bpy_struct.pop bpy_struct.property_overridable_library_set bpy_struct.property_unset bpy_struct.rna_ancestors bpy_struct.type_recast bpy_struct.values |
### References

| Members | Members |
| --- | --- |
| bpy.context.annotation_data_owner bpy.context.id bpy.context.selected_ids bpy.context.texture_user Action.fcurve_ensure_for_datablock ActionSlot.users AssetRepresentation.local_id BlendData.pack_linked_ids_hierarchy BlendData.pack_linked_ids_hierarchy BlendDataObjects.new BlendImportContextItem.id BlendImportContextItem.library_override_id BlendImportContextItem.reusable_local_id Depsgraph.id_eval_get Depsgraph.id_eval_get Depsgraph.ids DepsgraphUpdate.id DopeSheet.source DriverTarget.id ID.copy ID.evaluated_get ID.make_local ID.original ID.override_create ID.override_hierarchy_create ID.override_hierarchy_create | ID.user_of_id ID.user_remap IDOverrideLibrary.hierarchy_root IDOverrideLibrary.reference IDOverrideLibraryPropertyOperation.subitem_local_id IDOverrideLibraryPropertyOperation.subitem_reference_id IDOverrideLibraryPropertyOperations.add IDOverrideLibraryPropertyOperations.add IDViewerPathElem.id Key.user KeyingSetPath.id KeyingSetPaths.add MaskParent.id NodeTree.get_from_context NodeTree.get_from_context NodesModifierDataBlock.id Object.data PropertyGroupItem.id SpaceFileBrowser.activate_asset_by_id SpaceNodeEditor.id SpaceNodeEditor.id_from SpaceProperties.pin_id UILayout.template_action UILayout.template_path_builder UILayout.template_preview UILayout.template_preview |

[Related references](INDEX.md).
