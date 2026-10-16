# UV Operators: Smart UV Project, Options

### Smart UV Project

Reference

Editor:

3D Viewport, UV Editor

Mode:

Edit Mode

Menu:

UV → Unwrap → Smart UV Project

Shortcut:

U

Evaluates angles between selected faces, cuts them where edges are sharp, then projects each separated group along its mean normal onto the UV map. Seams can enable extra cutting. Suited for rigid shapes and structures.

Smart UV project on a truncated pyramid.

### Options

Adjust Last Operation panel allows detailed control:

Angle Limit
The highest angle allowed between adjacent-face normals before separation. Low limits create many small islands with little distortion; high limits yield few large islands with potential distortion.

Margin Method
The Island Margin parameter's meaning, governing empty space between UV islands.

Scaled
Island Margin is somewhat arbitrary, independent of UV island sizes or texture.

Add
Like above, but without internal scaling.

Fraction
Island Margin is a fraction of the UV square. On a 1024x1024 texture with Island Margin at 1/1024, islands get 1-pixel margins (and stay 2+ pixels apart).

Rotation Method

Axis-aligned
Auto-rotate to conserve space.

Axis-aligned (Horizontal)
Rotate islands to sit horizontally.

Axis-aligned (Vertical)
Rotate islands to sit vertically.

Island Margin
Empty space between islands. Margin Method controls its interpretation.

Area Weight
At 0, each group's projection vector is the average of its face normals.
At 1, it's an area-weighted average. Intermediate values blend both.

Correct Aspect
Compensates UV mapping for the target image's aspect ratio.
UVs scale properly when unwrapping to non-square textures.

For this to function, the mesh needs a material with an Image Texture node, which must be chosen in the Shader Editor.

Scale to Bounds
Scale the produced UV map outward until it occupies the whole texture.

[Related references](INDEX.md).
