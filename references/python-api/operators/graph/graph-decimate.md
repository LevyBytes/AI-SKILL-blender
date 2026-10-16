# bpy.ops.graph.decimate

bpy.ops.graph.decimate(*, mode='RATIO', factor=0.333333, remove_error_margin=0.0)

Shrink trajectories by removing frames that change the trajectory form the utmost

Parameters:

- mode (Literal['RATIO', 'ERROR']) – Mode, Which technique to utilize for reduction (optional)

- RATIO
Ratio – Use a portion to convey how numerous frames you wish to purge.

- ERROR
Error Margin – Use an divergence margin to convey how considerably the trajectory is sanctioned to deviate from the initial course.

- factor (float) – Factor, The portion of frames to purge (in [0, 1], optional)
- remove_error_margin (float) – Max Error Margin, How considerably the re-shaped trajectory is sanctioned to deviate from the initial (in [0, inf], optional)

Returns:

Result of the operator call.

Return type:

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
