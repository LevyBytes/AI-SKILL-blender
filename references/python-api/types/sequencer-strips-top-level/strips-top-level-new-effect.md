# bpy.types.StripsTopLevel: new_effect ( name , type , channel , frame_start , * , length = 0 , input1 = None , input2 = None )

new_effect ( name , type , channel , frame_start , * , length = 0 , input1 = None , input2 = None )

Add a new effect strip

Parameters :

- name ( str ) – Name for the new strip (never None)

- type ( Literal [ 'CROSS' , 'ADD' , 'SUBTRACT' , '`ALPHA_OVER`' , '`ALPHA_UNDER`' , '`GAMMA_CROSS`' , 'MULTIPLY' , 'WIPE' , 'GLOW' , 'COLOR' , 'SPEED' , 'MULTICAM' , 'ADJUSTMENT' , '`GAUSSIAN_BLUR`' , 'TEXT' , 'COLORMIX' ] ) – Type, type for the new strip

- CROSS
Crossfade – Fade out of one video, fading into another.

- ADD
Add – Add together color channels from two videos.

- SUBTRACT
Subtract – Subtract one strip’s color from another.

- `ALPHA_OVER`
Alpha Over – Blend alpha on top of another video.

- `ALPHA_UNDER`
Alpha Under – Blend alpha below another video.

- `GAMMA_CROSS`
Gamma Crossfade – Crossfade with color correction.

- MULTIPLY
Multiply – Multiply color channels from two videos.

- WIPE
Wipe – Sweep a transition line across the frame.

- GLOW
Glow – Add blur and brightness to light areas.

- COLOR
Color – Add a simple color strip.

- SPEED
Speed – Timewarp video strips, modifying playback speed.

- MULTICAM
Multicam Selector – Control active camera angles.

- ADJUSTMENT
Adjustment Layer – Apply nondestructive effects.

- `GAUSSIAN_BLUR`
Gaussian Blur – Soften details along axes.

- TEXT
Text – Add a simple text strip.

- COLORMIX
Color Mix – Combine two strips using blend modes.

- channel ( int ) – Channel, The channel for the new strip (in [1, 128])

- frame_start ( int ) – The start frame for the new strip (in [-inf, inf])

- length ( int ) – Length of the strip in frames, or the length of each strip if multiple are added (in [-inf, inf], optional)

- input1 (Strip) – First input strip for effect (optional)

- input2 (Strip) – Second input strip for effect (optional)

Returns :

New Strip

Return type :

Strip

[Related references](INDEX.md).
