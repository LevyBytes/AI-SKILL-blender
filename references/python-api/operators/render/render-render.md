# bpy.ops.render.render

bpy.ops.render. render ( * , animation = False , write_still = False , use_viewport = False , use_sequencer_scene = False , layer = '' , scene = '' , frame_start = 0 , frame_end = 0 ) 

Undocumented, consider contributing.

Parameters :

- animation ( bool ) – Animation, Render files from the animation range of this scene (optional)

- write_still ( bool ) – Write Image, Save the rendered image to the output path (used only when animation is disabled) (optional)

- use_viewport ( bool ) – Use 3D Viewport, When inside a 3D viewport, use layers and camera of the viewport (optional)

- use_sequencer_scene ( bool ) – Use Sequencer Scene, Render the sequencer scene instead of the active scene (optional)

- layer ( str ) – Render Layer, Single render layer to re-render (used only when animation is disabled) (optional, never None)

- scene ( str ) – Scene, Scene to render, current scene if not specified (optional, never None)

- frame_start ( int ) – Start Frame, Frame to start rendering animation at. If not specified, the scene start frame will be assumed. This should only be specified if doing an animation render (in [-inf, inf], optional)

- frame_end ( int ) – End Frame, Frame to end rendering animation at. If not specified, the scene end frame will be assumed. This should only be specified if doing an animation render (in [-inf, inf], optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
