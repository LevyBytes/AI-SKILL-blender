# Draw Brushes: Advanced, Stroke, Post-Processing, Randomize, Stabilize Stroke, Cursor

### Advanced

Spacing
Sets the smallest gap allowed between stroke points, given as a percentage of the brush size.

Low spacing pays off during fast strokes. A quick movement would ordinarily yield few samples and wide gaps; dropping the spacing percentage forces extra points so the minimum gap holds.

Draw slowly and the points already come thick, so the spacing setting adds nothing new. It merely guarantees a minimum gap and never deletes points.

Active Smooth
Number of smoothing passes applied to the stroke as you draw.

Angle
Heading of the input device that yields the thickest stroke (0° means horizontal).

Factor
How much thickness drops off when the stroke runs perpendicular to the Angle value.

Hardness
Alpha falloff from a point's edge in toward its center. Only takes effect with stroke materials of Dot or Box style.

Aspect X, Y
Sets the width and height of the alpha gradient.

### Stroke

#### Post-Processing
Steps that fire on the strokes the moment you finish, right as the LMB or Pen tip lifts. Toggle the whole set with the checkbox in the section panel header.

Smooth
How strongly point positions get smoothed along the stroke.

Iterations
Count of smoothing passes run over the stroke.

Subdivision Steps
Count of subdivisions added to freshly made strokes.

Simplify
Trims the final point count via an adaptive algorithm.

Trim Strokes End
Clips intersecting stroke ends on its own.

Outline
Switches on conversion of a freshly made stroke into its outline.

Material
The material the outline stroke uses.

Thickness
The thickness the outline stroke uses.

#### Randomize
Throws the stroke's points around for a randomized feel. The checkbox in the section panel header toggles Randomize.

Radius
How far randomness leans on the input device's pressure.

Strength
How far randomness reaches the stroke's strength value (alpha).

UV
How far randomness reaches the UV rotation.

Hue, Saturation, Value
Scatters the hue, saturation, and value of the stroke's Color.

Jitter
How much jitter gets mixed into the stroke.

Common Options

Stroke Random
Use randomness only at stroke level.

Use Pressure
Stylus pressure drives the effect's strength, and a curve widget shapes the pressure response.

#### Stabilize Stroke
By holding back and nudging point placement, Stabilize Stroke cuts jitter out of your strokes as you draw. Toggle it with the checkbox in the section panel header.

Radius
Smallest distance from the last point before the stroke carries on.

Factor
A smoothing factor; raise it for smoother strokes, though drawing starts to feel as if you are dragging the stroke behind you.

### Cursor

The checkbox in the Cursor header turns the cursor off.

Show Fill Color while Drawing
Displays, in the viewport, the material color the brush is bound to.

[Related references](INDEX.md).
