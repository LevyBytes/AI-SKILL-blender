# Passes: Cycles

### Cycles

Diffuse

Direct
The intensity and color of light that hit a surface with a Diffuse or Subsurface Scattering BSDF and did not yet bounce off/pass through any other surface (ignoring Transparent ones). The color of the surface itself is not included.

Indirect
The intensity and color of light that hit a surface with a Diffuse or Subsurface Scattering BSDF and already bounced off/passed through another surface before (ignoring Transparent ones). The color of the surface itself is not included.

Color
The colors of Diffuse and Subsurface Scattering BSDFs, modified by any Mix and Add Shader nodes. The intensity and color of light are not included.

Glossy

Direct, Indirect, Color
Same as above, but for glossy BSDFs.

Transmission

Direct, Indirect, Color
Same as above, but for transmissive BSDFs.

The Transparent BSDF is not included; see Light Paths for details. To create a transparent surface that does get included in this pass, use a Glass BSDF with the IOR set to 1.

Volume

Direct, Indirect
Same as above, but for volumetric BSDFs.

Other

Emission
Emission from directly visible surfaces.

Environment
Emission from the directly visible World Environment. When the Film is set to Transparent (meaning the world is excluded from the final render), this pass can be used to get the environment color and composite it back in.

Ambient Occlusion
Ambient occlusion from directly visible surfaces. This is a grayscale pass with values that go from 0 (fully occluded) to 1 (fully exposed), making it suitable for multiplying with a color image in the Compositor (see Mix Color Node).

As an alternative to this pass, it's also possible to use the Ambient Occlusion Node in materials.

Shadow Catcher
Shadows collected by objects with the Mask – Shadow Catcher option enabled. Can be multiplied with existing footage to (for example) have a rendered object cast a shadow on recorded ground.

[Related references](INDEX.md).
