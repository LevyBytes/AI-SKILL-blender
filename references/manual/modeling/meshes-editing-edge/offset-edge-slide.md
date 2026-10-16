# Offset Edge Slide

## Offset Edge Slide

### Offset Edge Slide 

Reference

Mode :

Edit Mode

Menu :

Edge ‣ Offset Edge Slide

Shortcut :

Shift - Ctrl - R

Wraps each selected edge with a pair of fresh flanking edges.

### Usage 

- Select one or more edges.

- Click the menu item or press Shift - Ctrl - R .

- Drag the cursor rightward to widen the gap or leftward to narrow it.
Holding Shift slows the motion down for finer control.

Alternatively, type a number.

- Press LMB or Return to confirm.

| Description | Description | Description |
| --- | --- | --- |
| Edges selected.  | Surrounding edges created.  | Cap Endpoint enabled.  |

### Options 

While running, the Factor shows above the 3D Viewport and the shortcuts appear in the status
bar. Once you confirm with LMB , everything stays adjustable in the Adjust Last Operation panel.

Cap Endpoint
Builds triangles wherever an edge chain ends.

Factor
How far across the flanking faces the new edges get placed, as a relative amount.

Even E
Switch this on and the new vertices sit at a fixed absolute gap from the edge chain or its
flanking edges, rather than a proportional one.

Flipped F
Toggles whether the shape follows the edge chain or the flanking edges while Even is on.

| Description | Description |
| --- | --- |
| Even enabled.  | Even and Flipped enabled.  |

Clamp Alt or C
Holds the fresh edges back from the faces beside them, blocking any slide past those faces.

Mirror Editing
With this checked, sliding the new edges drags any existing edges on the mesh's far side along
too. Mesh Symmetry must be enabled for this.

Correct UVs
Assigns the new vertices UVs that match where they land on the mesh. Leave it unchecked and the
new vertices simply inherit the UVs of the edges you originally picked.

[Related references](INDEX.md).
