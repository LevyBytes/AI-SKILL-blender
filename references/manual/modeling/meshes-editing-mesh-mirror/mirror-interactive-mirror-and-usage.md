# Mirror: Interactive Mirror, Usage, Options, X/Y/Z Global

## Mirror

### Mirror 

### Interactive Mirror 

Reference

Mode :

Object and Edit Modes

Menu :

Object/Mesh/Curves ‣ Mirror ‣ Interactive Mirror

Shortcut :

Ctrl - M

The Mirror operator flips the chosen elements about the Pivot Point along an axis of the
Transformation Orientation. It amounts to scaling the selection by -1 along that axis, only it
gives you a quicker, more direct workflow.

Hint

After mirroring a mesh, the face normals tend to get flipped inside out
(see the Face Orientation overlay).
The Flip Normals operator can fix this.

See also

- The Symmetrize operator creates a mirrored
copy of the mesh.

- The Mirror Modifier creates a mirrored copy that's
automatically kept up to date.

### Usage 

- Place the pivot point at the desired mirror location.

- When not mirroring along a global axis, ensure the transform orientation has an axis
pointing along the desired mirror direction (perpendicular to the mirror plane).

- Press Ctrl - M to activate the Mirror operator.

- Choose an axis by dragging with MMB or by pressing X , Y , or Z .
(The chosen axis is shown at the top of the 3D Viewport.) Press an axis key a second
time to toggle between the transform orientation axis and the global axis.

- Press LMB or Return to confirm, or RMB or Esc to cancel.

### Options 

Orientation
The transform orientation to take the Constraint Axis from.

Constraint Axis
Which axis or axes to mirror across. Mirroring across X, for instance, flips the selection
horizontally.

### X/Y/Z Global 

Reference

Mode :

Object and Edit Modes

Menu :

Object/Mesh/Curves ‣ Mirror ‣ X/Y/Z Global

These run a non-interactive mirror along the global X, Y, or Z axis.

[Related references](INDEX.md).
