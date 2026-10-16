# Inset Faces

## Inset Faces

### Inset Faces 

Reference

Mode :

Edit Mode

Tool :

Toolbar ‣ Inset Faces

Menu :

Face ‣ Inset Faces

Shortcut :

I

This rings the selected faces with a border of faces, then lets you set that border's thickness
by dragging the cursor. As the border fattens, the outermost selected faces thin out while the
inner ones hold their size.

You can also change the inset's depth mid-operation by holding Ctrl . As with Extrude Faces Along
Normals, this slides each selected vertex along its normal and may resize every face.

When the inset looks right, press LMB or Return to confirm. RMB or Esc cancels it.

| Description | Description | Description |
| --- | --- | --- |
| Faces selected.  | First inset using only Thickness.  | Second inset using only Depth.  |

Several disjoint "patches" of faces can also be inset at once.

### Options 

Inset operator options. 

The shortcuts below work while insetting and also appear in the status bar.

Boundary B
Also build border faces along boundary edges — those belonging to one face rather than two.

Offset Even
Keeps the border an even width along the edges. Switch it off and the width is even at the
corners instead.

| Description | Description |
| --- | --- |
| Offset Even enabled (default).  | Offset Even disabled.  |

Offset Relative
Scales each border vertex's Thickness and Depth offset by the mean length of its two neighboring
border edges.

Edge Rail
Snaps the new edges between border faces onto the existing edges between the inset faces.

| Description | Description |
| --- | --- |
| Edge Rail disabled.  | Edge Rail enabled.  |

Thickness
How wide the fresh border faces come out.

Depth Ctrl
How far up or down the inset faces shift.

Outset O
Grows the new border outward rather than inward.

Select Outer
Moves the selection onto the freshly made border faces.

Individual I
Insets each face on its own, instead of treating a connected patch as a single unit.

Interpolate
Carries mesh data — UVs, Color Attributes, vertex group weights, and so on — over to the new
border vertices.

[Related references](INDEX.md).
