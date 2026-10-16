# Blur Node

## Blur Node

The Blur node blurs an image, offering several modes. Inputs: Image (standard color input) and Size (an optional input multiplied with the X/Y blur radius, also accepting a value image to control the radius by a mask, ideally mapped 0 to 1). Type, differing in how they handle sharp edges, smooth gradients, and the highs/lows: Flat (blur everything uniformly), Tent (preserve highs and lows better via a linear falloff), Quadratic (Gaussian-like but a little faster and slightly worse), Cubic (keep the highs while giving an almost out-of-focus blur that smooths sharp edges), Gaussian (best-looking but slowest), Fast Gaussian (a Gaussian approximation), Catmull-Rom (keeps sharp contrast edges crisp), and Mitch (much like Cubic — highs kept, with a soft defocus-style blur over sharp edges). Also: Extend Bounds (let the blurred image extend past its original size) and Separable (a faster approximation blurring horizontally and vertically independently). Output: Image (standard color output).

[Related references](INDEX.md).
