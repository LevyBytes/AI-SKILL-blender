# Color Spaces: Display, Linear, Other

### Display 

Color spaces for displays and image files.

sRGB :

Standard RGB display space using Rec. 709 chromaticities and a D65 white point.

Rec.2020 :

BT.2020 2.4 Exponent EOTF Display.

Rec.1886 :

BT.1886 2.4 Exponent EOTF Display, commonly used for TVs.

Display P3 :

Apple's Display P3 with sRGB compound (piece-wise) encoding transfer function, common on Mac devices.

Rec.2100 PQ :

For high dynamic range images and video with Rec.2020 wide gamut, up to 10000 nits.

Rec.2100 HLG :

For high dynamic range images and video with Rec.2020 wide gamut, up to 1000 nits.

### Linear 

Color spaces commonly used for OpenEXR files.

Working Space :

The current blend file's linear working space, the default for compositing, shader and geometry nodes.

Linear Rec.709 :

Linear BT.709 chromaticities with illuminant D65 white point.

Linear Rec.2020 :

Linear BT.2020 with illuminant D65 white point.

ACEScg :

An ACES color space meant for rendering and compositing.
Its makeup is AP1 primaries, a white point at D60, and a transfer function that is linear.
The standard working space in ACES workflows.

ACES2065-1 :

An ACES color space whose makeup is AP0 primaries, again a D60 white point, with a linear transfer function.
Built to store and ship data while holding onto the most information it can.
The usual choice for delivery and archival across ACES workflows.

Linear FilmLight E-Gamut :

Linear E-Gamut with illuminant D65 white point.

Linear DCI-P3 D65 :

Linear DCI-P3 with illuminant D65 white point.

Linear CIE-XYZ E :

1931 CIE XYZ standard with assumed illuminant E white point.

Linear CIE-XYZ D65 :

1931 CIE XYZ with adapted illuminant D65 white point.

### Other 

Non-Color :

Plain non-color data, left untouched by any color transform (normal or displacement maps, for instance).

Working Space :

Falls back on the File color space set in the scene's color management.

[Related references](INDEX.md).
