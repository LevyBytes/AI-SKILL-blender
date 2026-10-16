# bpy.ops.wm.xr_navigation_teleport

bpy.ops.wm. xr_navigation_teleport ( * , selectable_only = True , force = 8.5 , range = 0.15 , ray_line_width = 6.0 , destination_indicator_width = 0.18 , hit_color = (0.4, 0.6, 0.9, 1.0) , miss_color = (1.0, 0.35, 0.35, 1.0) , fallback_color = (0.5, 0.45, 0.8, 1.0) ) 

Position VR watcher spot to tool ray collision area

Parameters :

- selectable_only ( bool ) – Selectable Only, Permit merely selectable things to have an impact on ray-casting output (optional)

- force ( float ) – Force, Strength push handling the shifting arc flight in m/s (in [0, inf], optional)

- range ( float ) – Range, Temporal segmentation span handling the shifting arc flight (in [0, inf], optional)

- ray_line_width ( float ) – Ray Line Width, Graphic breadth of the shifting ray direction (in [0, inf], optional)

- destination_indicator_width ( float ) – Destination Indicator Width, Graphic breadth of the impact target marker (in [0, inf], optional)

- hit_color ( Sequence [ float ] ) – Hit Color, Hue of ray-casting when it is successful (grouping of 4 items, in [0, 1], optional)

- miss_color ( Sequence [ float ] ) – Miss Color, Hue of ray-casting when it is unsuccessful (grouping of 4 items, in [0, 1], optional)

- fallback_color ( Sequence [ float ] ) – Fallback Color, Hue of ray-casting when a fallback instance is successful (grouping of 4 items, in [0, 1], optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
