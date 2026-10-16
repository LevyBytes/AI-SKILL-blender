# bpy.ops.grease_pencil.trace_image

bpy.ops.grease_pencil.trace_image ( * , target = 'NEW' , threshold = 0.5 , turnpolicy = 'MINORITY' , mode = 'SINGLE' , use_current_frame = True , frame_number = 0 )
Derive Grease Pencil strokes from raster imagery

Parameters:
- target ( Literal [ 'NEW' , 'SELECTED' ] ) – Target Object, Destination Grease Pencil (optional)
- threshold ( float ) – Color Threshold, Luminance boundary for stroke generation (in [0, 1], optional)
- turnpolicy ( Literal [ 'FOREGROUND' , 'BACKGROUND' , 'LEFT' , 'RIGHT' , 'MINORITY' , 'MAJORITY' , 'RANDOM' ] ) – Turn Policy, Strategy for resolving ambiguities during path decomposition (optional)
- FOREGROUND: Favor linking of foreground regions
- BACKGROUND: Favor linking of background regions
- LEFT: Always turn left
- RIGHT: Always turn right
- MINORITY: Connect the less-common neighboring color
- MAJORITY: Connect the more-common neighboring color
- RANDOM: Select pseudo-randomly
- mode ( Literal [ 'SINGLE' , 'SEQUENCE' ] ) – Mode, Whether to process one or a full sequence (optional)
- SINGLE: Convert the current image frame only
- SEQUENCE: Convert all sequential frames
- use_current_frame ( bool ) – Start At Current Frame, Begin conversion at the active image frame (optional)
- frame_number ( int ) – Trace Frame, Index of the single frame to trace, or zero to trace all (in [0, 9999], optional)

Returns:
Result of the operator call.
Return type: set[Literal[Operator Return Items]]

[Related references](INDEX.md).
