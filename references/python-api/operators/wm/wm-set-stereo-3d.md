# bpy.ops.wm.set_stereo_3d

bpy.ops.wm. set_stereo_3d ( * , display_mode = 'ANAGLYPH' , anaglyph_type = '`RED_CYAN`' , interlace_type = '`ROW_INTERLEAVED`' , use_interlace_swap = False , use_sidebyside_crosseyed = False ) 

Switches 3D stereo capability for the current window (or adjusts the display technique)

Parameters :

- display_mode (Literal[Stereo3D Display Items]) – Display Mode, (optional)

- anaglyph_type (Literal[Stereo3D Anaglyph Type Items]) – Anaglyph Type, (optional)

- interlace_type (Literal[Stereo3D Interlace Type Items]) – Interlace Type, (optional)

- use_interlace_swap ( bool ) – Swap Left/Right, Exchanges left and right stereo signals (optional)

- use_sidebyside_crosseyed ( bool ) – Cross-Eyed, Left eye sees right image and vice versa (optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]
bpy.ops.wm. set_stereo_3d ( * , display_mode = 'ANAGLYPH' , anaglyph_type = '`RED_CYAN`' , interlace_type = '`ROW_INTERLEAVED`' , use_interlace_swap = False , use_sidebyside_crosseyed = False )
Toggles 3D stereo support for the current window (or changes the display mode).
Parameters:
- display_mode (Literal[Stereo3D Display Items]) – Display Mode, (optional)
- anaglyph_type (Literal[Stereo3D Anaglyph Type Items]) – Anaglyph Type, (optional)
- interlace_type (Literal[Stereo3D Interlace Type Items]) – Interlace Type, (optional)
- use_interlace_swap ( bool ) – Swap Left/Right, Swap left and right stereo channels (optional)
- use_sidebyside_crosseyed ( bool ) – Cross-Eyed, Right eye should see left image and vice versa (optional)
Returns: The operator's result.
Return type: set[Literal[Operator Return Items]]

[Related references](INDEX.md).
