# Particle Edit Mode: Moving Keypoints or Particles, Mirror, Unify Length, Show/Hide

### Moving Keypoints or Particles 

- Press G to move selected keypoints, or employ standard vertex-editing methods.

- Disable Keep Root in the Toolbar to reposition particle roots.

- Apply standard vertex operations: scale, rotate, delete (full particles or individual keypoints).

- Keypoint duplication and extrusion are unavailable, but particle subdivision adds keypoints (Particle ‣ Subdivide).

- Alternatively, reparametrize a particle with Particle ‣ Rekey.

Path Steps settings govern display smoothness. Low settings produce blocky interpolation; high settings yield smooth curves.

### Mirror 

Reference

Mode :

Particle Edit Mode

Menu :

Particle ‣ Mirror

To create X-axis symmetrical haircuts:

- Select all particles: A.

- Mirror with Particle ‣ Mirror.

- Enable X Mirror in Sidebar Region ‣ Tool ‣ Options.

Mirroring can position two particles nearly identically. To save memory and render time, apply Merge by Distance from the Particle menu.

### Unify Length 

Reference

Mode :

Particle Edit Mode

Menu :

Particle ‣ Unify Length

Equalizes selected hair length by averaging.

### Show/Hide 

Reference

Mode :

Particle Edit Mode

Menu :

Particle ‣ Show/Hide

Hide and reveal particles similarly to vertex hiding in the 3D Viewport. Select target keypoints and press H to hide the particle; keypoints hide while the particle persists.

Hidden particles (those with hidden keypoints) do not respond to brush operations. However:

If Mirror Editing is active, particles with hidden keypoints may move when their mirrored counterparts move.

Press Alt - H to reveal all hidden particles.

[Related references](INDEX.md).
