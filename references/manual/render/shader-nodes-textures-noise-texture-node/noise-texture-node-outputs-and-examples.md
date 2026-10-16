# Noise Texture Node: Outputs, Examples, Notes

### Outputs

Factor
Value of fractal noise.

Color
Color with different fractal noise in each component.

### Examples

Noise Texture with high detail.

| fBM (fractal Brownian Motion). | Multifractal. |
| --- | --- |
| Hybrid Multifractal. | Heterogeneous Terrain. |
| Ridged Multifractal. | |

### Notes

Random though it looks, the noise follows a pattern that can fail to produce random values in some setups. Picture a grid of objects whose material samples a noise texture at each location. You would expect varied values since the locations differ, but that is not what happens.

An example configuration where the noise evaluates to a constant value.

Every object reads 0.5. To see why, look at the plot of a 1D noise texture below.

A plot of a 1D noise with zero details and zero distortion.

The horizontal line marks 0.5 and the vertical lines mark whole numbers, assuming a noise scale of 1. As shown, the noise always crosses the 0.5 line right at whole numbers. Since those objects sat on a grid at whole-number locations, they all came out 0.5 — which is the issue.

More generally, sampling the noise at integer multiples of one over the noise scale always returns 0.5, and samples near those points land close to 0.5. When that happens, reaching for the White Noise Texture is almost always the better call.

Either way, a few tricks ease the problem:

- Change the noise scale so the noise stops lining up with the evaluation domain.

- Add some arbitrary offset to the texture coordinates to break that alignment.

- Evaluate the noise at a higher dimension and tweak the extra dimension until it looks right.

| Constant value issue. | Mitigating the issue by adjusting the scale. |
| --- | --- |
| Mitigating the issue by adding an arbitrary offset. | Mitigating the issue by evaluating at a higher dimension. |

A similar thing shows up as banding in other setups, where high-contrast bands alternate with low-contrast ones. Planar surfaces tilted slightly along one axis, for instance, will show this banding.

An example configuration where the noise have a banding pattern.

It happens because the slight tilt makes values along the perpendicular axis change very slowly, which exposes the noise's underlying grid. Rotating the coordinates by an arbitrary amount is the easiest fix.

Mitigating the issue by rotating the coordinates by an arbitrary amount.

[Related references](INDEX.md).
