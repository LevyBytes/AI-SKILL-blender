# Multiply Strip

## Multiply Strip

### Multiply Strip

Multiply combines two color values.
Blender uses 0.0–1.0 scales.
Two 0.0–1.0 values multiply to stay 0.0–1.0, no normalization needed.

(Standard RGB bytes like RGB(124, 255, 56) produce out-of-range products like RGB(7316, 46410, 1848), requiring division by 256 to fit RGB(0–255).)

Main uses:

With a Mask

A black-and-white mask, when multiplied with an image, reveals only white zones (other areas turn black).

James Bond opening sequences, where the camera peers down a gun barrel, exemplify this.

With Uniform Colors

Multiplying a hue with an image softens certain color bands (and boosts complementary ones).

A brown pixel RGB(0.50, 0.29, 0.05) multiplied by cyan RGB(0.0, 1.0, 1.0) becomes RGB(0.0, 0.29, 0.05).
Reds disappear while blue and green heighten. Physically, cyan light on chocolate results in greener greens and bluer blues. Naturally, plants flourish more vivid, seawater looks tropical, skies feel open.

Note

This operation darkens overall output (result below both inputs).
All white → other picture; all black → all black!

### Options

This strip has no options.

### Example

Multiply Effect.

[Related references](INDEX.md).
