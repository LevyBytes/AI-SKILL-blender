# Motor Constraint

## Motor Constraint

### Motor Constraint 

Reference

Panel :

Physics ‣ Rigid Body Constraint

Type :

Motor

The motor constraint generates translation and/or rotation between objects.
It drives objects apart or together, creates simple rotation, or combines rotation with translation.
Translation may be blocked while rotation continues—the constraint differs from a screw.

The rotation axis is the constraint object's X axis, contrasting with Hinge's Z axis.
The Motor is vulnerable to confusing perturbations without a matching Hinge constraint—axes must align carefully.
Misalignment causes apparent motor inactivity.

Motor constraint options. 

### Options 

Linear Motor/Angular Motor

Enable
Activates linear or angular motor.

Target Velocity
Linear or angular motor target velocity.

Max Impulse
Maximum linear or angular motor impulse.

[Related references](INDEX.md).
