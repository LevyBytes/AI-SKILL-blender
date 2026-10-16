# Numeric Input

## Numeric Input

### Numeric Input 

Mouse control is convenient for transforms, but precise adjustments need exact values. After triggering a command, enter a number
to set the transformation strength. Then finalize or undo.
E.g. pressing S 2, Return will multiply the scale by two.

Move G
By default with no additions, movement occurs along the X axis.

Rotation R
Positive angles rotate counterclockwise.

Scale S
Sizing behaves much like moving.
The main difference is that by default, scaling applies to all three dimensions evenly.

You can monitor the numbers in the viewport footer.

Numeric input shown in the footer. 

Tip

Numerical values can also be set in
the sidebar.

### Simple Mode 

Blender supports two "input styles": basic and complex. Basic mode takes whole and decimal numbers.

Decimals Period
Type decimals by pressing Period.

Negate Minus
Reverse the value with Minus.

Reciprocal Slash
Pressing Slash during input flips the number to its opposite,
e.g. 2 / becomes 0.5 (half of 2); 20 / becomes 0.05 (one-twentieth).

Reset Backspace
Hitting Backspace after removing all preceding digits
will first revert the edited value to its starting point, and on a second press,
input ceases and reverts to standard transform with the mouse.

Cycle Components Tab, Ctrl - Tab
For multi-axis values, engage Tab or Ctrl - Tab.
E.g. To move an object a unit along all three directions, type: G 1
and Tab 1 and Tab 1.

Non-number Inputs
Numerical entry combines with
Axis Locking
to restrict movement to one axis or command-specific shortcuts.

### Advanced Mode 

Advanced mode allows you to type formulas and unit notations.

Press = or NumpadAsterisk to start advanced mode,
and Ctrl - = or Ctrl - NumpadAsterisk to switch back to simple mode.

Capabilities include:

- Notation ( cm, ", deg, etc.)
.
Reference unit system.

- Fundamental Python operations ( +, *, /, **, etc.)

- Math keywords and routines ( pi, sin, sqrt, etc.)
.
Reference Python's math package.

You can employ the negate and reciprocal shortcuts ( Minus, Slash),
as well as non-number inputs, but you must press Ctrl.

[Related references](INDEX.md).
