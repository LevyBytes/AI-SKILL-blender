# Animation Tools: Interpolate Sequence, Bake Object Transform to Grease Pencil

### Interpolate Sequence

Reference

Mode :

Draw Mode, Edit Mode

Menu :

Grease Pencil ‣ Interpolate Sequence

Shortcut :

Shift - Ctrl - E

Bridges the surrounding keyframes by generating strokes across the frames between them. A breakdown keyframe lands on every frame separating the previous keyframe from the next.

Step
Frame gap between generated interpolated frames.

Layer
Layers taken into the interpolation.

Exclude Break Downs
Keep existing Breakdown keyframes from serving as interpolation extremes.

Flip Mode
Reverse the destination stroke so its start and end line up with the source stroke.

Smooth
How much smoothing the interpolated strokes get, to trim jitter and noise.

Iterations
Count of smoothing passes over the freshly made strokes.

Type
Which interpolation method applies on the next Interpolate Sequence run.

### Bake Object Transform to Grease Pencil

Reference

Editor :

3D Viewport

Mode :

Object Mode

Menu :

Object ‣ Animation ‣ Bake Object Transform to Grease Pencil

Takes all Object-level transform animation across a chosen frame range and writes it into Grease Pencil object keyframes.

Start Frame, End Frame
Where the baking process starts and stops.

Step
Frame stride for the baking process.

Only Selected Keyframes
Convert only the selected keyframes.

Target Frame
Where the baked animation lands.

Projection Type
Picks the projection type for the converted strokes.

[Related references](INDEX.md).
