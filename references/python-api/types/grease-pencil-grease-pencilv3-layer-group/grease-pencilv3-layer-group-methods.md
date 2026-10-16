# bpy.types.GreasePencilv3LayerGroup: methods

new ( name , * , parent_group = None )

Create another Grease Pencil layer group.

Parameters :

- name ( str ) – Name, Name of the layer group (never None)

- parent_group (GreasePencilLayerGroup) – The parent layer group the new group will be created in (use None for the main stack) (optional)

Returns :

The newly created layer group

Return type :

GreasePencilLayerGroup
remove ( layer_group , * , keep_children = False )

Delete a Grease Pencil layer group.

Parameters :

- layer_group (GreasePencilLayerGroup) – The layer group to remove (never None)

- keep_children ( bool ) – Keep the children nodes of the group and only delete the group itself (optional)
move ( layer_group , type )

Shift a layer group within its parent group or the main stack.

Parameters :

- layer_group (GreasePencilLayerGroup) – The layer group to move (never None)

- type ( Literal [ 'DOWN' , 'UP' ] ) – Direction of movement
move_top ( layer_group )

Send a layer group up to the top of its parent group or the main stack.

Parameters :

layer_group (GreasePencilLayerGroup) – The layer group to move (never None)
move_bottom ( layer_group )

Send a layer group down to the bottom of its parent group or the main stack.

Parameters :

layer_group (GreasePencilLayerGroup) – The layer group to move (never None)
move_to_layer_group ( layer_group , parent_group )

Relocate a layer group inside a parent layer group.

Parameters :

- layer_group (GreasePencilLayerGroup) – The layer group to move (never None)

- parent_group (GreasePencilLayerGroup) – The parent layer group the layer group will be moved into (use None for the main stack)
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

[Related references](INDEX.md).
