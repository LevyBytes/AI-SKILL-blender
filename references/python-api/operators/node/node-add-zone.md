# bpy.ops.node.add_zone

bpy.ops.node. add_zone ( * , settings = None , use_transform = False , offset = (150.0, 0.0) , input_node_type = '' , output_node_type = '' , add_default_geometry_link = False ) 

Undescribed, think about adding to docs.

Parameters :

- settings ( bpy_prop_collection [ NodeSetting ]) – Settings, Setups to put on the fresh node (optional)

- use_transform ( bool ) – Use Transform, Launch transform tool after putting in the node (optional)

- offset ( Sequence [ float ] ) – Offset, How far to place nodes from the marker when putting them (array of 2 items, in [-inf, inf], optional)

- input_node_type ( str ) – Input Node, Says what entry node the made zone employs (optional, never None)

- output_node_type ( str ) – Output Node, Says what exit node the made zone employs (optional, never None)

- add_default_geometry_link ( bool ) – Add Geometry Link, When on, link inlets between shape components in this region (optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

File :

startup/bl_operators/node.py:729

[Related references](INDEX.md).
