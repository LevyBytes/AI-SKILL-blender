# Cameras: Lens

### Lens 

Type

These options decide the way solid 3D shapes get flattened into the 2D frame.

Perspective
This is the look the eye gives you day to day.
Far-off things shrink against near ones, and parallel rails seem to draw together with distance.

Focal Length/Field of View
Think of Focal Length as zoom: it fixes how much scene the frame holds at once.
Crank the length up for a tighter FOV and more zoom; shorten it to fit more scene in
(larger FOV , less zoom).

| Description | Description |
| --- | --- |
| Perspective camera with 35 mm focal length.  | Perspective camera with 210 mm focal length instead of 35 mm.  |

Lens Unit
State focal length either in millimeters or straight as the Field of View angle.

Hint

Pull Focal Length down while closing on a subject and you get a Dolly Zoom; push it up to reverse the effect.

This video demonstrates the Dolly Zoom camera effect.

Orthographic
Here every object keeps its real size whatever its distance from the camera.
Parallel lines stay parallel as a result, never meeting the way Perspective makes them.

Render from the same camera angle as the previous examples, but with orthographic perspective. 

Orthographic Scale
This dials the on-image size of the projected objects.

It is essentially the only knob orthographic perspective responds to.
With no vanishing points in this mode (parallel lines never meet), shifting the lens just mimics sliding the camera in the 3D Viewport.

Panoramic
Cycles Only

This single type gathers a whole assortment of panoramic projections.
See the Cycles panoramic camera settings for more information.

Custom
Cycles Only

The Custom type hands camera behavior over to your own OSL code.
See the Cycles custom camera documentation for more information.

Shift
Your handle on the vanishing points .
That term names the spot where parallel lines look like they meet.
The railroad's far end is the standout vanishing point throughout these examples.

| Description | Description |
| --- | --- |
| Horizontal lens shift of 0.330.  | Rotation of the camera object instead of a lens shift.  |

See how shifting the lens leaves horizontal lines dead level, whereas turning the camera body tilts them.

Note

Shifting the lens comes to the same thing as rendering a wider FOV and trimming the result off-center.

Clip Start and End
The band over which objects are drawn directly.
Whatever sits past it still tints the picture indirectly, since later light bounces escape clipping.

Note

Capping these distances counts in viewport rendering: it preserves enough rasterization precision.
Ray traced output shrugs the issue off, so it stomachs far wilder values.

Tip

Turn on Limits under Viewport Display and the clip bounds appear as two joined yellow dots running along the camera's sightline.

See also

- 3D Viewport clipping

[Related references](INDEX.md).
