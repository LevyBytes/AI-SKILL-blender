# bpy.ops.sequencer.select_lasso

bpy.ops.sequencer.select_lasso(*, path=None, use_smooth_stroke=False, smooth_stroke_factor=0.75, smooth_stroke_radius=35, mode='SET')

Pick pieces via freehand selection.

Parameters:

- path (bpy_prop_collection[OperatorMousePath]) – Path, (optional)
- use_smooth_stroke (bool) – Stabilize Stroke, Choice lags behind the pointer and follows a softer arc (optional)
- smooth_stroke_factor (float) – Smooth Stroke Factor, Larger numbers generate a softer path (in [0.5, 0.99], optional)
- smooth_stroke_radius (int) – Smooth Stroke Radius, Least separation from last point before choice resumes (in [10, 200], optional)
- mode (Literal['SET', 'ADD', 'SUB']) – Mode, (optional)
  - SET
    Set – Establish a fresh choice.
  - ADD
    Extend – Grow the existing choice.
  - SUB
    Subtract – Reduce the existing choice.

Returns:

Operation result.

Return type:

set[Literal[Operator Return Items]]
bpy.ops.sequencer.select_lasso(*, path=None, use_smooth_stroke=False, smooth_stroke_factor=0.75, smooth_stroke_radius=35, mode='SET')

Pick pieces via freehand selection.

Parameters:

- path (bpy_prop_collection[OperatorMousePath]) – Path, (optional)
- use_smooth_stroke (bool) – Stabilize Stroke, Choice lags behind the pointer and follows a softer arc (optional)
- smooth_stroke_factor (float) – Smooth Stroke Factor, Larger numbers generate a softer path (in [0.5, 0.99], optional)
- smooth_stroke_radius (int) – Smooth Stroke Radius, Least separation from last point before choice resumes (in [10, 200], optional)
- mode (Literal['SET', 'ADD', 'SUB']) – Mode, (optional)
  - SET
    Set – Establish a fresh choice.
  - ADD
    Extend – Grow the existing choice.
  - SUB
    Subtract – Reduce the existing choice.

Returns:

Operation result.

Return type:

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
