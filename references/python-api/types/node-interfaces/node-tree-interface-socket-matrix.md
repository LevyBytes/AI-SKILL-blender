# bpy.types.NodeTreeInterfaceSocketMatrix

draw ( context , layout )

Render the settings shown for this interface socket

Parameters :

- context (Context) – (never None)

- layout (UILayout) – Layout, the layout placed in the UI (never None)
init_socket ( node , socket , data_path )

Set up a fresh node socket instance

Parameters :

- node (Node) – Node, the node owning the socket being set up (never None)

- socket (NodeSocket) – Socket, the socket being set up (never None)

- data_path ( str ) – Data Path, route to this socket's specialized data (never None)
from_socket ( node , socket )

Fill in template parameters by copying an existing socket

Parameters :

- node (Node) – Node, the node owning the source socket (never None)

- socket (NodeSocket) – Socket, the source socket (never None)
classmethod bl_rna_get_subclass ( id , default = None , / )

Parameters :

- id ( str ) – The RNA type identifier.

- default (bpy.types.Struct | None) – The value to return when not found.

Returns :

Either the matching RNA type or the supplied default if none is found.

Return type :

bpy.types.Struct
classmethod bl_rna_get_subclass_py ( id , default = None , / )

Parameters :

- id ( str ) – The RNA type identifier.

- default ( type | None ) – The value to return when not found.

Returns :

Either the matching class or the supplied default if none is found.

Return type :

type
### Inherited Properties

| Members | Members |
| --- | --- |
| bpy_struct.id_data NodeTreeInterfaceItem.item_type NodeTreeInterfaceItem.parent NodeTreeInterfaceItem.position NodeTreeInterfaceItem.index NodeTreeInterfaceSocket.name NodeTreeInterfaceSocket.identifier NodeTreeInterfaceSocket.description NodeTreeInterfaceSocket.socket_type NodeTreeInterfaceSocket.in_out NodeTreeInterfaceSocket.hide_value NodeTreeInterfaceSocket.hide_in_modifier | NodeTreeInterfaceSocket.force_non_field NodeTreeInterfaceSocket.is_inspect_output NodeTreeInterfaceSocket.is_panel_toggle NodeTreeInterfaceSocket.layer_selection_field NodeTreeInterfaceSocket.menu_expanded NodeTreeInterfaceSocket.optional_label NodeTreeInterfaceSocket.select NodeTreeInterfaceSocket.attribute_domain NodeTreeInterfaceSocket.default_attribute_name NodeTreeInterfaceSocket.structure_type NodeTreeInterfaceSocket.default_input NodeTreeInterfaceSocket.bl_socket_idname |
### Inherited Functions

| Members | Members |
| --- | --- |
| bpy_struct.as_pointer bpy_struct.driver_add bpy_struct.driver_remove bpy_struct.get bpy_struct.id_properties_clear bpy_struct.id_properties_ensure bpy_struct.id_properties_ui bpy_struct.is_property_hidden bpy_struct.is_property_overridable_library bpy_struct.is_property_readonly bpy_struct.is_property_set bpy_struct.items bpy_struct.keyframe_delete bpy_struct.keyframe_insert bpy_struct.keys bpy_struct.path_from_id | bpy_struct.path_from_module bpy_struct.path_resolve bpy_struct.pop bpy_struct.property_overridable_library_set bpy_struct.property_unset bpy_struct.rna_ancestors bpy_struct.type_recast bpy_struct.values NodeTreeInterfaceItem.bl_rna_get_subclass NodeTreeInterfaceItem.bl_rna_get_subclass_py NodeTreeInterfaceSocket.bl_system_properties_get NodeTreeInterfaceSocket.draw NodeTreeInterfaceSocket.init_socket NodeTreeInterfaceSocket.from_socket NodeTreeInterfaceSocket.bl_rna_get_subclass NodeTreeInterfaceSocket.bl_rna_get_subclass_py |
## NodeTreeInterfaceSocketMatrix(NodeTreeInterfaceSocket)

### NodeTreeInterfaceSocketMatrix(NodeTreeInterfaceSocket)

base classes — bpy_struct, NodeTreeInterfaceItem, NodeTreeInterfaceSocket
class bpy.types. NodeTreeInterfaceSocketMatrix ( NodeTreeInterfaceSocket )

A node socket that carries a matrix value

[Related references](INDEX.md).
