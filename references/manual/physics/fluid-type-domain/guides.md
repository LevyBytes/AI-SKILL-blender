# Guides

## Guides

### Guides

Reference

Panel :

Physics ‣ Fluid ‣ Guides

Type :

Domain

Fluid guides enforce forces on the sim, analogous to external forces yet preserving physically-accurate flow. The Guides panel tunes global guiding. Enabling guides activates more precise (computationally costly) pressure solving even without baked guides or attached domains. Reserve guide-enabling for intentional use.

See also

Fluid guiding is Primal-Dual Optimization for Fluids.

Weight
Guiding lag degree. Larger "alpha" = greater lag.

Size
Vortex size from guiding. Larger "blur radius" or "beta" = bigger vortices.

Velocity Factor
All guiding velocities multiply by this. Every domain-grid cell scales by this.

Velocity Source
Guiding velocity origin.

Effector :

Domain effectors supply global guiding velocity grid. Once baked, domain resolution is locked.

Domain :

Another fluid domain supplies guiding velocity, possibly at different resolution and type (e.g., Gas domain guiding Liquid domain). Must be pre-baked.

Guide Parent
Selects the guiding domain when Domain is the velocity source.

Bake Guides, Free Guides
With Modular cache and Effector velocity source. Bake Guides writes effector vertex velocities for driving, pre-baking step. Status bar shows progress; Esc pauses. After, Free Guides deletes cache. Pause/resume available.

[Related references](INDEX.md).
