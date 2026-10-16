# bpy.ops.cycles.merge_images

**bpy.ops.cycles.merge_images**( * , input_filepath1 = '' , input_filepath2 = '' , output_filepath = '' )

Merge OpenEXR files rendered at different sample counts into a single image with lower noise.

Parameters:
- input_filepath1 ( str ) – Input Filepath, Image file path to merge (optional, never None)
- input_filepath2 ( str ) – Input Filepath, Image file path to merge (optional, never None)
- output_filepath ( str ) – Output Filepath, Image file path for the merged result (optional, never None)

Returns: Result of the operator call.
Return type: set[Literal[Operator Return Items]]

File: addons_core/cycles/operators.py:137

[Related references](INDEX.md).
