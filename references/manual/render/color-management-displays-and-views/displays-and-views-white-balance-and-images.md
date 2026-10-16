# Displays and Views: White Balance, Images, Display, Output, Video

### White Balance 

Nudges colors so a chosen white point, set by color temperature and tint, reads as white on the display.

Rather than punching in values, you can grab the color picker.
Pick a color and temperature and tint settle so that color balances to white.
This holds only when the color lands close enough to a blackbody emitter.

You may also white balance through the compositing pipeline by way of the Color Balance Node

Temperature
The blackbody temperature of the lead illuminant. A D65 white point is the default.

Tint
How far the blackbody curve leans toward green or magenta.

Blackbody temperature curve. 

### Images 

### Display 

By default, only renders show up and save with the render View baked in.
These are the "Render Result" and "Viewer" image data-blocks, plus the files the Render Animation operator writes straight to disk.
Reopen a render stored as an intermediate OpenEXR file, though, and Blender cannot work out by itself that it is a render
(for all it knows, the file is an image texture or a displacement map).
The settings below are how we tell it the file is indeed a render and that the transformations should go on.

View as Render
Show the image data-block, renders included, with view, exposure, gamma and RGB curves applied.
Good for eyeing rendered frames in linear OpenEXR files just as they look fresh from the renderer.

### Output 

For saving files, a matching option waits.

Save as Render
A switch in the image save operator that lays on the view, exposure, gamma and RGB curves.
Good for writing linear OpenEXR out to, say, PNG or JPEG in display space.

These file formats accept wide gamut images: PNG, JPEG, WebP, AVIF, TIFF and JPEG 2000.

For HDR images the choices are AVIF or PNG. Blender writes them at 203 nits diffuse white, the convention most browsers and image viewers expect.

### Video 

### Output 

Video renders out in wide gamut and HDR color spaces alike. The scene display is the default, though overriding the color management settings in the output properties lets you assign another color space.

Writing out HDR video brings a handful of extra demands:

- Set color management display to Rec.2100 PQ or HLG

- Set codec to H.265 or AV1

- Set bit depth to 10 or 12

Players and devices vary in how far they support HDR video.
For the broadest reach, bit depth 10 alongside PQ encoding stands as a solid default.

For HDR video Blender uses 100 nits diffuse white, the convention most video players and browsers expect.

[Related references](INDEX.md).
