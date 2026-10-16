# Collision: Soft Body and Cloth, Examples, Hints

### Soft Body and Cloth

This panel notifies all sims that the object deflects/collides with dynamics on shared layers (particles, soft bodies, cloth).

Note

The object's geometry deforms cloth, so the sim requires the "true" mesh shape at that frame—the base shape modified by shape keys or armatures. Place the Collision Modifier after these.
The image shows the Character mesh Modifiers panel (not the cloth object).

Collision stack. 

Damping
Collision damping regulating surface bounce.

- 0.0 - None, soft bodies bounce maximally.

- 1.0 - Full, soft bodies don't bounce.

Thickness
Padding added internally and externally to faces, preventing intersections. The soft body settles away from faces by this distance. Normal (blue arrow) defines inside/outside.

Outer
Outer collision zone extent.

Inner
Inner zone padding distance.

A soft body vertex colliding with a plane. 

Friction
How slippery cloth is during collision. Silk glides more than cotton.

Single Sided
When active, the collider represents a solid boundary, ejecting intersecting cloth along its normal.

Override Normals
When active, cloth collision forces follow collider normals.

Note

Soft body collision is finicky. Fast-moving objects cause penetration. Check Soft Bodies.

### Examples

Deflected particles. 

A Meta object uses Instancing Vertices onto downward-emitting particles deflected by a mesh cube.

### Hints

- Orient mesh normals toward particles for correct deflection. Negative scales have similar effects; recalculate normals after applying scales.

- Hair reacts directly to force fields, so short-range fields may eliminate collision needs.

- Hair avoids its emitting mesh in Particle Edit Mode for basic collision modeling.

[Related references](INDEX.md).
