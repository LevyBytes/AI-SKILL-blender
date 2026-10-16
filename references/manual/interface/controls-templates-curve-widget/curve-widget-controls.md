# Curve Widget: Controls

### Controls
Zoom In
Magnifies for finer detail and tighter control. While zoomed, pan around the curve by clicking and dragging with LMB over an empty spot.

Zoom Out
Pulls back for less detail and a whole-curve view. The clipping region is the limit — you can't zoom past it (see Clipping below).

Reverse Path Profile Curves
Mirror the curve around the diagonal.

Clipping Options Mapping Curves

Use Clipping
Pins curve points within the values you give.

Min X/Y and Max X/Y
Fix the lower and upper bounds the curve points may reach.

Specials

Reset View
Zooms the view fully out.

Extend Options Mapping Curves
Governs how the curve carries on past its first point and beyond its last.

Extend Horizontal
Makes the curve "go flat."

Extend Extrapolated
Keeps the curve heading in its current direction.

| Description | Description |
| --- | --- |
| Extend Horizontal. | Extend Extrapolated. |

Reset Curve
Returns the curve to default, clearing every point you added.

Handle Type
The selected control point's handle type, which governs the shape the curve takes through that point.

Auto Handle
Yields a smooth curve with no manual handle setup needed.

Vector Handle
Yields straight lines meeting at a sharp corner.

Free Handle Profile Curves
Exposes Bézier handles you can move freely and apart from one another, which may leave a sharp corner at the point.

Aligned Free Handles Profile Curves
Exposes freely movable Bézier handles tied to face in opposite directions, keeping the curve smooth through the point.

Auto Clamped Handle Mapping Curves
Like Auto Handle, but with overshoot held in check too.

| Description | Description | Description |
| --- | --- | --- |
| Vector Handles. | Auto Handles. | Auto Clamped Handles. |

X, Y
The coordinates of the selected control point.

Delete X
Drops the selected control point. The endpoints — first and last — stay put.

Copy/Paste Ctrl - C , Ctrl - V
Hover over a Curve Widget and press Ctrl - C , Ctrl - V to carry the entire curve across to another.

Presets Brush Curve Widgets Only
A set of preset curves you can snap the curve to. What shape each yields turns on whether the property's default curve slopes up or down.

| Smooth | Round | Root |
| --- | --- | --- |
| Sharp | Linear | Constant |

| Smooth | Round | Root |
| --- | --- | --- |
| Sharp | Linear | Constant |

[Related references](INDEX.md).
