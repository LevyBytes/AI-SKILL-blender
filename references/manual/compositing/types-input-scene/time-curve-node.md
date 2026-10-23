# Time Curve Node

## Time Curve Node

The Time Curve node produces a factor (0.0 to 1.0) between the scene's start and end time via a curve mapping. Inputs: Start/End Frame (the time range whose values the output should span, becoming the graph's X axis — and reversible by setting a start frame greater than the end). Properties: Curve (the curve's Y value is the factor output; see the Curve widget) — and flipping the curve reverses the time input, which is easy to overlook. Output: Factor (the curve's Y value at the current frame). A hint notes the Map Range Node can remap the output, and since some curves can push the Time Curve above one or below zero, the Map Value node's Min/Max clamping can keep it safe.

The Time Curve node produces a factor value (0.0 to 1.0) between the scene's start and end time via a curve mapping.

Inputs:
Start/End Frame: the start and end frames of the time range whose values the output should span; this range becomes the graph's X axis. Set a start frame past the end frame to run the time input in reverse.

Properties:
Curve: the Y value the curve defines is the factor output; for the controls, see Curve widget. Tip: flipping the curve reverses the time input, but that's easy to miss in the node setup.

Outputs:
Factor: the curve's Y value at the current frame.
Hint: the Map Range Node can remap the output to a more fitting value. Some curves can make the Time Curve node output above one or below zero, so to be safe use the Map Value node's Min/Max clamping to bound the output.

Example: the time controls, left to right: none, slow down, freeze, speed up, reverse.

[Related references](INDEX.md).
