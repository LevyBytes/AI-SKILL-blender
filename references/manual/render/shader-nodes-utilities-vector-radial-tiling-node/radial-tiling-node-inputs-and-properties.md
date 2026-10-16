# Radial Tiling Node: Inputs, Properties, Outputs

## Radial Tiling Node

The Radial Tiling Node splits a 2D Cartesian input coordinate system into as many radial segments as the Sides input asks for. Each segment carries its own affinely transformed segment coordinate system, which you can use to tile textures in a radially symmetric way.

Inputs:
Vector — the input system's vector to divide into radial segments.
Sides — how many radial segments to split the input coordinate system into; a non-integer value leaves one irregular segment that is smaller than the regular ones (illustrated at Sides 5.0, 5.25, 5.5, and 6.0).
Roundness — the roundness of the segment coordinate systems (illustrated at 0.0, 0.25, 0.5, and 1.0).

Properties:
Normalize — when enabled, the Segment Coordinates output's X-coordinates are remapped into a 0.0 to 1.0 range and a constant 1.0 is added to the Y-coordinates, making the output range non-negative.

Outputs:
Segment Coordinates — segment coordinates for mapping textures within each radial segment.
Segment ID — a unique ID per radial segment, starting at 0 and increasing by 1 counterclockwise for each segment.
Segment Width — the relative width of each radial segment; can scale textures to fit each one.
Segment Rotation — the counterclockwise rotation of each segment coordinate system; can align the rotation of each segment's textures.

Examples: the Segment Coordinates output tiles textures radially, demonstrated by radially tiling a heart texture. As the segment count rises, each segment's relative width shrinks, eventually making the textures overlap and clip — visible at Sides 6.5, where the non-integer value worsens the clipping because of the smaller irregular segment; feed the Segment Width output back in to scale the textures by each segment's relative width and avoid this (the example uses an arbitrary texture scale of 0.725, tweakable to resize the textures). By default the segment coordinate systems are rotated so their Y-axes meet the origin; the Segment Rotation output can instead align them along a global direction (the example uses an arbitrary texture rotation of -1.571, tweakable to rotate the textures). For textures spanning the whole UV space, seams along segment borders usually show even when the source texture is seamless; the Normalize option removes these seams by keeping the X-coordinates spanning the full 0 to 1 range, though it adds a distortion effect you may need extra nodes to counter if it's unwanted. For some textures a more rounded look near segment borders helps, achieved by raising the Roundness input.

The Radial Tiling Node splits a 2D Cartesian input coordinate system into as many radial segments as the Sides input asks for. Each segment carries its own affinely transformed segment coordinate system, which you can use to tile textures in a radially symmetric way.

Inputs:
Vector — the input system's vector to divide into radial segments.
Sides — how many radial segments to split the input coordinate system into; a non-integer value leaves one irregular segment that is smaller than the regular ones (illustrated at Sides 5.0, 5.25, 5.5, and 6.0).
Roundness — the roundness of the segment coordinate systems (illustrated at 0.0, 0.25, 0.5, and 1.0).

Properties:
Normalize — when enabled, the Segment Coordinates output's X-coordinates are remapped into a 0.0 to 1.0 range and a constant 1.0 is added to the Y-coordinates, making the output range non-negative.

Outputs:
Segment Coordinates — segment coordinates for mapping textures within each radial segment.
Segment ID — a unique ID per radial segment, starting at 0 and increasing by 1 counterclockwise for each segment.
Segment Width — the relative width of each radial segment; can scale textures to fit each one.
Segment Rotation — the counterclockwise rotation of each segment coordinate system; can align the rotation of each segment's textures.

Examples: the Segment Coordinates output tiles textures radially, demonstrated by radially tiling a heart texture. As the segment count rises, each segment's relative width shrinks, eventually making the textures overlap and clip — visible at Sides 6.5, where the non-integer value worsens the clipping because of the smaller irregular segment; feed the Segment Width output back in to scale the textures by each segment's relative width and avoid this (the example uses an arbitrary texture scale of 0.725, tweakable to resize the textures). By default the segment coordinate systems are rotated so their Y-axes meet the origin; the Segment Rotation output can instead align them along a global direction (the example uses an arbitrary texture rotation of -1.571, tweakable to rotate the textures). For textures spanning the whole UV space, seams along segment borders usually show even when the source texture is seamless; the Normalize option removes these seams by keeping the X-coordinates spanning the full 0 to 1 range, though it adds a distortion effect you may need extra nodes to counter if it's unwanted. For some textures a more rounded look near segment borders helps, achieved by raising the Roundness input.

### Radial Tiling Node

This node segments a 2D cartesian coordinate space into radial sections based on the Sides parameter. Each section contains its own affinely transformed local coordinate system for radially symmetric texture tiling.

### Inputs

Vector
The input vector representing the coordinate system to divide.

Sides
Count of radial sections. Non-integer values create an irregular final section smaller than regular ones.

| Description | Description | Description | Description |
| --- | --- | --- | --- |
| Sides: 5.0. | Sides: 5.25. | Sides: 5.5. | Sides: 6.0. |

Roundness
Curvature of the segment coordinate systems.

| Description | Description | Description | Description |
| --- | --- | --- | --- |
| Roundness: 0.0. | Roundness: 0.25. | Roundness: 0.5. | Roundness: 1.0. |

### Properties

Normalize
When enabled, X-coordinates of Segment Coordinates are remapped to a 0.0–1.0 range and a constant 1.0 is added to Y-coordinates, ensuring non-negative output ranges.

| Description | Description |
| --- | --- |
| Normalize: Disabled. | Normalize: Enabled. |

### Outputs

Segment Coordinates
Local coordinates for texture mapping within each section.

Segment ID
Distinct identifier for each section, starting at 0 and incrementing counterclockwise.

Segment Width
Relative size of each section. Useful for scaling textures to fit segment dimensions.

Segment Rotation
Counterclockwise rotation angle of each section coordinate system. Useful for aligning texture rotation per section.

[Related references](INDEX.md).
