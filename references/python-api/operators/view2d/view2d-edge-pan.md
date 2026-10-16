# bpy.ops.view2d.edge_pan

bpy.ops.view2d. edge_pan ( * , inside_padding = 1.0 , outside_padding = 0.0 , speed_ramp = 1.0 , max_speed = 500.0 , delay = 1.0 , zoom_influence = 0.0 ) 

Scrolls the view while the mouse rests against an edge

Parameters :

- inside_padding ( float ) – Inside Padding, Inside distance in UI units from the edge of the region within which to start panning (in [0, 100], optional)

- outside_padding ( float ) – Outside Padding, Outside distance in UI units from the edge of the region at which to stop panning (in [0, 100], optional)

- speed_ramp ( float ) – Speed Ramp, Width of the zone in UI units where speed increases with distance from the edge (in [0, 100], optional)

- max_speed ( float ) – Max Speed, Maximum speed in UI units per second (in [0, 10000], optional)

- delay ( float ) – Delay, Delay in seconds before maximum speed is reached (in [0, 10], optional)

- zoom_influence ( float ) – Zoom Influence, Influence of the zoom factor on scroll speed (in [0, 1], optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
