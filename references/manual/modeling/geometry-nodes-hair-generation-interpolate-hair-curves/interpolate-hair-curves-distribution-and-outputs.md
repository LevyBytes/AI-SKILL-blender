# Interpolate Hair Curves: Distribution, Outputs

### Distribution

Distribution Method
Sets how root points for interpolated curves spread over the surface.

Random :

Scatters roots randomly across the surface.

Poisson Disk :

Uses Poisson disk sampling to keep a minimum distance between root points, giving an even, natural spread.

Density
Interpolated strands grown per unit of surface area. Higher values lift total hair density.

Density Mask
A scalar factor that locally scales curve density over the surface.

Mask Texture
An image texture deciding which surface areas grow hair, sampled via the Surface UV Map input.

Tip

Sampling runs after root points exist, so mesh resolution does not cap accuracy. The Density Mask input is usually faster; both together balance quality and performance.

Viewport Amount
A factor thinning viewport curve density for performance; final render density is untouched.

Seed
Random seed for interpolation and distribution. Move it for a different spread under the same settings.

### Outputs

Geometry
Output geometry holding the interpolated hair curves.

Guide Index
An integer attribute holding, per interpolated curve, the index of the main guide curve that generated it.

Surface Normal
The surface normal heading at each strand's root attachment point.

[Related references](INDEX.md).
