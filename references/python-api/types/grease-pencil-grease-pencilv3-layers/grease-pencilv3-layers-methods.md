# bpy.types.GreasePencilv3Layers: methods

new ( name , * , set_active = True , layer_group = None )

Create another Grease Pencil layer.

Parameters :

- name ( str ) – Name, Name of the layer (never None)

- set_active ( bool ) – Set Active, Set the newly created layer as the active layer (optional)

- layer_group (GreasePencilLayerGroup) – The layer group the new layer will be created in (use None for the main stack) (optional)

Returns :

The newly created layer

Return type :

GreasePencilLayer
remove ( layer )

Delete a Grease Pencil layer.

Parameters :

layer (GreasePencilLayer) – The layer to remove (never None)
move ( layer , type )

Shift a Grease Pencil layer within its layer group or the main stack.

Parameters :

- layer (GreasePencilLayer) – The layer to move (never None)

- type ( Literal [ 'DOWN' , 'UP' ] ) – Direction of movement
move_top ( layer )

Send a Grease Pencil layer up to the top of its layer group or the main stack.

Parameters :

layer (GreasePencilLayer) – The layer to move (never None)
move_bottom ( layer )

Send a Grease Pencil layer down to the bottom of its layer group or the main stack.

Parameters :

layer (GreasePencilLayer) – The layer to move (never None)
move_to_layer_group ( layer , layer_group )

Relocate a Grease Pencil layer into a layer group.

Parameters :

- layer (GreasePencilLayer) – The layer to move (never None)

- layer_group (GreasePencilLayerGroup) – The layer group the layer will be moved into (use None for the main stack)
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
