# Introduction

### Introduction 

Particles are numerous elements emitted from mesh surfaces, typically numbering in thousands.
Each can be a light source or mesh, linked or dynamic.
They respond to numerous forces and influences, with finite lifespans.
Dynamic particles simulate fire, smoke, mist, dust, magical effects, and similar phenomena.

Hair particles form curves representing hair, fur, grass, and bristles.

Particles appear as Particle Modifiers, though all configuration occurs in the Particle tab.

Example fur created from particles. 

Particles generally flow from emitting geometry into space.
Movement occurs through multiple influences:

- Initial velocity away from the mesh.

- Emitter movement (vertex, face, or object).

- Gravity or air resistance effects.

- Force field effects: wind, vortices, curve guides.

- Object interactions: collisions.

- Swarm intelligence where flock members interact while pursuing targets or avoiding threats.

- Soft-body physics-driven motion (Hair particle systems only).

- Lattice-based manual transformation.

Particle rendering modes include:

- Halos (for Flames, Smoke, Clouds).

- Meshes with animation (fish, bees, etc.); each particle carries another object.

- Hair curves following particle paths, editable in the 3D Viewport (combing, adding, cutting, moving, etc.).

Every object may host multiple particle systems. Each system supports up to 10,000,000 particles. Certain particle types (Hair and Keyed) permit up to 10,000 children per particle.
Memory and patience provide practical boundaries.

[Related references](INDEX.md).
