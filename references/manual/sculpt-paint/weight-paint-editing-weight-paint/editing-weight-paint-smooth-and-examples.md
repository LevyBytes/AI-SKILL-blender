# Editing Weight Paint: Smooth, Examples

### Smooth

The Smooth operator averages selected vertex weights based on adjacent vertices,
producing smoother transitions in weight distributions. Use this for refining weight flows,
improving deformation during rigging, and removing sharp transitions between adjacent weights.

Note

This tool requires active vertex selection; without it, it becomes unavailable.

Subset
Limit operation to a subset.
See The Subset Option above for subset definitions.

Factor
Governs blending intensity toward connected vertex average weight.

- A Factor of 0.0 leaves weights untouched.

- A Factor of 1.0 applies the calculated average fully.

- Between 0.0 and 1.0 performs partial blending.

Iterations
Defines repetition count of the smoothing pass.
Higher counts yield smoother results but risk unwanted fine-detail degradation.

Expand/Contract
Modifies smoothing reach by expanding or contracting the affected region:

- Positive values widen the area to encompass nearby vertices.

- Negative values narrow focus to a smaller subset.

### Examples

Example: Single Selected Vertex

Suppose one selected vertex connects to four unselected ones.
The unselected vertices carry weights: 1, 0, 0, and 0.
Averaging unselected neighbors yields: \\((1 + 0 + 0 + 0) / 4 = 0.25\\)

With Factor set to:

- 0.0: Original weight preserved.

- 1.0: Adopts average (0.25).

- Between 0 and 1: Weight gradually shifts toward 0.25 proportionally.

Single vertex select with a Factor of 1.0.

Example: Multiple Selected Vertices

With multiple selected vertices,
Smooth evaluates each against its unselected neighbors.

For example:

- Three unselected neighbors with \\((1, 0, 0)\\) average to \\(0.333\\) .

- One unselected neighbor with weight 1 averages to \\(1.0\\) .

- Only unselected neighbors with \\((0, 0, 0)\\)
stays unchanged at \\(0.0\\) .

Factor value determines these final values.

Three selected vertices with a Factor of 1.0.

Example: Edge Loop Smoothing

A practical scenario involves selecting a center edge loop to
blend across adjacent regions. For instance:

- Two flanking unselected vertices on either edge carry \\(1\\) and \\(0\\) .

- Their average is \\((1 + 0) / 2 = 0.5\\) .

- Running Smooth with Factor at 1.0 colors the loop green,
creating gradual transition between "active" (left) and "inactive" (right) zones.

Center edge loop of vertices selected with a Factor of 1.0.

[Related references](INDEX.md).
