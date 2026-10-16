# Introduction: Selection Modes, Switching Selection Mode, Multiple Selection Modes, Expand/Contract Selection, X-Ray

### Selection Modes

Reference

Mode :

Edit Mode

Menu :

3D Viewport Header ‣ Select Mode

Shortcut :

1 , 2 , 3
( Shift Multiple Selection Modes,
Ctrl Expand/Contract Selection)

Edit Mode gives you three selection modes, Vertex, Edge, and Face. Switch among them with the header button in the 3D Viewport or the shortcut key.

Selection mode buttons

Vertex 1
Here vertices appear as dots, black when unselected, orange when selected, and white for the active one.

Edge 2
Here vertices are hidden. Edges show black when unselected, yellow when selected, and white for the active edge.

Face 3
Here selected faces fill with orange, and the active face also gets a white border.

| Description | Description | Description |
| --- | --- | --- |
| Vertex mode example.  | Edge mode example.  | Face mode example.  |

### Switching Selection Mode

Moving "up" the ladder, from Vertices to Edges or Edges to Faces, keeps the old selection only where it forms a whole element in the new mode.

So with all four of a face's edges selected, going from Edges to Faces keeps that face; any edges short of a full face fall away.

Going "down," everything stays selected. Select a face and switch to Edge mode, for instance, and all four of its edges come along.

| Description | Description |
| --- | --- |
| Selection in Edge mode.  | Switching to Face mode.  |

### Multiple Selection Modes

Hold Shift as you switch and several modes can run at once.

### Expand/Contract Selection

Holding Ctrl while moving to a "higher" mode expands the selection, fully taking in elements of the new mode that were only partly covered before.

| Description | Description |
| --- | --- |
| Selection in Vertex mode.  | Switching to Edge mode while holding Ctrl.  |

Holding Ctrl into a "lower" mode does the reverse, contracting the selection by dropping new-mode elements that have any unselected neighbor.

### X-Ray

X-Ray shading lets you both see hidden geometry and select it. The trade-off: you can no longer click a face anywhere on its surface, only on the selection dot at its center.

| Description | Description |
| --- | --- |
| X-ray enabled.  | X-ray disabled.  |

[Related references](INDEX.md).
