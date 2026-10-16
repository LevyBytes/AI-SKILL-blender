# Image Texture Node

### Image Texture Node

Applies an image to a surface as a texture.

### Inputs

Vector
A 3D coordinate projected onto the 2D image through the chosen Projection method; the node then reports the colour and alpha at that projected spot.

This socket usually takes a feed from the Texture Coordinate Node. Left unconnected, the coordinate comes from the object's active UV map (with Z = 0).

### Properties

Image
Image data-block to use.

Interpolation
Method to scale images up or down for rendering.

Linear :

Regular quality interpolation.

Cubic :

Smoother, better quality interpolation. Bump maps should use this for best results.

Closest :

No interpolation (nearest neighbor). Useful for rendering pixel art.

Smart :

Cycles Only
Only for Open Shading Language. Uses cubic interpolation scaling up and linear scaling down, for better speed and sharpness.

Projection
How Vector is projected onto the image to arrive at a colour.

Flat :

Lay the image in a unit square (running from (0, 0, 0) to (1, 1, 0)) and project the Vector straight down onto it. This is the usual choice with UV maps.

Box :

Lay the image on every face of a unit cube (running from (0, 0, 0) to (1, 1, 1)) and project the Vector onto that cube along whichever axis is nearest the mesh normal. It is a common pick for architectural models, which carry plenty of box-shaped objects.

Blend
Instead of hitting a single face (which gives hard seams), project onto several faces and blend the results. Raise the value for more blending and a smoother result.

Sphere :

Wrap the image over a sphere centred at (0.5, 0.5, 0.5) and project the Vector outward from that centre onto it. This is the obvious fit for spherical objects like planets, and works well on organic shapes too.

Tube :

Wrap the image around a cylinder based at (0.5, 0.5, 0) with height 1, then project the Vector sideways from the central axis onto it. Handy for things like a bottle label, though it does not suit the top or bottom of objects.

| Flat projection | Box projection |
| --- | --- |
| Sphere projection | Tube projection |

[Related references](INDEX.md).
