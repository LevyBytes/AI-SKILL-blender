# bpy.ops.sculpt.color_filter

bpy.ops.sculpt. color_filter ( * , start_mouse = (0, 0) , area_normal_radius = 0.25 , strength = 1.0 , iteration_count = 1 , event_history = None , type = 'FILL' , fill_color = (1.0, 1.0, 1.0) )

Enact a transformation to change the current color property

Parameters :

- start_mouse ( Sequence [ int ] ) – Starting Mouse, (array of 2 items, in [0, 16384], optional)

- area_normal_radius ( float ) – Normal Radius, Span for computing surface orientation when clicked, measured as a share of brush radius(in [0.001, 5], optional)

- strength ( float ) – Strength, How much the filter affects the colors (in [-10, 10], optional)

- iteration_count ( int ) – Repeat, How many times to execute the filter (in [1, 10000], optional)

- event_history ( bpy_prop_collection [ OperatorStrokeElement ]) – (optional)

- type ( Literal [ 'FILL' , 'HUE' , 'SATURATION' , 'VALUE' , 'BRIGHTNESS' , 'CONTRAST' , 'SMOOTH' , 'RED' , 'GREEN' , 'BLUE' ] ) – Filter Type, (optional)

- FILL
Fill – Fill with a specific color.

- HUE
Hue – Change hue.

- SATURATION
Saturation – Change saturation.

- VALUE
Value – Change value.

- BRIGHTNESS
Brightness – Change brightness.

- CONTRAST
Contrast – Change contrast.

- SMOOTH
Smooth – Smooth colors.

- RED
Red – Change red channel.

- GREEN
Green – Change green channel.

- BLUE
Blue – Change blue channel.

- fill_color (mathutils.Color) – Fill Color, (array of 3 items, in [0, inf], optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
