# Screw: Options, Examples, Creating a Spring

### Options 

Screw panel (in Edit Mode). 

Steps
The number of extrusions to be done for each 360° turn.

Turns
The number of turns to create.

Center X, Y, Z
World-space coordinates of the pivot the geometry revolves around. It starts out at the 3D
Cursor's location.

Axis X, Y, Z
The direction vector the geometry spins about. It begins as the screen's vertical axis — so the
global Z in a side view, or the global Y in a top view. Flip the Axis to swap between clockwise
and counterclockwise.

Tip

You can use the Align View to Active
menu item to align the viewport, and thereby the Axis , to a certain item
in the scene.

Keep in mind the Axis governs only the "horizontal" spin around the centerpoint, not any
"vertical" travel. That vertical motion always follows the distance and direction set by the open
profile's endpoints, heading downward in the object's local space.

### Examples 

### Creating a Spring 

Start with a circle for the spring's cross section:

- Open Blender and delete the default Cube.

- Add a circle by pressing Shift - A and selecting Mesh ‣ Circle .

- Set the Location X property of this new object to -3 and its Rotation X property to 90°.

- Enter Edit Mode by pressing Tab .

- Switch to the Front Orthographic view by pressing Numpad1 .

Extrusion profile created. 

Now add a vertical line that sets how far apart the spring's loops sit:

- Deselect all vertices by clicking on an empty space or pressing Alt - A .

- Click Ctrl - RMB twice to create two vertices connected by an edge.

- Select both vertices and press S X 0 Return to ensure they have the same X coordinate.
(This is necessary to keep the spring's radius constant.)

Guide profile created. 

The spring is ready to build:

- Select both the circle and the line by pressing A .

- Click Edge ‣ Screw .

- Adjust the Steps and Turns to your liking.

- Try changing Axis Z to -1 and see that this makes the spring turn the other way.

| Description | Description |
| --- | --- |
| Counterclockwise direction.  | Flipped to Clockwise direction.  |

A diagonal Axis yields curious shapes: for instance, hold Axis Z at -1 and set Axis X to 1.
Each loop then tilts 45°, yet the loops still march straight down the guide line's direction
from one to the next.

[Related references](INDEX.md).
