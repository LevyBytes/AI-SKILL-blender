# Film

## Film

### Film

Reference

Panel :

Render ‣ Film

Exposure
Adjusts image brightness. Unlike the Exposure in Color management, this option operates on raw image values while Color management exposure applies to the view transform.

### Pixel Filter

Images and screens have finite resolution, necessitating pixel filters to prevent Aliasing. The technique applies slight blurring to soften edges.

Type
Filtering algorithm selection.

Box :

No filtering.

Gaussian :

Smooth filtering.

Blackman-Harris :

Default, balancing smoothness with detail retention.

Width
Lower values produce crisp renders; higher values soften and reduce aliasing.

### Transparent

Render the background as transparent, enabling compositing over alternate backgrounds after rendering.

Transparent Glass
Render refractive surfaces as transparent for compositing glass over alternate backgrounds.

Roughness Threshold
For transparent glass, surfaces with roughness exceeding this limit remain opaque.

Film: Filtering and Background

Filter Size
Limited image and screen resolution necessitate pixel filtering to avoid aliasing artifacts. This is achieved by gentle image softening.

This setting controls softening strength; lower values produce sharp renders, higher values soften and reduce aliasing.

Transparent
Render the background transparent for compositing over a different backdrop post-render.

Overscan
Percentage of render dimensions to add to the internal render buffer. Serious performance impact but resolves perimeter render glitches.

[Related references](INDEX.md).
