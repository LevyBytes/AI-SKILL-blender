# bpy.types.UIList: overview

base class: bpy_struct

subclasses —
`ASSETBROWSER_UL`_metadata_tags, `CLIP_UL`_tracking_objects, `CURVES_UL`_attributes, `DATA_UL`_bone_collections, `FILEBROWSER_UL`_dir, `GPENCIL_UL`_annotation_layer, `GPENCIL_UL`_matslots, `GREASE_PENCIL_UL`_attributes, `GREASE_PENCIL_UL`_masks, `IMAGE_UL`_render_slots, `IMAGE_UL`_udim_tiles, `MASK_UL`_layers, `MATERIAL_UL`_matslots, `MESH_UL`_attributes, `MESH_UL`_color_attributes, `MESH_UL`_color_attributes_selector, `MESH_UL`_uvmaps, `MESH_UL`_vgroups, `PARTICLE_UL`_particle_systems, `PHYSICS_UL`_dynapaint_surfaces, `POINTCLOUD_UL`_attributes, `POSE_UL`_selection_set, `RENDER_UL`_renderviews, `SCENE_UL`_gltf2_filter_action, `SCENE_UL`_keying_set_paths, `TEXTURE_UL`_texpaintslots, `TEXTURE_UL`_texslots, `UI_UL`_list, `USERPREF_UL`_asset_libraries, `USERPREF_UL`_extension_repos, `VIEWLAYER_UL`_aov, `VIEWLAYER_UL`_linesets, `VOLUME_UL`_grids, `WORKSPACE_UL`_addons_items
class bpy.types. UIList ( bpy_struct )

UI list containing the elements of a collection
### UIList(bpy_struct)
### Basic UIList Example

Below is the UIList subclass that drives the material-slots list, annotated heavily so each step is clear.

Pay attention to how the class is named — the convention mirrors the one used for panels and menus.

Note

A UIList subclass has to be registered before Blender will make use of it.

The complete program is in the [upstream source](https://docs.blender.org/api/5.1/bpy.types.UIList.html#basic-uilist-example).
### Advanced UIList Example - Filtering and Reordering

This longer version of the vertex-groups UIList subclass is shown for illustration only — walking every vertex inside a ‘draw’ callback would wreck UI performance, so you would not ship it as-is. Even so, it demonstrates nicely how filtering and reordering callbacks fit together.

[Open the complete example modules](../../examples/vertex-group-list/INDEX.md).

[Related references](INDEX.md).
