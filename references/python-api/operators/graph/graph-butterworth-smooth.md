# bpy.ops.graph.butterworth_smooth

bpy.ops.graph.butterworth_smooth(*, cutoff_frequency=3.0, filter_order=4, samples_per_frame=1, blend=1.0, blend_in_out=1)

Make smooth a animation while keeping the general course of the trajectory

Parameters:

- cutoff_frequency (float) – Frequency Cutoff (Hz), Reduced principles provide a sleeker trajectory (in [0, inf], optional)
- filter_order (int) – Filter Order, Taller principles create a stricter frequency border (in [1, 32], optional)
- samples_per_frame (int) – Samples per Frame, Quantity of estimates to reckon per timing, facilitates with subframe material (in [1, 64], optional)
- blend (float) – Blend, How considerably to blend to the sleek trajectory (in [0, inf], optional)
- blend_in_out (int) – Blend In/Out, Straight blend the silky material to the edge frames of the pick (in [0, inf], optional)

Returns:

Result of the operator call.

Return type:

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
