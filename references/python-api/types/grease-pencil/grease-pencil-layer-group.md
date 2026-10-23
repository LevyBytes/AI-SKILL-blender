# bpy.types.GreasePencilLayerGroup

children

Layer groups directly nested under this one, in stack order so the first entry sits at the bottom of the tree. (default None, readonly)

Type :

bpy_prop_collection[GreasePencilTreeNode]
color_tag

(default 'COLOR1' )

Type :

Literal[‘NONE’, ‘COLOR1’, ‘COLOR2’, ‘COLOR3’, ‘COLOR4’, ‘COLOR5’, ‘COLOR6’, ‘COLOR7’, ‘COLOR8’]
is_expanded

The layer group shows expanded in the UI (default False)

Type :

bool
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
| GreasePencil.layer_groups GreasePencilTreeNode.parent_group GreasePencilv3LayerGroup.active GreasePencilv3LayerGroup.move GreasePencilv3LayerGroup.move_bottom GreasePencilv3LayerGroup.move_to_layer_group GreasePencilv3LayerGroup.move_to_layer_group | GreasePencilv3LayerGroup.move_top GreasePencilv3LayerGroup.new GreasePencilv3LayerGroup.new GreasePencilv3LayerGroup.remove GreasePencilv3Layers.move_to_layer_group GreasePencilv3Layers.new |
## GreasePencilLayerGroup(GreasePencilTreeNode)

### GreasePencilLayerGroup(GreasePencilTreeNode)

base classes: bpy_struct, GreasePencilTreeNode
class bpy.types. GreasePencilLayerGroup ( GreasePencilTreeNode )

Group of Grease Pencil layers

[Related references](INDEX.md).
