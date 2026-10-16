# UV Operators: Options, Cube Projection, Cylinder Projection

### Options

Adjust Last Operation panel allows detailed control:

Edge Length Mode
Method for computing the UV edge lengths of newly attached quads.

Even
Each new UV edge gets the same length as the UV edge it extends, regardless of mesh edge length.

Length
Each new UV edge length is proportional to its mesh edge length.

Length Average
Each new UV edge length is proportional to its edge ring's average mesh edge length.

### Cube Projection

Reference

Editor:

3D Viewport, UV Editor

Mode:

Edit Mode

Menu:

UV → Unwrap → Cube Projection

Shortcut:

U

Assigns each selected face to the most fitting side of an imaginary cube, then lays all sides across the UV map, overlapping. Use Pack Islands to separate if needed.

The cube aligns with the Transform Pivot Point center and the mesh's local axes.

### Options

Adjust Last Operation panel allows detailed control:

Cube Size
The projection cube's dimension.

Correct Aspect
Compensates UV mapping for the target image's aspect ratio.
UVs scale properly when unwrapping to non-square textures.

For this to function, the mesh needs a material with an Image Texture node, which must be chosen in the Shader Editor.

Clip to Bounds
Relocates out-of-bounds UVs to the closest border.

Scale to Bounds
Scale the produced UV map outward until it occupies the whole texture.

### Cylinder Projection

Reference

Editor:

3D Viewport, UV Editor

Mode:

Edit Mode

Menu:

UV → Unwrap → Cylinder Projection

Shortcut:

U

Maps selected faces onto a virtual cylinder, then unwraps it.
The cylinder centers on the Transform Pivot Point, typically at the selected faces' averaged position; you can move it elsewhere (e.g., using the 3D Cursor).

[Related references](INDEX.md).
