# bpy.types.AssetShelf: methods

## AssetShelf(bpy_struct)

UI widget for quick asset browsing and picking.

base class: bpy_struct

subclasses —
`IMAGE_AST`_brush_paint, `NODE_AST`_compositor, `VIEW3D_AST`_brush_gpencil_paint, `VIEW3D_AST`_brush_gpencil_sculpt, `VIEW3D_AST`_brush_gpencil_vertex, `VIEW3D_AST`_brush_gpencil_weight, `VIEW3D_AST`_brush_sculpt, `VIEW3D_AST`_brush_sculpt_curves, `VIEW3D_AST`_brush_texture_paint, `VIEW3D_AST`_brush_vertex_paint, `VIEW3D_AST`_brush_weight_paint, `VIEW3D_AST`_pose_library
class bpy.types. AssetShelf ( bpy_struct )

Quick-access asset panel within an editor.
## See also

- [Bpy Struct](../data-types-bpy-struct/INDEX.md)
classmethod poll ( context )

If this method returns a non-null output, the asset shelf will be visible

Return type :

bool
classmethod asset_poll ( asset )

Determine if an asset should be visible in the asset shelf. If this method returns a non-null output, the asset will be visible.

Return type :

bool
classmethod get_active_asset ( )

Return a reference to the asset that should be highlighted as active in the asset shelf

Returns :

The weak reference to the asset to be highlighted as active, or None

Return type :

AssetWeakReference
classmethod draw_context_menu ( context , asset , layout )

Draw UI elements into the context menu UI layout displayed on right click
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
### Inherited Properties 

| Members | Members |
| --- | --- |
| bpy_struct.id_data | |
### Inherited Functions 

| Members | Members |
| --- | --- |
| bpy_struct.as_pointer bpy_struct.driver_add bpy_struct.driver_remove bpy_struct.get bpy_struct.id_properties_clear bpy_struct.id_properties_ensure bpy_struct.id_properties_ui bpy_struct.is_property_hidden bpy_struct.is_property_overridable_library bpy_struct.is_property_readonly bpy_struct.is_property_set bpy_struct.items | bpy_struct.keyframe_delete bpy_struct.keyframe_insert bpy_struct.keys bpy_struct.path_from_id bpy_struct.path_from_module bpy_struct.path_resolve bpy_struct.pop bpy_struct.property_overridable_library_set bpy_struct.property_unset bpy_struct.rna_ancestors bpy_struct.type_recast bpy_struct.values |

UI widget for quick asset browsing and picking — continued methods.

### Inherited Functions 

| Members | Members |
| --- | --- |
| bpy_struct.as_pointer bpy_struct.driver_add bpy_struct.driver_remove bpy_struct.get bpy_struct.id_properties_clear bpy_struct.id_properties_ensure bpy_struct.id_properties_ui bpy_struct.is_property_hidden bpy_struct.is_property_overridable_library bpy_struct.is_property_readonly bpy_struct.is_property_set bpy_struct.items | bpy_struct.keyframe_delete bpy_struct.keyframe_insert bpy_struct.keys bpy_struct.path_from_id bpy_struct.path_from_module bpy_struct.path_resolve bpy_struct.pop bpy_struct.property_overridable_library_set bpy_struct.property_unset bpy_struct.rna_ancestors bpy_struct.type_recast bpy_struct.values |

[Related references](INDEX.md).
