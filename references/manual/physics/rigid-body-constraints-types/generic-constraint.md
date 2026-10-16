# Generic Constraint

## Generic Constraint

### Generic Constraint 

Reference

Panel :

Physics ‣ Rigid Body Constraint

Type :

Generic

The generic constraint provides extensive parameters.

X, Y, and Z axis constraints limit object translation. Clamping min/max to zero replicates Point constraint behavior.

Clamping relative rotation to zero maintains alignment.
Combining absolute rotation and translation clamps mimics Fixed constraint behavior.

Nonzero parameter spreads allow oscillation throughout the simulation.

### Options 

Limits

Angular

X Angle, Y Angle, Z Angle
Enable/disable rotation limits around X, Y, or Z axis.

Lower
Minimum rotation for X, Y, or Z axis.

Upper
Maximum rotation for X, Y, or Z axis.

Linear

X Axis, Y Axis, Z Axis
Enable/disable translation limits on X, Y, or Z axis.

Lower
Minimum translation for X, Y, or Z axis.

Upper
Maximum translation for X, Y, or Z axis.

[Related references](INDEX.md).
