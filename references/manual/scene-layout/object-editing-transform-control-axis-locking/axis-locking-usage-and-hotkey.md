# Axis Locking: Usage, Hotkey, Pointing, Axis Locking Types, Plane Locking

## Axis Locking

### Axis Locking 

Axis locking illustration. 

This toggle narrows transformations to the chosen axis.

Transformations (movement/resizing/rotation)
in Object and Edit Modes (plus extrusions in Edit Mode)
can be limited to a specific axis according to
the active transform orientation.
By confining a transformation to one axis, you restrict movement to a single dimension.

### Usage 

A locked axis displays in higher brightness than an unlocked axis. In the picture on the right,
the Z axis glows brightly since movement is confined to this axis. This state can be achieved in two ways:

### Hotkey 

The axis of operation can switch during a transform by pressing X, Y, or Z.

### Pointing 

Axis constraint in action. 

Pressing MMB after starting a transform lets you select an axis to limit to.
A clickable option to define the translation path is displayed,
showing the three axes in the viewport. A dashed white line indicates direction.
The axis to confirm will be the one highlighted when the MMB is released.

When you've moved in the target direction,
pressing MMB will snap to the highlighted axis.

### Axis Locking Types

### Axis Locking 

Reference

Mode:
Object and Edit Modes (move, rotate, scale, extrude)

Shortcut:
X, Y, Z or MMB after moving the mouse in the target direction.

Axis locking narrows the transformation to a single dimension (or blocks movement along two axes).
A face, vertex, or other selectable thing can only shift,
resize, or rotate along one axis.

### Plane Locking 

Reference

Mode:
Object and Edit Modes (move, scale)

Shortcut:
Shift - X, Shift - Y, Shift - Z or Shift - MMB
after moving the mouse in the target direction.

Plane locking example. 

Plane locking limits the transformation to two dimensions
(or forbids movement along one axis),
establishing a space where the element can shift or resize easily.
Plane locking only influences movement and sizing.

Keep in mind that for turning, both axis and plane locking work identically as a rotation occurs
around one axis only.
Trackball rotations R R cannot be confined in any way.

[Related references](INDEX.md).
