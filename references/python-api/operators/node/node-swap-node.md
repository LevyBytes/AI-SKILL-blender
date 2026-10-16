# bpy.ops.node.swap_node

bpy.ops.node. swap_node ( * , settings = None , type = '' , visible_output = '' ) 

Exchange the selected nodes for the requested classification

Parameters :

- settings ( bpy_prop_collection [ NodeSetting ]) – Settings, Settings to be applied on the newly created node (optional)

- type ( str ) – Node Type, Node type (optional, never None)

- visible_output ( str ) – Output Name, If provided, all outputs that are named differently will be hidden (optional, never None)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

File :

startup/bl_operators/node.py:555

[Related references](INDEX.md).
