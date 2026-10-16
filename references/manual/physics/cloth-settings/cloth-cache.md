# Cache

## Cache

### Cache

Reference

Panel :

Physics ‣ Cloth Cache

After the deflection mesh is ready for the target frame range (including any animation via armatures),
instruct the cloth simulator to compute and handle collisions. Select the cloth object and in the Object tab, Physics tab, set Start and End frames for computation, then press Bake.

Cloth cache settings match those of other dynamic systems. See Particle Cache for more.

Note

If the cloth object moves or is edited after simulation has already run, the cache must be cleared; otherwise, Blender will misrepresent vertex positions using the stored mesh state.

Note

Subdivision Surface Modifier

Baking and caching occur at each subdivision level, so preview and render subdivision must match.

Note

Start and End cannot change without clearing the simulation. Once finished, options appear: free the bake, edit it, or re-bake.

### Editing the Cached Simulation

Important

Cached simulation editing is not currently functional, see:
blender/blender#77114 for details.

[Related references](INDEX.md).
