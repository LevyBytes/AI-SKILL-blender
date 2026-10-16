# Path Animation

## Path Animation

Path Animation settings govern how child objects move along a path.

Note

This feature is deprecated but still available.
A more sustainable method is the Follow Path Constraint.

Path Animation panel. 

Frames
Count of frames needed to complete the path,
setting the maximum Evaluation Time value.

Evaluation Time
Parametric position on the curve length (divided by Frames to get the actual position).
Defaults to the global frame number,
but can be keyframed for custom control.

Clamp
Prevent curve path children from travelling past the start/end points.

Follow
Rotate curve path children to align with the path's curvature.

Example:

This example shows Path Animation setup .

- Build something to animate plus a path for it to travel along.
Here the Monkey and the Bézier Circle stand in for those.

- Bind the monkey onto the Bézier circle: click the monkey first and the curve second
(which leaves the curve active), then press Ctrl - P and choose Follow Path .
That keyframes Evaluation Time on its own and switches Follow on within
the Path Animation panel.

- Pick the monkey and
Clear Origin to remove its offset.

- Adjust the monkey's orientation by changing
the Tracking Axis.

| Description | Description |
| --- | --- |
| Monkey parented to the Bézier Circle.  | The final result.  |

[Related references](INDEX.md).
