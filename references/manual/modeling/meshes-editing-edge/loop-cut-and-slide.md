# Loop Cut and Slide

## Loop Cut and Slide

### Loop Cut and Slide 

Reference

Mode :

Edit Mode

Menu :

Edge ‣ Loop Cut and Slide

Shortcut :

Ctrl - R

This divides a run of faces into two or more parallel loops. By default the fresh edges land
midway, though you're free to nudge them off toward either side.

### Usage 

You drive the tool through two interactive stages:

- Choose the face loop to cut

With the tool running, hover over an edge the cut should pass through — meaning one that runs
crosswise to the cut. A yellow preview line marks where the cut will fall. Press LMB to lock it
and continue, or RMB to abort.

- Slide the new edge loop(s)

Drag the cursor to reposition the freshly added loop. LMB drops the cut where you've placed it,
while RMB drops it dead center.

| Description | Description | Description |
| --- | --- | --- |
| Mesh before inserting edge loop.  | Choosing the face loop.  | Sliding the new edge loop.  |

See also

The Edge Slide tool for sliding existing edge loops.

### Options 

The following can be set live during the tool, and again afterward via the Adjust Last
Operation panel.

Number of Cuts Wheel
In the first stage, dial the cut count up or down by scrolling Wheel , typing a figure,
or hitting PageUp / PageDown .

| Description | Description |
| --- | --- |
| Preview of multiple edge loops.  | Result of using multiple cuts.  |

Smoothness
Pushes the new edges along their normals to keep the surface's curve. Alt - Wheel changes this
in the first stage, but since you get no preview there, it's usually cleaner to tweak it later
in the Adjust Last Operation panel.

| Description | Description |
| --- | --- |
| Added edge loop without smoothing.  | Same edge loop, but with smoothing value.  |

Falloff
Falloff type for Smoothness . Changes the shape of the profile.

Factor
Position of the edge loop relative to the surrounding ones.

Even E
Gives the new loop a uniform gap from one neighboring loop, rather than a gap scaled to the
length of each crosswise edge it cuts. Tap E during the second stage to flip it on or off.

Flipped F
Holds the Even gap against the opposite adjacent edge instead. Tap F during the second
stage to toggle.

| Description | Description | Description |
| --- | --- | --- |
| Cut with Even disabled.  | Cut with Even enabled. The red dot shows the side to which an even distance is kept.  | Cut with Even and Flipped enabled.  |

Clamp C
Uncheck this and the new loop is allowed past the boundary edges of the face loop.
Press C , or hold Alt , during the second stage to toggle it.

Mirror Editing
With this checked, sliding the new edges drags any existing edges on the mesh's far side along
too. Mesh Symmetry must be enabled for this.

Correct UVs
Leave this unchecked and the UV-map faces split evenly even when the 3D cut sits off-center.

[Related references](INDEX.md).
