# Mesh Cache Modifier: Options

## Mesh Cache Modifier

### Mesh Cache Modifier

The Mesh Cache modifier pulls animated mesh data out of an external file and feeds it to a mesh, letting the mesh deform across time. Its usual role is importing animation built in other software, delivering smooth playback of those cached deformations.

In behavior it sits close to shape keys, yet the modifier exists specifically to play back animation stored externally rather than deformations driven by keyframes.

Important

The .mdd and .pc2 formats both count on the vertex order holding steady across the whole animation.
Add, drop, or shuffle vertices downstream of this modifier and you may get results you didn't intend.

### Options

Mesh Cache Modifier.

Format
Names the input file format. For now the modifier handles .mdd and .pc2 .

File Path
Where the external cache file holding the animation data lives.

Influence
Sets how strong the deformation comes through. Drop it lower and the cached animation blends with the original mesh shape.

Deform Mode
Sets the way the cache data acts on the mesh:

Overwrite :

Swaps vertex positions out for the ones held in the cache file.

Integrate :

Folds the cache deformation in with deformations already present, like shape keys or modifiers.

Note

This mode suits small, localized tweaks best.
Sweeping changes, reposing limbs for instance, may not behave as you'd expect.

Interpolation
Sets how the frames sitting between cache data get handled:

None :

Draws on nothing but the raw cache frames, with no interpolation.

Linear :

Blends across frames for smoother transitions, handy when cache frames don't line up exactly with the scene
frames.

Vertex Group
When given, limits the effect to just the vertices held in that vertex group.

Invert
Flips which vertices the chosen vertex group covers, so the group instead
marks the vertices the modifier will leave undeformed.

The group's weight values are reversed by this setting.

[Related references](INDEX.md).
