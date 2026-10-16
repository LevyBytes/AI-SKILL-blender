# Particle Instance Modifier: Create Along Paths, Layers, Examples

### Create Along Paths

Out of the box, instances sit wherever the particles happen to be on the current frame. Switch on Create Along Paths and the modified object's instance bends its shape to trail the particle path (or hair strand), which frees you to choose a spot along that path independent of the current frame.

Tip

To tune the particles' path, switch to the Path visualization type
over on the Render panel of the Particle System tab.

Note

A baked particle system is required, the exceptions being Hair type and Keyed physics.

Position
Sets what share of the path the instance fills,
or where it sits on the path when the Keep Shape option is on.

Random
Sprinkles randomness onto each instance's Position value.

Rotation
Sets the rotation about the path.

Random
Sprinkles randomness onto each instance's Rotation value.

Keep Shape
Switching this on keeps the instance from deforming
and drops it onto the path at the spot given by the Position value.

### Layers

Through these fields you pick the Color Attribute to be loaded with colors derived from the particle data. Such Color Attributes can serve, for instance, inside a shader to bring variation to a material.

Index
A Color Attribute holding values drawn from the particle's index.

Value
A Color Attribute holding random per-particle values.

### Examples

Particle Instance modifier example.

In the render above, one plane mesh object carries two separate vertex groups,
and each group feeds its own independent particle system,
with every particle system tied to a distinct Particle Instance modifier.
Here the Particle Instance modifiers sit on a sphere and a cube.
See example blend-file.

Create Along Path example.

Here a lone Keyed particle runs through four points (the green planes)
along an elliptical path. The Particle Instance modifier goes onto a cylinder object,
which is then linked to that Keyed particle system.

Switch Create Along Paths on and, rather than the cylinder simply sitting where the particle is,
the cylinder mesh bends to match the path the particle traces.
How cleanly that deformation comes off depends on the geometry of the object being bent.
The cylinder here carries plenty of loop cuts down its length,
giving it points at which to flex and follow the particle path.

Create Along Paths on the Particle Instance modifier handles hair (strand) particles
just as it does keyed ones. With hair, the modifier's mesh tracks
the length and profile of the strand paths.

Note

Since strands die the instant they're generated, the Create Along Paths checkbox is
only of any use when you've also turned the Dead checkbox on.

[Related references](INDEX.md).
