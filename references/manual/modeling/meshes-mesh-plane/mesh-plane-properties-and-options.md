# Mesh Plane: Properties, Options, Material

## Mesh Plane

### Mesh Plane

Reference

Menu :

3D Viewport ‣ Add ‣ Image ‣ Mesh Plane

In one step, Mesh Plane builds a plane, fits its proportions to the chosen image, and gives it a material textured with that image. Filenames drive the names of the resulting plane, material, and texture.

Accepted inputs are a single image, several images at once, an image sequence, or a movie clip:

- Single Image : one plane carrying the image as its texture.

- Multiple Images : several planes, either stacked together or spread out.

- Image Sequence/Movie Clip : one plane that plays back the animated frames.

### Properties

Whatever import settings you choose can be stored as an Operator Preset.

### Options

Relative Paths
Records the image path relative to the open blend-file. See Relative Paths.

Force Reload
Re-reads the file even when its image data-block is already loaded.

Detect Image Sequences
Treats numbered image files as one animated sequence rather than as individual planes. Blender sets the frame range for you, and you can tweak it afterward.

### Material

So the imported picture shows up, Blender builds a material for the plane. These shader choices exist:

Shader
The type of node shader to use.

Principled :

Routes the image into the Base Color input of a Principled BSDF shader.

Shadeless :

Yields a material that ignores lighting, mixing Diffuse and Emission shaders under the control of a Light Path node.

Emission :

Like Principled , except the texture feeds the Emission input rather than Base Color .

Emission Strength
Adjusts the intensity of emission.

Render Method
Governs blending behavior and which features stay compatible. See Material Settings for more information.

Dithered :

Supports grayscale hashed transparency and works with render passes and raytracing. This is the deferred-rendering path.

Under the Dithered method, rendering happens in stacked layers. Any given layer can only transmit (for instance, refract) light coming from the layers before it, and where nothing below is hit, transmissive BSDFs fall back to light probes.

Blended :

Supports colored transparency but rules out render passes and raytracing. This is forward rendering.

Show Backface
Reveals the far side through transparent areas.

Backface Culling
Conceals the plane's far side.

Overwrite Material
Normally a name clash makes Blender add a number to keep the new material distinct; turning this on lets the new material replace the existing one instead.

[Related references](INDEX.md).
