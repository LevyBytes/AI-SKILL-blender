# UV Operators: Options, Sphere Projection

### Options

Adjust Last Operation panel allows detailed control:

Direction, Align
The cylinder axis's orientation.

View on Equator
Use an axis perpendicular to the current viewport direction.
If Align is Polar ZX, use the vertical viewport axis; if Polar ZY, use the horizontal.

View on Poles
Use an axis parallel to the current viewport direction.
The cylinder rotates 90° on its axis, and the UV map shifts a quarter-width, based on Align.

Align to Object
Use the object's local Z axis.
The cylinder rotates 90° on its axis, and the UV map shifts a quarter-width, based on Align.

Pole
How to treat vertices on the cylinder axis.

Pinch
Gather all UV versions of the vertex to the same U coordinate.
Often results in heavy UV face distortion.

Fan
Spread each UV version across U coordinates that reduce distortion.

| Description | Description | Description |
| --- | --- | --- |
| Unwrapping the top of a dome. | Pole set to Pinch. | Pole set to Fan. |

Preserve Seams
Cut the mesh along seams before applying projection.

Radius
Half the cylinder height (not its radius; the cylinder exists only for projection, so its radius is irrelevant).

Correct Aspect
Compensates UV mapping for the target image's aspect ratio.
UVs scale properly when unwrapping to non-square textures.

For this to function, the mesh needs a material with an Image Texture node, which must be chosen in the Shader Editor.

Clip to Bounds
Relocates out-of-bounds UVs to the closest border.

Scale to Bounds
Scale the produced UV map outward until it occupies the whole texture.

### Sphere Projection

Reference

Editor:

3D Viewport, UV Editor

Mode:

Edit Mode

Menu:

UV → Unwrap → Sphere Projection

Shortcut:

U

Casts selected faces onto an imaginary sphere, then flattens it like a world map: latitude lines run vertical, longitude lines space evenly. Helpful for texturing globular objects like eyes or planets.

The sphere centers on the Transform Pivot Point, typically at the selected faces' averaged position; you can move it elsewhere (e.g., using the 3D Cursor).

Using an equirectangular image with a Sphere Projection.

[Related references](INDEX.md).
