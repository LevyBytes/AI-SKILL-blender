# Rotation: Angular Velocity

### Angular Velocity 

Reference

Panel :

Particle System ‣ Rotation ‣ Angular Velocity

Permits specifying whether and how particles rotate over their lifetime. Dynamic activation requirement exists for this feature.

Axis

The rotation center. Velocity, Horizontal, or Vertical selections additionally sustain orientation relative to movement direction, even at zero Amount.

None

Rotation deactivates.

Velocity

Rotation occurs about the particle's velocity vector.

Horizontal

Rotation happens around the axis orthogonal to movement and lying in the worldwide XY plane. Vertical-moving particles exhibit no rotation due to lack of distinct axis.

Vertical

Rotation occurs about the axis orthogonal to horizontal rotation and particle velocity. Vertical-moving particles exhibit no rotation.

Global X, Y, Z

Rotation about universal axes.

Random

Rotation about an arbitrary axis.

Hint

Deploy Curve Guide with particles oriented to curve direction via Velocity / Hair Orientation Axis, Dynamic activation, and Velocity Angular Velocity Axis. Particles will consistently point curve-forward. (Standard objects use Follow Curve via Follow Path Constraint or curve legacy Follow, though these methods lack particle compatibility.)

Amount

The rotational speed magnitude about the Axis.

[Related references](INDEX.md).
