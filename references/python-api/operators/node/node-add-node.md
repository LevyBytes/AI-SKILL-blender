# bpy.ops.node.add_node

bpy.ops.node. add_node ( * , settings = None , use_transform = False , type = '' , visible_output = '' ) 

Bring a node to the working mesh

Parameters :

- settings ( bpy_prop_collection [ NodeSetting ]) – Settings, Setups to put on the fresh node (optional)

- use_transform ( bool ) – Use Transform, Launch transform tool after putting in the node (optional)

- type ( str ) – Node Type, Node variety (optional, never None)

- visible_output ( str ) – Output Name, If given, every outlet named otherwise will be shut (optional, never None)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

File :

startup/bl_operators/node.py:490

[Related references](INDEX.md).
