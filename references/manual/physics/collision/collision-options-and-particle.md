# Collision: Options, Particle

## Collision

### Collision

Reference

Mode :

Object Mode

Panel :

Physics ‣ Collision

Particles, Soft Bodies, and Cloth can hit mesh objects. Boids avoid Collision objects.

- Particle effect scope can be restricted to a group (Field Weights panel).

- Deflection for soft body is tricky; penetration often happens.

- Hair particles disregard deflectors (though animating as soft bodies respects deflection).

Cache recalculation is manual (Delete Bake) when deflection settings change—it doesn't happen automatically.

A collider may be toggled on/off animatably using the control to its right.

### Options

Collision panel.

### Collision

Field Absorption
A deflector can block effectors. Specify absorption per collision object to reduce force transmission. 100% blocks completely. Stacked objects (10%, 43%, 3%) absorb around 50% (100 × (1 - 0.1) × (1 - 0.43) × (1 - 0.03)).

### Particle

Permeability
Portion of particles crossing the mesh.

Stickiness
Particle adherence strength.

Kill Particles
Destroys particles upon contact.

Damping
Collision-induced damping (velocity-independent).

Randomize
Random damping variation.

Friction
Surface friction during movement.

Randomize
Random friction variation.

[Related references](INDEX.md).
