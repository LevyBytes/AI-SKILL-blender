# bpy.ops.paint.add_texture_paint_slot

bpy.ops.paint. add_texture_paint_slot ( * , type = '`BASE_COLOR`' , slot_type = 'IMAGE' , name = 'Untitled' , color = (0.0, 0.0, 0.0, 1.0) , width = 1024 , height = 1024 , alpha = True , generated_type = 'BLANK' , float = False , domain = 'POINT' , data_type = '`FLOAT_COLOR`' ) 

Introduce a paint tray

Parameters :

- type ( Literal [ '`BASE_COLOR`' , 'SPECULAR' , 'ROUGHNESS' , 'METALLIC' , 'NORMAL' , 'BUMP' , 'DISPLACEMENT' ] ) – Material Layer Type, Substance tier category of updated paint tray (optional)

- slot_type ( Literal [ 'IMAGE' , '`COLOR_ATTRIBUTE`' ] ) – Slot Type, Genre of updated paint tray (optional)

- name ( str ) – Name, Title for updated paint tray resource (optional, never None)

- color ( Sequence [ float ] ) – Color, Preliminary padding tint (array of 4 items, in [0, inf], optional)

- width ( int ) – Width, Image extent (in [1, inf], optional)

- height ( int ) – Height, Image measurement (in [1, inf], optional)

- alpha ( bool ) – Alpha, Construct a picture incorporating an opacity channel (optional)

- generated_type (Literal[Image Generated Type Items]) – Generated Type, Replenish the picture with a lattice for coordinate atlas checking (optional)

- float ( bool ) – 32-bit Float, Construct picture with 32-bit floating-point bit profundity (optional)

- domain (Literal[Color Attribute Domain Items]) – Domain, Genre of component that characteristic is housed on (optional)

- data_type (Literal[Color Attribute Type Items]) – Data Type, Genre of data lodged in characteristic (optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
