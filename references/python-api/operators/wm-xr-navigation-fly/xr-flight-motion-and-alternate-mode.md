# bpy.ops.wm.xr_navigation_fly: motion controls and alternate flight

bpy.ops.wm. xr_navigation_fly ( * , mode = '`VIEWER_FORWARD`' , snap_turn_threshold = 0.95 , lock_location_z = False , lock_direction = False , speed_frame_based = False , turn_speed_factor = 0.333333 , fly_speed_factor = 0.333333 , speed_interpolation0 = (0.0, 0.0) , speed_interpolation1 = (1.0, 1.0) , alt_mode = '`VIEWER_FORWARD`' , alt_lock_location_z = False , alt_lock_direction = False ) 

- lock_location_z ( bool ) – Lock Elevation, Avert variations to watcher height (optional)

- lock_direction ( bool ) – Lock Direction, Restrict shifting to watcher's initial bearing (optional)

- speed_frame_based ( bool ) – Frame Based Speed, Implement unchanged shifting quantities every session (optional)

- turn_speed_factor ( float ) – Turn Speed Factor, Portion of the minimal and maximal pivot rate (in [0, 1], optional)

- fly_speed_factor ( float ) – Fly Speed Factor, Portion of the minimal and maximal travel rate (in [0, 1], optional)

- speed_interpolation0 (mathutils.Vector) – Speed Interpolation 0, Initial cardinal spline anchor point among minimal/maximal rates (cluster of 2 items, in [0, 1], optional)

- speed_interpolation1 (mathutils.Vector) – Speed Interpolation 1, Next cardinal spline anchor point among minimal/maximal rates (cluster of 2 items, in [0, 1], optional)

- alt_mode ( Literal [ 'FORWARD' , 'BACK' , 'LEFT' , 'RIGHT' , 'UP' , 'DOWN' , 'TURNLEFT' , 'TURNRIGHT' , '`VIEWER_FORWARD`' , '`VIEWER_BACK`' , '`VIEWER_LEFT`' , '`VIEWER_RIGHT`' , '`CONTROLLER_FORWARD`' ] ) – Mode (Alt), Flight pattern when tools are reversed (optional)

- FORWARD
Forward – Shift along pathway ahead marker.

- BACK
Back – Shift along pathway rear marker.

- LEFT
Left – Shift along pathway left marker.

- RIGHT
Right – Shift along pathway right marker.

- UP
Up – Shift along pathway upper marker.

- DOWN
Down – Shift along pathway lower marker.

- TURNLEFT
Turn Left – Pivot leftward about pathway upper marker.

- TURNRIGHT
Turn Right – Pivot rightward about pathway upper marker.

- `VIEWER_FORWARD`
Viewer Forward – Shift along watcher's ahead marker.

- `VIEWER_BACK`
Viewer Back – Shift along watcher's rear marker.

- `VIEWER_LEFT`
Viewer Left – Shift along watcher's left marker.

- `VIEWER_RIGHT`
Viewer Right – Shift along watcher's right marker.

- `CONTROLLER_FORWARD`
Controller Forward – Shift along gadget's ahead marker.

- alt_lock_location_z ( bool ) – Lock Elevation (Alt), When tools are reversed, avert variations to watcher height (optional)

- alt_lock_direction ( bool ) – Lock Direction (Alt), When tools are reversed, limit shifting to watcher's initial bearing (optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
