# Toolbar

## Toolbar

The Toolbar holds a list of tools. Links to each mode's Toolbar follow.
Object Mode: Object Mode.
Edit Mode: Mesh Edit Mode, Curve Edit Mode, Surface Edit Mode, Metaball Edit Mode.
Paint Modes: Sculpt Mode, Texture Paint Mode, Vertex Paint Mode, Weight Paint Mode.
Grease Pencil: Grease Pencil Edit, Grease Pencil Draw, Grease Pencil Sculpting, Grease Pencil Weight Paint.

Selection tools:
Tweak — select or move.
Select Box — select strips by dragging a box; every strip the box touches is selected.
Select Circle — select strips by dragging a circle; every strip the circle's path touches is selected.
Select Lasso — select strips by drawing a lasso.

Blade — cuts a strip in two: it first trims the strip to show only the content up to the cut, then adds a second strip showing the content after it. The Blade tool handles both point cuts and a box gesture for swiftly clearing unwanted strip sections. You can split in these ways:
- Choose the tool in the Toolbar, then click a strip wherever you want the split.
- Click and drag a box; everything inside it is sliced out and deleted.
With the box gesture, everything inside the box area is deleted. With Remove Gaps on, strips after the removed section move backward in time to close the gap (ripple). When rippling, this applies to every channel the box crosses; channels the box doesn't cover stay put, letting other strips keep their relative timing if you like. If the box starts at a strip's beginning or end, the ripple amount comes from the distance between the strip handle and the box's time-side, and when the box spans gaps between strips, those gaps can be removed when rippling too.
Tool Settings:
Type — the split type for point-based cuts. Soft (you can still restore the cut content in the new strips by dragging their handles) or Hard (you can't restore it by dragging handles, though it can still be recovered via the Hold Offset in the Sidebar).
Remove Gaps — in box blade mode, closes the gaps left between cut strips and ripples following strips earlier in time; hold Shift before dragging to skip this briefly and keep the gap.
Ignore Selection — in box blade mode, cuts every strip inside the box, selected or not.
Ignore Connections — keeps the cut from propagating to connected strips, such as effect strips.

Slip — moves only a strip's content. By default it only lets the content move within the strip handles; while that limit is in force the strip outline is drawn red, and pressing C toggles the limiting on or off.

[Related references](INDEX.md).
