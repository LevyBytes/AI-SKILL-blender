# Screw: Creating a Screw Spindle, Creating a Screw Tip

### Creating a Screw Spindle 

For helices with no gaps between turns, the Screw operator is a natural fit.

- Open Blender and enter Edit Mode for the default cube.

- Delete all vertices by pressing X or Delete .

- Switch to the Front Orthographic view by pressing Numpad1 .

- Click Ctrl - RMB three times to create a profile like the one below.

- Select the two vertices closest to the global Z axis and press S X 0 Return
to ensure they have the same X coordinate.

- Select all three vertices and click Edge ‣ Screw .

- Adjust the Steps and Turns to your liking.

| Description | Description |
| --- | --- |
| Profile for a screw spindle.  | Result after running the Screw operator.  |

More elaborate forms work too, such as this spiral "staircase":

| Description | Description |
| --- | --- |
| Profile.  | Generated mesh.  |

### Creating a Screw Tip 

So far the profile's first and last vertex have always shared an X coordinate, which holds the
helix at a constant radius. Nothing forces that, though — feed in differing X coordinates and the
helix tapers or flares as it climbs.

| Description | Description |
| --- | --- |
| Profile.  | Generated.  |

[Related references](INDEX.md).
