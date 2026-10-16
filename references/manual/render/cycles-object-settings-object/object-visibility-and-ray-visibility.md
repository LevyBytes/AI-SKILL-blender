# Object: Visibility, Ray Visibility, Culling

## Object

### Object 

### Visibility 

Reference

Panel :

Object Properties ‣ Visibility

See also

There are several other general visibility properties.

Mask – Shadow Catcher
Sets the object to soak up shadow rays and nothing else. Worth noting: shadow catcher objects still swap indirect light with other CG objects.
That smooths the job of dropping CGI elements into real-world footage.

Note

What the Shadow Catcher hands back depends on whether the Shadow Catcher pass is on in the Render Layer settings. With the pass on, every indirect light interaction is logged. With it off, a plain approximation stands in, and that approximation is what viewport rendering leans on.

Example of the shadow catcher. Note how the material of the plane can still be viewed in the spheres. 

### Ray Visibility 

Objects can be hidden from particular ray types.
One use is keeping an emitting mesh out of camera rays.
Instanced objects inherit this; hide the parent from some ray types and the children go hidden from those too.

On performance, these options beat a shader node setup chasing the same look.
An object invisible to a given ray drops out early in ray traversal, which trims ray casts and shader runs.

Camera
Lets the Camera see the object, the viewport's own view included while it renders.

Diffuse
Lets diffuse rays see the object.

Glossy
Lets glossy rays see the object.

Transmission
Lets transmission rays see the object.

Volume Scatter
Lets volumetric scatter rays see the object.

Shadow
Lets the object throw shadows.

### Culling 

To switch these on you first have to enable the matching camera cull options over in the scene simplify panel.

Use Camera Cull
Hide objects from rays by tossing out anything past the camera frustum.

Use Distance Cull
Drops any object sitting farther from the camera than a set distance. Married to camera frustum culling, it spares nearby objects that fall outside the frustum yet still surface in reflections. It is handy too for culling small objects far off.

[Related references](INDEX.md).
