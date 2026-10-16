# Tracking Marker

## Tracking Marker

Point: move the whole marker with RMB, or by dragging the anchor point (the black dot) with LMB; pressing G also moves the whole marker, and pressing G twice moves the marker while leaving the anchor in place (an anchor outside the pattern area appears as a cross joined to the marker position by a dashed line). S scales the whole marker, while pressing S twice scales only the pattern area; R rotates the Pattern — depending on the pivot point used, either spinning patterns about their own centers or rotating whole markers about, e.g., the median point. To match a marker's perspective transform on a plane, edit the individual corners by hand: each corner deforms independently to define the shape, and dragging a corner with LMB repositions it.
Note: deforming a pattern isn't only useful for planar/affine tracking — since only the pixels inside the pattern are considered, it can help specify a better pattern to track even for simple position tracking.
The Search area can't be rotated, which is intentional: deforming the search area makes no sense.

Plane: the plane's bottom-left corner carries X/Y axes (X is red, Y is green) to help read the plane's orientation in space. You'll likely need to adjust the plane object's corners by hand — slide individual corners with LMB, or use the general transform tools G, R, S. Adjusting the corners keeps the plane following the plane defined by the tracks it was originally created from.

[Related references](INDEX.md).
