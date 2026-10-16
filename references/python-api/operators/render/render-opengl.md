# bpy.ops.render.opengl

bpy.ops.render. opengl ( * , animation = False , render_keyed_only = False , sequencer = False , write_still = False , view_context = True ) 

Grab a snapshot of the currently active viewport

Parameters :

- animation ( bool ) – Animation, Render files from the animation range of this scene (optional)

- render_keyed_only ( bool ) – Render Keyframes Only, Render only those frames where selected objects have a key in their animation data. Only used when rendering animation (optional)

- sequencer ( bool ) – Sequencer, Render using the sequencer's OpenGL display (optional)

- write_still ( bool ) – Write Image, Save the rendered image to the output path (used only when animation is disabled) (optional)

- view_context ( bool ) – View Context, Use the current 3D view for rendering, else use scene settings (optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
