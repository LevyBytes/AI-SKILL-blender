# Newtonian: Integration, Deflection

### Integration 

Reference

Panel :

Particle System ‣ Physics ‣ Integration

Integrators furnish mathematical frameworks for calculating particle trajectories. Choose per your animation targets per the following direction.

Integration

Euler

Referred to as "Forward Euler". The most basic integrator. Executes fast yet produces less precise results. Without dampening, particles gradually accumulate energy. Bouncing particle energy increases with each bounce as an example. Distinguished from "Backward Euler" (absent here) which dissipates energy gradually. Deploy for brief simulations or highly-dampened scenarios where computation speed outweighs numerical accuracy.

Verlet

Executes swiftly with excellent balance. Energy preservation occurs with minimal computational drift.

Midpoint

Titled "2nd order Runge-Kutta". Slower than Euler yet substantially more accurate. Constant acceleration (minus drag scenarios) preserves energy. Bouncing particles occasionally exceed starting height infrequently, avoiding systematic climbing. Generally superior for most situations.

RK4

Termed "4th order Runge-Kutta". Comparable to Midpoint yet slower with enhanced precision. Energy remains conserved even with variable acceleration. Reserve for complex situations where Midpoint proves inadequate.

Timestep

The elapsed simulation duration (in seconds) per frame.

Subframes

Computational substeps per frame. Increased counts improve stability and resolution precision for rapidly-moving particles.

The following configurations apply exclusively to Fluid-type physics:

Adaptive

The system independently computes the substep count.

Threshold

A precision allowance establishing how far a particle can relocate before requiring extra substeps. Governs relative distance tolerance.

Minimum frame steps number becomes Subframes + 1. Elevated turbulence may trigger supplementary substeps per Threshold specifications.

### Deflection 

Reference

Panel :

Particle System ‣ Physics ‣ Deflection

Size Deflect

Particle scale factors into deflection computations.

Die on Hit

Particles terminate upon deflector impact.

Collision Collection

When specified, particles collide with grouped entities exclusively.

[Related references](INDEX.md).
