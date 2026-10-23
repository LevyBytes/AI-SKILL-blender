# Proportional Editing

## Proportional Editing

Reference - Mode: Object and Edit Mode. Location: Header ‣ Proportional Editing. Shortcut: O.

Proportional Editing transforms your current selection while also pulling along the unselected geometry around it. Influence drops off with distance — the more remote an unselected element is, the smaller the effect it receives (which is where the name comes from). It shines when you need to deform dense meshes gently.

Note: Blender's Sculpting workflow is an alternative, offering brushes and tools that proportionally reshape a mesh without exposing the individual vertices.

Controls:
Disable (O): the feature is off and only the selected vertices respond.
Enable (O): geometry beyond the selection is affected too, out to a set radius.

Proportional Size: during a transform you can grow or shrink the tool's reach from the Proportional Editing popover, or with WheelUp / WheelDown, or PageUp / PageDown. As the radius changes, the points around your selection reposition to match.

Falloff: mid-edit you can swap the curve profile either by clicking the Falloff icon in the header or by pressing Shift-O for a pie menu. The available profiles are Constant (No Falloff), Random, Linear, Sharp, Root, Sphere, Smooth, and Inverse Square.

Object Mode: although Proportional Editing lives mostly in Edit Mode, it works in Object Mode as well, where it acts on whole objects instead of individual mesh components. In the illustrated case the leftmost cylinder is being scaled upward, and the cylinders beside it are pulled along too.

Edit Mode: on heavy geometry, nudging things subtly without leaving visible bumps and ridges in the surface is hard, and that is exactly where Proportional Editing earns its keep.

Options:
Connected Only (Alt-O): rather than relying on a plain radius, the falloff propagates through linked geometry. That lets you proportionally edit the vertices of one finger on a hand without disturbing the neighboring fingers: those other vertices are near in 3D space yet distant when you follow the mesh's edge connectivity. The icon shows a blue center while Connected is active, and the mode exists only in Edit Mode.
Projected from View: distance along the viewing direction is disregarded when the radius is applied.

Example: the sample render of a low-poly landscape was produced simply by raising the vertices of a triangulated grid with Proportional Editing turned on.

[Related references](INDEX.md).
