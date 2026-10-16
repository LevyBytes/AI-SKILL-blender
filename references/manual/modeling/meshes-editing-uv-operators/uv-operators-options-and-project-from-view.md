# UV Operators: Options, Project from View

### Options

Adjust Last Operation panel allows detailed control:

Direction, Align
The sphere axis's orientation.

View on Equator
Use an axis perpendicular to the current viewport direction.
If Align is Polar ZX, use the vertical viewport axis; if Polar ZY, use the horizontal.

View on Poles
Use an axis parallel to the current viewport direction.
The sphere rotates 90° on its vertical axis, and the UV map shifts a quarter-width, based on Align.

Align to Object
Use the object's local Z axis.
The sphere rotates 90° on its vertical axis, and the UV map shifts a quarter-width, based on Align.

Pole
How to treat vertices on the sphere axis.
(See Cylinder Projection for an example.)

Pinch
Gather all UV versions of the vertex to the same U coordinate.
Often results in heavy UV face distortion.

Fan
Spread each UV version across U coordinates that reduce distortion.

Preserve Seams
Cut the mesh along seams before applying projection.

Correct Aspect
Compensates UV mapping for the target image's aspect ratio.
UVs scale properly when unwrapping to non-square textures.

For this to function, the mesh needs a material with an Image Texture node, which must be chosen in the Shader Editor.

Clip to Bounds
Relocates out-of-bounds UVs to the closest border.

Scale to Bounds
Scale the produced UV map outward until it occupies the whole texture.

### Project from View

Reference

Editor:

3D Viewport

Mode:

Edit Mode

Menu:

UV → Project from View

Shortcut:

U

Maps selected faces onto the viewport plane. The UV map becomes a wireframe view of the mesh from the current angle. Choose this when using a photo of a real object as texture. Receding areas will show stretching.

[Related references](INDEX.md).
