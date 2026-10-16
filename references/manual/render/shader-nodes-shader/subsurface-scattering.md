# Subsurface Scattering

## Subsurface Scattering

### Subsurface Scattering

This node supplies a basic form of subsurface multiple scattering, which suits skin, wax, marble, milk and the like. With these materials light does not simply reflect off the surface; it sinks in, bounces around inside, and is either absorbed or exits again a short distance away.

You can set the average travel distance of each colour channel on its own. Skin, for instance, lets red travel furthest, which is what gives it those characteristic reddish shadows and its soft look.

### Inputs

Color
Surface tint, or in physics terms, the per-wavelength chance that light bounces back.

Scale
Overall multiplier on the scattering radius.

Radius
Mean depth light reaches under the surface. A larger figure softens the look as light seeps into shadow and across the object. Each of the R, G and B channels gets its own scattering distance, which lets you render things like skin where red travels deeper. The three vector components feed the R, G and B channels in order.

IOR Cycles Only
Index of refraction for Subsurface Scattering .

Anisotropy Cycles Only
Directionality of subsurface scattering. Higher anisotropy scatters deeper into the object.

Roughness Cycles Only
Roughness of the glossy shell wrapping the subsurface volume.

Normal
Shading normal; leaving it unconnected falls back to the geometry's default shading normal.

### Properties

Subsurface Method
Rendering method to simulate subsurface scattering.

Note

EEVEE does not support the Random Walk methods.

Christensen-Burley :

A physically based volume-scattering approximation. It is less accurate than Random Walk, though in certain scenes it clears noise sooner.

Random Walk (Fixed Radius) :

Gives accurate results on thin, curved objects. Because Random Walk does real volumetric scattering inside the mesh, it suits closed meshes best; holes and overlapping faces can trip it up.

Random Walk :

Works much like Random Walk (Fixed Radius) but adjusts the Radius from the Color , Anisotropy , and IOR . That way it aims to hold on to more surface detail and colour than Random Walk (Fixed Radius) does.

### Outputs

BSSRDF
BSSRDF shader output.

### Examples

Random walk subsurface scattering.

[Related references](INDEX.md).
