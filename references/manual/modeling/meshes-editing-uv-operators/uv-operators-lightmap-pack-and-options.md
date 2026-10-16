# UV Operators: Lightmap Pack, Options, Follow Active Quads

### Lightmap Pack

Reference

Editor:

3D Viewport, UV Editor

Mode:

Edit Mode

Menu:

UV → Unwrap → Lightmap Pack

Shortcut:

U

Positions each selected face individually on the UV map. Lightmaps are widely used for baking lighting into textures for real-time rendering – they maximize texture usage, typically producing a fragmented and skewed UV map unsuitable for hand texturing.

### Options

Adjust Last Operation panel allows detailed control:

Selection

Selected Faces
Only unwraps chosen faces.

All Faces
Unwraps the entire mesh.

Share Texture Space
Multi-Object Editing allows generating UV maps for several meshes simultaneously.
When Share Texture Space is on, UV maps won't cross, so a single lightmap texture can serve all meshes.

New UV Map
Generates a fresh UV map instead of overwriting the current one. See UV Maps.

Pack Quality
Increased values yield less-wasted UV space (yet take longer to process).

Margin
Empty space between faces in the UV map.

### Follow Active Quads

Reference

Editor:

3D Viewport, UV Editor

Mode:

Edit Mode

Menu:

UV → Unwrap → Follow Active Quads

Shortcut:

U

Starting from the active quad, attaches its chosen neighboring quads sequentially to its pre-existing UV quad. Non-quad faces are skipped.

Note

Since the active quad's UV stays unchanged, you typically want to first ensure it has similar proportions in the UV and mesh (e.g., by unwrapping just that face first). Otherwise, distortion spreads outward.

Note

The resulting UV map can exceed bounds. Scale it manually or apply Pack Islands to correct.

[Related references](INDEX.md).
