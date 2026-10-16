# Volume Properties: Grids, OpenVDB File

## Volume Properties

### Volume Properties

### Grids

In the List View you'll see each grid that the OpenVDB file holds, together with its name and data type.
A "grid" is a body of volumetric data; usually it records each voxel's density,
though it can just as well hold temperatures, velocities, and so on.

Pick a grid and the volume object switches to showing it.

### OpenVDB File

File Path
Which VDB file gets used.

Sequence
Pulls in extra VDB files, one for every animation frame. Just like image sequences,
each file wants a numbered suffix, so choosing smoke-000.vdb
in the File Path expects a smoke-001.vdb, a smoke-002.vdb, and so on after it.

Frames
How many of the sequence's frames to play through.

Start
The scene frame on which the sequence kicks off.

Offset
How many of the sequence's opening frames to leave out.

Mode
What the volume does before the sequence's opening frame ( Start ) and after its
closing one ( Start + Frames ).

Clip :

Display nothing at all.

Extend :

Hold on the sequence's first or last frame and keep it on screen.

Repeat :

Loop the sequence over and over (and over…).

Ping-Pong :

Run the sequence forward, then in reverse, then forward once more, and so on.

[Related references](INDEX.md).
