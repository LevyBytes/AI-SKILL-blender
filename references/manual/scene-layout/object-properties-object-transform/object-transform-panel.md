# Transform: Object Mode, Properties ‣ Object Properties ‣ Transform

### Transform 

Reference

Mode:
Object Mode

Panel:
Properties ‣ Object Properties ‣ Transform

Panel:
3D Viewport ‣ Sidebar ‣ Transform

Transform Options. 

The Transform area in the Sidebar lets you view and
hands-on/numerically manage the placement, rotation, and other details of an item, in Object Mode.
Every item saves its placement, heading, and proportions.
These might require manual adjustment, resetting, or baking.
In Edit Mode. It chiefly lets you type exact spots for a corner,
or averaged location for a corner grouping (including a line/surface). Because each object class gets distinct
entry in its Transform area in Edit Mode,
examine their respective sections in the Modeling part.

Employ this area to examine or alter the item's transform values like position,
turning, and/or sizing. These numbers change the item's anchor and then impact the look of
every corner and surface.

Location
The item's anchor position in item-relative directions.

Rotation
The item's direction, relative to the world directions and its own anchor.

Rotation Mode
System for determining rotations, more material can be in
the appendix.

Euler:
The gizmo lines stick to the Euler direction,
giving you a view of the underlying XYZ direction in the Euler spin,
plus feasible Gimbal effects.

Axis Angle:
The X, Y, and Z values denote a spot from the item origin.
This spot and the origin establish a line around which the W setting establishes the turn.

Quaternion:
X, Y, Z, and W reflect the Quaternion features.

Scale
The item's comparative proportions along the item direction
(e.g. the Scale X value mirrors the proportions along the item X direction).
Every item (block, ball, etc.), when made, has a proportions of unit in every item direction.
To make the item bigger or tinier, you enlarge or minimize it in the target direction.

Dimensions
The area of the item's perimeter box
(arranged with the item directions – consider a mailing carton just roomy enough to hold the item).

Transform Properties Locking
While toggled, the corresponding transform number
stays unchanged in interactive procedures.
But the number can alter through non-interactive procedures,
like hand-entering the number or executing Python.

As a case, if you tied the Location X setting
you are unable to employ the viewport gizmo to shift the item across the world X line.
Still you can shift it by keying the Location X number area.
Think of the tie choice as a firm constraint, modifiable just from the area.

To tie a setting, tap the padlock image next to the key.
The button is unlocked when the image exhibits an undone padlock,
and it is locked when the image shows a done padlock.

[Related references](INDEX.md).
