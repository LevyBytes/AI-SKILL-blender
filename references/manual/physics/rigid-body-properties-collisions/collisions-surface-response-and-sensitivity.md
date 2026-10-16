# Collisions: Surface Response, Sensitivity, Collections

### Surface Response 

Friction
Movement resistance; specifies velocity loss upon collision.

Bounciness
Rebound magnitude after collision (0 to 1, rigid to perfectly elastic).
Determines how much objects bounce following contact.

### Sensitivity 

Collision margins enhance performance and stability.
Shape-dependent behavior: some shapes embed margins; others show visible gaps.

Embedded margin shapes:

- Sphere

- Box

- Capsule

- Cylinder

- Convex Hull: uniform scale required when embedded.

Non-embedded margin shapes:

- Cone

- Active Triangle Mesh

- Passive Triangle Mesh: usually zero.

Margin
Collision proximity threshold where interactions still occur; nonzero values typically perform best.

### Collections 

Rigid body collision allocation uses groups (up to 20).

[Related references](INDEX.md).
