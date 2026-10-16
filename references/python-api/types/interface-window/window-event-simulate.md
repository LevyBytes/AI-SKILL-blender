# bpy.types.Window: event_simulate

event_simulate ( type , value , * , unicode = '' , x = 0 , y = 0 , shift = False , ctrl = False , alt = False , oskey = False , hyper = False )

event_simulate

Parameters :

- type (Literal[Event Type Items]) – Type

- value (Literal[Event Value Items]) – Value

- unicode ( str ) – (optional)

- x ( int ) – (in [-inf, inf], optional)

- y ( int ) – (in [-inf, inf], optional)

- shift ( bool ) – Shift, (optional)

- ctrl ( bool ) – Ctrl, (optional)

- alt ( bool ) – Alt, (optional)

- oskey ( bool ) – OS Key, (optional)

- hyper ( bool ) – Hyper, (optional)

Returns :

Item, Added key map item

Return type :

Event

[Related references](INDEX.md).
