# bpy.types.KeyMapItems: new, new_modal, new_from_item

new ( idname , type , value , * , any = False , shift = 0 , ctrl = 0 , alt = 0 , oskey = 0 , hyper = 0 , key_modifier = 'NONE' , direction = 'ANY' , repeat = False , head = False ) 

new

Parameters :

- idname ( str ) – Operator Identifier, (never None)

- type (Literal[Event Type Items]) – Type

- value (Literal[Event Value Items]) – Value

- any ( bool ) – Any, (optional)

- shift ( int ) – Shift, (in [-1, 1], optional)

- ctrl ( int ) – Ctrl, (in [-1, 1], optional)

- alt ( int ) – Alt, (in [-1, 1], optional)

- oskey ( int ) – OS Key, (in [-1, 1], optional)

- hyper ( int ) – Hyper, (in [-1, 1], optional)

- key_modifier (Literal[Event Type Items]) – Key Modifier, (optional)

- direction (Literal[Event Direction Items]) – Direction, (optional)

- repeat ( bool ) – Repeat, When set, accept key-repeat events (optional)

- head ( bool ) – At Head, Force item to be added at start (not end) of key map so that it doesn’t get blocked by an existing key map item (optional)

Returns :

Item, Added key map item

Return type :

KeyMapItem
new_modal ( propvalue , type , value , * , any = False , shift = 0 , ctrl = 0 , alt = 0 , oskey = 0 , hyper = 0 , key_modifier = 'NONE' , direction = 'ANY' , repeat = False ) 

new_modal

Parameters :

- propvalue ( str ) – Property Value, (never None)

- type (Literal[Event Type Items]) – Type

- value (Literal[Event Value Items]) – Value

- any ( bool ) – Any, (optional)

- shift ( int ) – Shift, (in [-1, 1], optional)

- ctrl ( int ) – Ctrl, (in [-1, 1], optional)

- alt ( int ) – Alt, (in [-1, 1], optional)

- oskey ( int ) – OS Key, (in [-1, 1], optional)

- hyper ( int ) – Hyper, (in [-1, 1], optional)

- key_modifier (Literal[Event Type Items]) – Key Modifier, (optional)

- direction (Literal[Event Direction Items]) – Direction, (optional)

- repeat ( bool ) – Repeat, When set, accept key-repeat events (optional)

Returns :

Item, Added key map item

Return type :

KeyMapItem
new_from_item ( item , * , head = False ) 

new_from_item

Parameters :

- item (KeyMapItem) – Item, Item to use as a reference (never None)

- head ( bool ) – At Head, (optional)

Returns :

Item, Added key map item

Return type :

KeyMapItem

[Related references](INDEX.md).
