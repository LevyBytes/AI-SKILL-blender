# bpy.types.GreasePencilLayer: methods

## GreasePencilLayer(GreasePencilTreeNode)

### GreasePencilLayer(GreasePencilTreeNode)

base classes — bpy_struct, GreasePencilTreeNode
class bpy.types. GreasePencilLayer ( GreasePencilTreeNode )

Collection of related drawings
get_frame_at ( frame_number )

Get the frame at given frame number

Parameters :

frame_number ( int ) – Frame Number, (in [-1048574, 1048574])

Returns :

Frame

Return type :

GreasePencilFrame
current_frame ( )

The Grease Pencil frame at the current scene time on this layer

Return type :

GreasePencilFrame
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
| bpy_struct.id_data GreasePencilTreeNode.name GreasePencilTreeNode.hide GreasePencilTreeNode.lock GreasePencilTreeNode.select GreasePencilTreeNode.use_onion_skinning | GreasePencilTreeNode.use_masks GreasePencilTreeNode.channel_color GreasePencilTreeNode.next_node GreasePencilTreeNode.prev_node GreasePencilTreeNode.parent_group |
### Inherited Functions

| Members | Members |
| --- | --- |
| bpy_struct.as_pointer bpy_struct.driver_add bpy_struct.driver_remove bpy_struct.get bpy_struct.id_properties_clear bpy_struct.id_properties_ensure bpy_struct.id_properties_ui bpy_struct.is_property_hidden bpy_struct.is_property_overridable_library bpy_struct.is_property_readonly bpy_struct.is_property_set bpy_struct.items bpy_struct.keyframe_delete | bpy_struct.keyframe_insert bpy_struct.keys bpy_struct.path_from_id bpy_struct.path_from_module bpy_struct.path_resolve bpy_struct.pop bpy_struct.property_overridable_library_set bpy_struct.property_unset bpy_struct.rna_ancestors bpy_struct.type_recast bpy_struct.values GreasePencilTreeNode.bl_rna_get_subclass GreasePencilTreeNode.bl_rna_get_subclass_py |
### References

| Description | Description |
| --- | --- |
| GreasePencil.layers GreasePencilv3Layers.active GreasePencilv3Layers.move GreasePencilv3Layers.move_bottom | GreasePencilv3Layers.move_to_layer_group GreasePencilv3Layers.move_top GreasePencilv3Layers.new GreasePencilv3Layers.remove |

[Related references](INDEX.md).
