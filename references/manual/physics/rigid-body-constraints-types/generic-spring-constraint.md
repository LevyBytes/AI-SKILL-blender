# Generic Spring Constraint

## Generic Spring Constraint

### Generic Spring Constraint 

Reference

Panel :

Physics ‣ Rigid Body Constraint

Type :

Generic Spring

The generic spring constraint applies spring parameters across X/Y/Z axes, extending Generic constraint capabilities.
Using springs alone causes bouncing between anchor-attached objects—usually excessive freedom.
Most scenarios benefit from enabling translation or rotation constraints alongside springs.

Setting spring damping to 1 prevents forces from realigning anchor points, causing odd behavior. Verify damping levels if springs behave unexpectedly.

### Options 

Generic Spring constraint options. 

Limits

X/Y/Z Axis
Enable/disable translation limits on X, Y, or Z axis.

Lower
Minimum translation for X, Y, or Z axis.

Upper
Maximum translation for X, Y, or Z axis.

X/Y/Z Angle
Enable/disable rotation limits around X, Y, or Z axis.

Lower
Minimum rotation for X, Y, or Z axis.

Upper
Maximum rotation for X, Y, or Z axis.

Springs

X/Y/Z Axis
Enable/disable spring translation on X, Y, or Z axis.

Stiffness
Spring stiffness controlling translation flexibility on X, Y, or Z axis. Higher values reduce compliance.

Damping
Spring damping for translation on X, Y, or Z axis, controlling oscillation magnitude.

X/Y/Z Angle
Enable/disable spring rotation around X, Y, or Z axis.

Stiffness
Spring stiffness controlling rotation flexibility around X, Y, or Z axis. Higher values reduce compliance.

Damping
Spring damping for rotation around X, Y, or Z axis, controlling oscillation magnitude.

[Related references](INDEX.md).
