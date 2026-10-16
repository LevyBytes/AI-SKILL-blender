# Hair Dynamics

## Hair Dynamics

### Hair Dynamics 

Reference

Panel :

Particle System ‣ Hair Dynamics

Hair particles gain physics-based behavior through dynamic simulation. Enable hair physics by toggling the checkbox next to Hair Dynamics.

Quality Steps
Simulation quality expressed as steps per frame; higher values improve fidelity at the cost of computation time.

Pin Goal Strength
Spring stiffness governing how strongly vertices return to their target positions.

Warning

When applying motion blur to animations, render one additional frame beyond the final output frame to ensure proper blur calculation.

### Collisions 

Quality
General parameter controlling simulation fineness; greater values produce more precise results with reduced mesh penetration, though computation increases.

Distance
The threshold distance at which other objects trigger hair repulsion away from contact. Smaller distances risk numerical errors but accelerate computation; larger values may produce unrealistic results and slow the simulation.
Optimal results come from balancing speed against fidelity.

Impulse Clamping
Restricts post-collision movement to prevent explosions in geometrically complex collision scenarios.

Collision Collection
Restricts collisions to objects in the specified collection; these objects must have Collision physics enabled.

### Structure 

Reference

Panel :

Particle System ‣ Hair Dynamics ‣ Structure

Vertex Mass
Numerical value controlling hair weight.

Stiffness
Parameter governing strand resistance to bending.

Random
Random variation in hair stiffness.

Damping
Damping coefficient for bending oscillations.

### Volume 

Reference

Panel :

Particle System ‣ Hair Dynamics ‣ Volume

Real-world hair phenomena can be modeled more efficiently through volumetric approaches rather than pure geometric strand representation. This involves constructing a regular three-dimensional grid (similar to fluid simulation grids) and interpolating hair properties across cell boundaries.

Air Drag
Parameter controlling medium density around hair, determining drag magnitude and flow speed.

Internal Friction
Friction coefficient between individual hair strands.

Voxel Grid Cell Size
Dimension of each cell in the volumetric simulation grid.

Density Target
Upper limit on hair volumetric density.

Density Strength
Magnitude of influence the Density Target exerts on the simulation.

[Related references](INDEX.md).
