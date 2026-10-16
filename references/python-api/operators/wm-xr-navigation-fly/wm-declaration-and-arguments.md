# bpy.ops.wm.xr_navigation_fly: declaration-and-arguments

bpy.ops.wm. xr_navigation_fly ( * , mode = '`VIEWER_FORWARD`' , snap_turn_threshold = 0.95 , lock_location_z = False , lock_direction = False , speed_frame_based = False , turn_speed_factor = 0.333333 , fly_speed_factor = 0.333333 , speed_interpolation0 = (0.0, 0.0) , speed_interpolation1 = (1.0, 1.0) , alt_mode = '`VIEWER_FORWARD`' , alt_lock_location_z = False , alt_lock_direction = False ) 

Shift/pivot matching the VR watcher or tool

Parameters :

- mode ( Literal [ 'FORWARD' , 'BACK' , 'LEFT' , 'RIGHT' , 'UP' , 'DOWN' , 'TURNLEFT' , 'TURNRIGHT' , '`VIEWER_FORWARD`' , '`VIEWER_BACK`' , '`VIEWER_LEFT`' , '`VIEWER_RIGHT`' , '`CONTROLLER_FORWARD`' ] ) – Mode, Flight pattern (optional)

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

- snap_turn_threshold ( float ) – Snap Turn Threshold, Trigger rank for action when utilizing break pivot (in [0, 1], optional)

[Related references](INDEX.md).
