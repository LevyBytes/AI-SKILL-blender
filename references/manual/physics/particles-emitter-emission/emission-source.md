# Emission: Source

### Source 

Reference

Panel :

Particle System ‣ Emission ‣ Source

Emit From

Defines emission methodology and site, granting granular spatial distribution authority.

Tip

Vertex groups constrain emission; configuration happens in the Vertex Groups panel.

Vertices

Particles originate from mesh vertices.

Faces

Particles originate from mesh surface faces.

Volume

Particles originate from the interior of a closed mesh.

Tip

Mesh must be Manifold for volume emission. Edge Split Modifiers and similar fracture the surface, preventing volume emission from operating as intended.

Use Modifier Stack

Takes Modifiers positioned above the Particle Modifier in the modifier hierarchy into consideration during emission, otherwise using unmodified geometry.

Note

Rendered particles may diverge from viewport particles when modifiers create differing geometry between viewport and render output.

Distribution

These configurations govern how particle emissions disperse across release sites (Faces or Volume).

Jittered

Particles distribute across jittered placements on emitter geometry.

Particles/Face

Emissions per surface face (0 = automated calculation).

Jittering Amount

The degree of distribution randomness applied.

Random

Particles discharge from arbitrary locations within emitter geometry.

Grid

Particles arrange in a 3D lattice; those within geometry stay, others discard.

Invert Grid

Inverts geometry interpretation and spatial interpretation.

Hexagonal

Employs hexagonal lattice configuration instead of rectangular arrays.

Resolution

The lattice granularity.

Random

Applies random translation to grid positions.

Random Order

Emitter indices process in random succession rather than sequentially. Grid distribution excludes this option.

Even Distribution

Particle distribution equilibrates via surface area ratios, yielding smaller elements producing fewer particles while maintaining uniform density.

[Related references](INDEX.md).
