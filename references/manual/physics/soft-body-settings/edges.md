# Edges

## Edges

### Edges 

Reference

Panel :

Physics ‣ Soft Body ‣ Edges

Configure mesh edges to function as springs. See interior forces.

Springs
Designate a vertex group for spring stiffness values.

Pull
Spring stiffness for edges (stretch resistance).
Lower values mean weak springs (elastic material); higher values mean strong springs (stiff material).

0.5 resembles latex; 0.9 resembles a sweater; 0.999 resembles heavily starched fabric or leather.
Instability develops at 0.999, warranting reduction.

Push
Soft-body compression resistance, like a compression spring.
Low values suit fabric; high values suit inflated or stiff objects.

Damp
Spring friction magnitude. High values (up to 50) dampen Push / Pull and stabilize cloth.

Plasticity
Permanent post-collision deformation.
Vertices assume new positions without modifier application.

Bending
Adds virtual connections between a vertex and its neighbors' neighbors, including diagonals. Damping applies here too.

Length
Edges shrink or expand in percentage; 0 disables. 100% maintains size.

Collision

Edge
Detects soft-body mesh-edge collisions.

Face
Detects soft-body mesh-face collisions (computationally intensive).
Face-enabled collision resolves errors but lacks dampening. Soft-body regions near collision meshes "jitter" even without motion.
Edge collision includes dampening for better control, though collision-object Deflection Dampening doesn't affect face collision.

### Aerodynamics 

Surrounding-medium force.
See exterior forces for details.

Type

Simple :

Edges receive drag from surrounding medium.

Lift Force :

Edges receive lift while passing through medium.

Factor
Aerodynamic force magnitude. Begin with 30.

### Stiffness 

Quad-face diagonal edges act as springs, preventing collapse.

Shear
Virtual spring stiffness for quad-face diagonals.

[Related references](INDEX.md).
