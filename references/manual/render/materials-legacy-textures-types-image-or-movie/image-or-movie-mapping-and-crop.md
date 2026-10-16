# Image or Movie: Mapping, Crop, Sampling

### Mapping

Image Mapping panel.

In the Mapping panel, you can control how the image is mapped or projected onto the 3D model.

Flip Axes
Rotates the image 90 degrees counterclockwise when rendered.

Extension
How the image is extrapolated beyond its original bounds.

Extend :

Outside the image the colors of the edges are extended.

Clip :

Clip to image size and set exterior pixels as transparent. Outside the image, an alpha value of 0.0 is returned. This allows you to 'paste' a small logo on a large object.

Clip Cube :

Clips to cubic-shaped area around the images and sets exterior pixels as transparent. The same as Clip, but now the 'Z' coordinate is calculated as well. An alpha value of 0.0 is returned outside a cube-shaped area around the image.

Repeat :

The image is repeated horizontally and vertically.

Repeat X, Y
X/Y repetition multiplier.

Mirror X, Y
Mirror on X/Y axes. These buttons allow you to map the texture as a mirror, or automatic flip of the image, in the corresponding X and/or Y direction.

Checker :

Checkerboards quickly made. You can use the option size on the Mapping panel as well to create the desired number of checkers.

Tiles Even/Odd
Set even/odd tiles.

Distance
Governs the distance between the checkers in parts of the texture size.

#### Crop

Minimum X, Y / Maximum X, Y
The offset and the size of the texture in relation to the texture space. Pixels outside this space are ignored. Use these to crop, or choose a portion of a larger image to use as the texture.

### Sampling

In the Sampling panel you can control how the information is retrieved from the image.

Image Sampling panel.

Interpolation
This option interpolates the pixels of an image. This becomes visible when you enlarge the picture. By default, this option is on. Turn this option off to keep the individual pixels visible and if they are correctly anti-aliased. This last feature is useful for regular patterns, such as lines and tiles; they remain 'sharp' even when enlarged considerably. Turn this image off if you are using digital photos to preserve crispness.

| Description | Description |
| --- | --- |
| Magnified Picture pattern absent Blending . | Magnified Picture pattern utilizing Blending . |

Span
Boost the filter scope utilized via blending.
When you see dark lines or edges surrounding the patterned thing, notably wherever the picture gets see-through,
switch that rating down starting 1.0 to 0.1 or likewise.

[Related references](INDEX.md).
