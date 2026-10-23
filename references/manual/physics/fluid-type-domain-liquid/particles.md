# Particles

## Particles

### Particles

Note

Secondary particle activation also creates a particle system. Deactivation deletes it and settings. These systems don't contribute to mesh generation, needing geometry assignment for rendering.

Spray
Generate spray during secondary simulation: those airborne particles from big splashes.

Foam
Generate foam: surface-riding particles.

Bubbles
Generate bubbles: subsurface particles.

Combined Export
Particle-type grouping into single particle system. No sim outcome change, only allocation.

Upres Factor
Particle sim resolution multiplier, matching Resolution Divisions.

Wave Crest Potential Maximum
Wave-crest marking threshold ceiling. Higher = fewer marked.

Wave Crest Potential Minimum
Wave-crest marking threshold floor. Lower = more marked.

Trapped Air Potential Maximum
Trapped-air marking ceiling. Higher = fewer marked.

Trapped Air Potential Minimum
Trapped-air marking floor. Lower = more marked.

Kinetic Energy Potential Maximum
Fluid-speed ceiling initiating particle emission. Higher = fewer particles.

Kinetic Energy Potential Minimum
Fluid-speed floor. Lower = more particles.

Potential Radius
Radius for per-cell potential. Higher = slower, smoother grids.

Particle Update Radius
Radius for per-particle position updating. Higher = slower, less chaotic movement.

Wave Crest Particle Sampling
Max particles per wave-crest cell per frame.

Trapped Air Particle Sampling
Max particles per trapped-air cell per frame.

Particle Life Maximum
Longest particle existence.

Particle Life Minimum
Shortest particle existence.

Bubble Buoyancy
Upward force strength. High = mainly upward movement.

Bubble Drag
Fluid-following force strength. High = fluid-aligned movement.

Particles in Boundary

Delete :

Remove secondary particles inside obstacles or leaving domain.

Push Out :

Reintroduce secondary particles to the domain.

Bake Particles, Free Particles
With Modular cache.

Status bar shows progress; Esc pauses. Post-baking, Free Particles clears. Pause/resume available.

[Related references](INDEX.md).
