# Cameras: Background Images

### Background Images 

Dropping a backdrop image into the camera earns its keep in many jobs:
modeling is the clear one, but it pays off in painting too
(say, holding face references while you paint textures right onto the model…),
and in animation, where a video stands in as backdrop, among others.

Background Source
Where the backdrop image originates.

Image :

Draw on an outside image, an image sequence, a video file, or a generated texture.

Movie Clip :

Draw on one of the scene's Movie Clip data-blocks.

Active Clip
Display whichever Movie Clip the scene flags as its Active Clip.

Render Undistorted
Draw the backdrop through undistorted proxies wherever they are on hand.

Proxy Render Size
Pick either full non-proxy display or a proxy size for drawing the backdrop.

See also

To build a proxy, the Movie Clip Editor Proxy settings have to be used.
Otherwise the proxy settings here have no effect.

Color Space
The color space Blender reads the image or video file as.

View as Render
Apply the color management settings as this image goes to screen.

Opacity
Sets the backdrop image's transparency.

Depth
Place the image either behind every object or out ahead of them all.

Frame Method
How the image is sized into the camera view.

Stretch :

Pins the image's dimensions to the camera bounds, the aspect ratio shifting if it must.

Fit :

Shrinks the image until it sits wholly inside the camera view, the aspect ratio held intact.

Crop :

Enlarges the image until it covers the whole camera view, the aspect ratio held intact, so its overhanging parts get clipped.

Offset X, Y
Nudge the backdrop image by these amounts.

Under orthographic views the unit is ordinary scene units.
In the camera view it goes relative to the camera bounds (0.1 shifts it by 10% of view width or height).

Rotation
Spin the image about its own center.

Scale
Enlarge or reduce the image from its center.

Flip

X
Mirrors the image left to right, sending the left edge to the right and the reverse.

Y
Mirrors the image top to bottom, sending the top edge to the bottom and the reverse.

Note

A Movie Clip, or any image set to view as render, sits behind objects only with film transparency enabled or the scene world disabled in the viewport.

[Related references](INDEX.md).
