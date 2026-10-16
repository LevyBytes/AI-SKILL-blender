# Glossary: Caustics, in the rippling pattern on a pool floor.

Caustics
The optical effect of light concentrated by specular reflection or refraction.
Seen, for instance, when light through a glass of water casts shapes on a table, or
in the rippling pattern on a pool floor.

In rendering it refers to diffuse-reflected light paths after a glossy or refractive bounce.

See also Caustics on Wikipedia.

Child
An Object affected by its Parent.

Chroma
Chrominance
Broadly, the color part left after an image's luminance ( L or Y ) channel is separated out.
The term is used in two different contexts:

Video Systems
The general split into Y (Luminance) and C (Chrominance) channels,
where chrominance is given by U = ( Blue minus Luminance ) and V = ( Red minus Luminance ).

Matte Compositing
A point in the color gamut ringed by a mix of a chosen spectrum of its RGB
neighboring colors. That point is the Chroma key, and this key (a chosen color) is used to make
an Alpha Mask . How much gamut space this chrominance point spans is set by users
in a circular or square shape.

Chromaticities
Where the Primaries sit on the CIE 1931 xy chromaticity diagram.

Clamp
Clamping
Restricting a variable to a range. Values past either end are set
to the constant minimum or maximum of the range.

Collection
A means of organizing objects. See also Collections.

Color Gamut
Traditionally, the span of color a particular color model/space can reproduce.
It's often illustrated as a 2D figure using CIE Yxy coordinates.

Color Model
A scheme for expressing colors as numbers.

RGB
An additive system mixing three primaries — red, green, and blue — to make other colors.

HSV
Three values many find more intuitive (closer to human perception) than RGB.
Here colors are given as Hue, Saturation, and Value.

HSL
Like HSV, except the trio is Hue, Saturation, and Luminance.

YUV
A luminance-chrominance standard from analog PAL (European) broadcast video.

YCbCr
Luminance-ChannelBlue-ChannelRed component video for digital broadcast,
whose standards were updated for HDTV and is often dubbed the HDMI component-video format.

Color Space
A coordinate system where a vector encodes a color value.
Defining one fixes three things:

- The precise color of every Primary.

- The White Point.

- A transfer function (also called a tone response curve).

Which spaces are on hand depends on the active OCIO config;
the defaults are laid out in detail at
Default OpenColorIO Configuration.

Linear
A space whose channel values rise in direct proportion
to light intensity. It's the most physically faithful way to represent color, used internally
for rendering, shading, and compositing so blending and lighting come out right.

[Related references](INDEX.md).
