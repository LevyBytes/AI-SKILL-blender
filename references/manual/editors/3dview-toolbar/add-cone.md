# Add Cone

## Add Cone

Reference - Mode: Object Mode and Edit Mode. Tool: Toolbar ‣ Add Cone. Drops a cone mesh object into the scene interactively.

Usage: start by dragging with LMB to lay out the object's base; release LMB and slide the mouse to set its height; then click LMB once more to lock in the shape. A few keys can be held to flip a setting for as long as you hold them:
Ctrl: turns snapping on or off.
Alt: switches the Origin setting.
Shift: switches the Aspect setting.

Tool Settings:
Depth: the starting depth (measured from the screen into the scene) used when the object is placed.
  Surface: begins placement on the surface beneath the pointer; with nothing there, it behaves like Cursor Plane.
  Cursor Plane: begins placement on a plane passing through the 3D Cursor, oriented by the Orientation and Plane Axis settings.
  Cursor View: begins placement on a plane through the 3D Cursor that faces the view.
Orientation: the orientation given to the new object: a trio of axes from which Plane Axis selects one.
  Surface: adopts the normal orientation of the surface under the pointer; with no surface, it matches Default.
  Default: adopts the current Transform Orientation.
Snap To: what to target while Snapping.
  Geometry: snaps to every kind of geometry (vertices, edges, faces).
  Default: snaps to whatever the global snapping options specify.
Plane Axis: which of the three Orientation axes (X, Y, or Z) counts as "up" for the object; its base ends up perpendicular to that axis.
Auto Axis: instead of the axis named by Plane Axis, uses the one nearest the viewport's viewing direction (when you aren't hovering a surface).
Base:
  Origin: how the base gets laid out. Edge draws it from one corner across to the opposing corner; Center draws it from the middle out to a corner.
  Aspect: whether the base keeps a free or a fixed aspect ratio. Free lets width and depth be set independently; Fixed forces them equal.
Height:
  Origin: how the height gets laid out. Edge treats the base as the bottom and then you set the top; Center treats the base as the middle and then you set the top.
  Aspect: whether the bounding box's side keeps a free or fixed aspect ratio. Free lets height be set independently of the base; Fixed forces height to match the base's largest side.
Vertices: how many vertices form the base.
Base Fill Type: how the circle at the base is closed off. Triangle Fan fills it with triangles meeting at a central vertex; N-gon fills it with one N-gon; Nothing leaves it open, producing only the outer ring of vertices.

[Related references](INDEX.md).
