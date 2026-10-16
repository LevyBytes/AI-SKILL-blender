# Mirror: Interactive Mirror, Usage, Properties

### Mirror 

### Interactive Mirror 

Reference

Mode:
Object and Edit Modes, Video Sequencer Preview

Menu:
Object/Mesh/Curves/Strip ‣ Mirror ‣ Interactive Mirror

Shortcut:
Ctrl - M

The Mirror operation flips the picked geometry around a given axis.
This is functionally equal to scaling the selection by -1 in that direction,
though provides a quicker and more user-friendly method.

When mirroring sequencer strips, the axis mirror value changes rather than applying -1 scaling.
Positioning and rotation shift to achieve the same visual outcome as object mirroring.

The operation references the selected Transformation Orientation
and Pivot Point
For complete flexibility, you can:

- Relocate the pivot point to any position for symmetry control.

- Pick a transformation orientation (such as Global, Local, or Normal).

- Designate which axis (X, Y, or Z) to flip across.

Tip

For non-destructive flipping, apply the Mirror Modifier instead.

### Usage 

To perform a flip along a particular axis:

- Hit Ctrl - M, followed by X, Y, or Z to choose the axis.

- Press the same key again to alternate between the selected Transform Orientation and global space.

- Hold MMB and move the mouse to interactively adjust the flip direction.

### Properties 

Orientation
The Transform Orientation governing how the X, Y, and Z directions are positioned.

Constraint Axis
Determines which axis/axes receive the flip.
As an illustration, using the X axis flips the selection side-to-side.

[Related references](INDEX.md).
