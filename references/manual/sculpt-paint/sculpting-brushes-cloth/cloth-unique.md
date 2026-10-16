# Cloth: Unique

### Unique

Persistent
Prevents accumulation of deformation across successive strokes.
Useful for repeatedly applying distinct forces to a starting shape.

When off, each stroke compounds on previous results.

Set Persistent Base
Resets the reference geometry, allowing additional layered deformations.

Simulation Area
Defines which mesh portion activates during the stroke.
Selection directly impacts performance based on mesh density.

Local
Updates only a fixed-radius region centered on the brush.

Global
Updates all visible mesh geometry.

Dynamic
The active region follows the brush while remaining bounded by a fixed radius.

Simulation Limit
Distance factor relative to brush radius controlling effect extent.

Simulation Falloff
Region receiving deformation falloff application.
Scales as a multiplier of Simulation Limit; shown as a dashed outline.

Pin Simulation Boundary
Locks vertices in the falloff zone, preventing discontinuities
and transitioning smoothly to unaffected areas.

Deformation
The operation type applied to cloth.

Drag:
Pulls cloth toward the cursor,
matching a finger sliding across fabric.

Push:
Drives cloth away from the cursor,
like pressing on cloth with a fingertip.

Pinch Point:
Concentrates cloth into a pointed tip.

Pinch Perpendicular:
Concentrates cloth into a linear edge.

Inflate:
Raises cloth by introducing compressed air underneath.

Grab:
Lifts and repositions cloth as a unit.

Expand:
Stretches the fabric outward.

Snake Hook:
Moves cloth while maintaining surface integrity,
producing natural-looking pleats and folds.
This is achieved by modulating deformation stiffness per step
to reduce simulation influence.

Force Falloff
Brush impact profile.

Radial:
Distributes force as a sphere.

Plane:
Distributes force as a flat plane.

Cloth Mass
Weight of each simulated particle.

Cloth Damping
Propagation rate of forces through cloth.

Soft Body Plasticity
Retention of original configuration,
providing Soft Body characteristics.

Use Collisions
Activates contact with external objects during simulation.
Objects must have Collision Physics enabled to participate.

[Related references](INDEX.md).
