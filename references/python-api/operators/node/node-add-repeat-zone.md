# bpy.ops.node.add_repeat_zone

bpy.ops.node. add_repeat_zone ( * , settings = None , use_transform = False , offset = (150.0, 0.0) ) 

Generate a repeat region that permits operating nodes a changing count of times

Parameters :

- settings ( bpy_prop_collection [ NodeSetting ]) – Settings, Setups to put on the fresh node (optional)

- use_transform ( bool ) – Use Transform, Launch transform tool after putting in the node (optional)

- offset ( Sequence [ float ] ) – Offset, How far to place nodes from the marker when putting them (array of 2 items, in [-inf, inf], optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

File :

startup/bl_operators/node.py:729

[Related references](INDEX.md).
