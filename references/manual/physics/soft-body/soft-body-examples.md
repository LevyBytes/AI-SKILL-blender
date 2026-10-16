# Examples

### Examples 

Simple examples demonstrate soft-body physics potential.

### A Bouncing Cube

### The Process 

Initialize start and end frames as 1 and 150.

Add a plane and scale five times. Go to Physics, add Collision (defaults suffice).

Add a cube (or use default), enter Edit Mode, subdivide three times.
Add a Bevel Modifier to smooth edges; press R twice and move cursor slightly for additional rounding.

The setup now resembles:

The scene, ready for soft body physics. 

Soft body physics activation:
Go to Properties ‣ Physics, select Soft Body.
Uncheck Soft Body Goal; check Soft Body Self Collision.
Under Soft Body Edges, increase Bending to 10.

Playback produces slow-motion bouncing.
For faster playback, bake the physics.

Under Soft Body Cache, set start and end to 1 and 150.
Test with cache step 5 or 10; for final animation, reduce to 1 for complete caching.

The finished setup:

The physics cache settings. 

The physics edges and self collision settings. 

Now bake the simulation, apply materials and textures, and render.

### The Result 

The rendered bouncing cube

[Related references](INDEX.md).
