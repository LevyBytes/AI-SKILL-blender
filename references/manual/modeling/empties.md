# Empties

## Empties

An empty is a position marker in space with no geometry. It renders invisibly but serves as a control anchor.

Empty Display Types.

Plain Axes: Six lines extending along each axis (±X, ±Y, ±Z).
Arrows: Three labeled arrows along the positive X, Y, Z axes.
Single Arrow: One arrow pointing along +Z.
Circle: A circle initially in the XZ plane.
Cube: A cube aligned to the coordinate axes.
Sphere: Three circles (one per axis) forming an implied sphere.
Cone: A cone initially pointing along +Y.
Image: Empties can hold images. Use this for reference artwork, blueprints, or figure sheets for modeling.
The image displays regardless of rendering mode.

Access Empty display options via Properties ‣ Object Data ‣ Empty panel.

Offset X, Y: Move the image anchor (1.0 = image width/height).

X=0.5, Y=0.5: Anchor at image center.
X=0.0, Y=0.0: Anchor at bottom-left.
X=1.0, Y=1.0: Anchor at top-right.

Depth:

Default: Standard depth behavior.
Front: Always appear in front.
Back: Always appear behind.

Tip: For a reference image, set Depth to Front and lower Opacity.

Side:

Both: Show front and back.
Front: Show only the front.
Back: Show only the back.

Tip: When using reference photos from both sides, set each empty to display only from the matching viewpoint.

Show in:

Orthographic: Visible in orthographic projection.
Perspective: Visible in perspective projection.

Hint: Disabling this prevents reference images from obstructing your model.

Only Axis Aligned: Display only when the view aligns with the object's local axes.

Opacity: Blend strength between image and background (0–1).

An empty can only be edited in Object Mode, covering transformation and parenting. Other tools appear in the Object section.

Apply Scale Ctrl+A

Empties lack traditional object data, so "apply scale" works differently. Instead, the Display Size property controls the visual size (before scaling). The scale on the most-stretched axis combines with Display Size to maintain correct proportions on that axis.

Display As: Which empty primitive to show in the viewport.
Size: Scales the visual size of the empty (offset, not transform).

Empties serve as deformation handles. Common uses:

Parent object for a group: An empty can parent other objects, allowing centralized control without render impact.

Target for constraints: Use an empty as a constraint anchor. For example, a camera can track a point via a Track To constraint.

Array offset: An empty can drive an Array Modifier, enabling complex transformations through single-object movement.

An example of an empty controlling an array. ‣ An example of an empty driving a Track To constraint. ‣

Other applications:
- Placeholders for missing objects
- Rigging anchors
- Depth-of-field markers
- Reference images

[Related references](INDEX.md).
