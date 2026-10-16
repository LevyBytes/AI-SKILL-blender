# Shear

## Shear

### Shear

Reference

Mode:

Object and Edit Mode

Tool:

Toolbar → Shear

Menu:

Object/Mesh/Curve/Surface → Transform → Shear

Shortcut:

Shift - Ctrl - Alt - S

Shearing deforms selected geometry by moving upper vertices left and lower ones right (or vice versa) relative to the Pivot Point. Vertices further from the pivot shift more. The outcome: vertical edges become slanted while horizontal ones remain unchanged.

### Usage

### Tool

Set up a pivot point and optionally a transform orientation.
Choose an axis on the gizmo matching the "above"/"below" direction (controlling how much each vertex shears). Then drag the handle matching the "horizontal" direction (where vertices move).

Using the Shear tool.

### Operator

Set a pivot point, then select from the menu or press the shortcut.
Drag left or right to shear, then hit LMB to confirm.

By default, "above," "below," and "horizontal" use the current viewport plane, but options can alter this.

Using the Shear operator with different pivot points.

### Options

Angle
How much to "rotate" vertical edges.

Axis
The axis perpendicular to the shearing plane. For instance, when vertices travel along X and distance is measured from the pivot along Y, set Axis to Z.

Axis Ortho
The axis along which vertices slide. Must differ from Axis.

Orientation
The Transform Orientation from which to select Axis and Axis Ortho.

Mirror Editing
Whether to affect corresponding geometry on the opposite mesh side.
Mesh Symmetry must be active.

Proportional Editing
See Proportional Editing.

[Related references](INDEX.md).
