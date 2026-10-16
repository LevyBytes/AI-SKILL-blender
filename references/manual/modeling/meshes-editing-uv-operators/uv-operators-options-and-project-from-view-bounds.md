# UV Operators: Options, Project from View (Bounds), Reset

### Options

Adjust Last Operation panel allows detailed control:

Orthographic
Apply Orthographic instead of Perspective projection.

Camera Bounds
Align the image borders that would display through the current camera with UV map borders.
Only affects rendering through the camera; see Viewing the Active Camera.

Correct Aspect
Compensates UV mapping for the target image's aspect ratio.
UVs scale properly when unwrapping to non-square textures.

For this to function, the mesh needs a material with an Image Texture node, which must be chosen in the Shader Editor.

Clip to Bounds
Relocates out-of-bounds UVs to the closest border.

Scale to Bounds
Scale the produced UV map outward until it occupies the whole texture.

### Project from View (Bounds)

Reference

Editor:

3D Viewport

Mode:

Edit Mode

Menu:

UV → Project from View (Bounds)

Shortcut:

U

Identical to Project from View, but with Scale to Bounds enabled by default.

### Reset

Reference

Editor:

3D Viewport, UV Editor

Mode:

Edit Mode

Menu:

UV → Reset

Shortcut:

U

Resets each selected face's UV layout to cover the full UV area.

[Related references](INDEX.md).
