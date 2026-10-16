# bpy.ops.node.swap_zone

bpy.ops.node. swap_zone ( * , settings = None , offset = (150.0, 0.0) , input_node_type = '' , output_node_type = '' , add_default_geometry_link = False ) 

Undocumented, consider contributing.

Parameters :

- settings ( bpy_prop_collection [ NodeSetting ]) – Settings, Settings to be applied on the newly created node (optional)

- offset ( Sequence [ float ] ) – Offset, Offset of nodes from the cursor when added (array of 2 items, in [-inf, inf], optional)

- input_node_type ( str ) – Input Node, Specifies the input node used by the created zone (optional, never None)

- output_node_type ( str ) – Output Node, Specifies the output node used by the created zone (optional, never None)

- add_default_geometry_link ( bool ) – Add Geometry Link, When enabled, create a link between geometry sockets in this zone (optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

File :

startup/bl_operators/node.py:847

[Related references](INDEX.md).
