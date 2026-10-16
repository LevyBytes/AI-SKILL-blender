# bpy.ops.cycles.denoise_animation

**bpy.ops.cycles.denoise_animation**( * , input_filepath = '' , output_filepath = '' )

Use the denoising algorithm to clean up a rendered animation. Requires denoising data passes saved as OpenEXR.

Parameters:
- input_filepath ( str ) – Input Filepath, Image file path for denoising. If blank, uses the render output path and frame range (optional, never None)
- output_filepath ( str ) – Output Filepath, If blank, denoises in place (optional, never None)

Returns: Result of the operator call.
Return type: set[Literal[Operator Return Items]]

File: addons_core/cycles/operators.py:49

[Related references](INDEX.md).
