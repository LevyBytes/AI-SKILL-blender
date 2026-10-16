# bpy.ops.grease_pencil.bake_grease_pencil_animation

bpy.ops.grease_pencil.bake_grease_pencil_animation ( * , frame_start = 1 , frame_end = 250 , step = 1 , only_selected = False , frame_target = 1 , project_type = 'KEEP' )
Encode object motion into stroke keyframes

Parameters:
- frame_start ( int ) – Start Frame, Timeline beginning point (in [1, 100000], optional)
- frame_end ( int ) – End Frame, Timeline endpoint (in [1, 100000], optional)
- step ( int ) – Step, Spacing between intermediate frames (in [1, 100], optional)
- only_selected ( bool ) – Only Selected Keyframes, Process only highlighted keyframes (optional)
- frame_target ( int ) – Target Frame, Output keyframe number (in [1, 100000], optional)
- project_type ( Literal [ 'KEEP' , 'FRONT' , 'SIDE' , 'TOP' , 'VIEW' , 'CURSOR' ] ) – Projection Type, (optional)
- KEEP: Leave strokes at their original orientation
- FRONT: Project onto the X-Z plane
- SIDE: Project onto the Y-Z plane
- TOP: Project onto the X-Y plane
- VIEW: Project to align with the current camera viewpoint using cursor placement
- CURSOR: Project based on 3D cursor orientation

Returns:
Result of the operator call.
Return type: set[Literal[Operator Return Items]]

[Related references](INDEX.md).
