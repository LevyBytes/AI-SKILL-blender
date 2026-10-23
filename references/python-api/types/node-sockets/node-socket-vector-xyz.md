# bpy.types.NodeSocketVectorXYZ

default_value 

(array of 3 items, in [-inf, inf], default (0.0, 0.0, 0.0))

Type :

mathutils.Vector
links 

Every node link attached to this socket, whether incoming or outgoing.

Type :

NodeLinks

Note

Takes O(len(nodetree.links)) time.

(readonly)
classmethod bl_rna_get_subclass ( id , default = None , / ) 

Parameters :

- id ( str ) – Identifier naming the RNA type.

- default (bpy.types.Struct | None) – Fallback returned if no match is found.

Returns :

Either the matching RNA type or the supplied fallback when nothing matches.

Return type :

bpy.types.Struct
classmethod bl_rna_get_subclass_py ( id , default = None , / ) 

Parameters :

- id ( str ) – Identifier naming the RNA type.

- default ( type | None ) – Fallback returned if no match is found.

Returns :

Either the matching class or the supplied fallback when nothing matches.

Return type :

type
### Inherited Properties 

| Members | Members |
| --- | --- |
| bpy_struct.id_data NodeSocket.name NodeSocket.label NodeSocket.identifier NodeSocket.description NodeSocket.is_output NodeSocket.select NodeSocket.hide NodeSocket.enabled NodeSocket.link_limit NodeSocket.is_linked NodeSocket.is_unavailable NodeSocket.is_multi_input NodeSocket.show_expanded | NodeSocket.is_inactive NodeSocket.is_icon_visible NodeSocket.hide_value NodeSocket.pin_gizmo NodeSocket.node NodeSocket.type NodeSocket.display_shape NodeSocket.inferred_structure_type NodeSocket.bl_idname NodeSocket.bl_label NodeSocket.bl_subtype_label NodeSocket.links NodeSocketStandard.links |
### Inherited Functions 

| Members | Members |
| --- | --- |
| bpy_struct.as_pointer bpy_struct.driver_add bpy_struct.driver_remove bpy_struct.get bpy_struct.id_properties_clear bpy_struct.id_properties_ensure bpy_struct.id_properties_ui bpy_struct.is_property_hidden bpy_struct.is_property_overridable_library bpy_struct.is_property_readonly bpy_struct.is_property_set bpy_struct.items bpy_struct.keyframe_delete bpy_struct.keyframe_insert bpy_struct.keys bpy_struct.path_from_id bpy_struct.path_from_module bpy_struct.path_resolve | bpy_struct.pop bpy_struct.property_overridable_library_set bpy_struct.property_unset bpy_struct.rna_ancestors bpy_struct.type_recast bpy_struct.values NodeSocket.bl_system_properties_get NodeSocket.draw NodeSocket.draw_color NodeSocket.draw_color_simple NodeSocket.bl_rna_get_subclass NodeSocket.bl_rna_get_subclass_py NodeSocketStandard.draw NodeSocketStandard.draw_color NodeSocketStandard.draw_color_simple NodeSocketStandard.bl_rna_get_subclass NodeSocketStandard.bl_rna_get_subclass_py |
## NodeSocketVectorXYZ(NodeSocketStandard)

### NodeSocketVectorXYZ(NodeSocketStandard) 

base classes: bpy_struct, NodeSocket, NodeSocketStandard
class bpy.types. NodeSocketVectorXYZ ( NodeSocketStandard ) 

A node socket carrying a three-component vector.

[Related references](INDEX.md).
