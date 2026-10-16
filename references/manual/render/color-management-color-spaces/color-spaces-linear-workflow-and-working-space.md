# Color Spaces: Linear Workflow, Working Space, Images and Video, Built-in Color Spaces

## Color Spaces

### Color Spaces 

### Linear Workflow 

Rendering, showing, and storing images each demand a Different Color Space.

For rendering and compositing the best fit is a scene linear color space, since it follows nature more closely and keeps the math physically sound.
Blender leans on scene linear color across materials, lighting, geometry and compositing.

Those numbers, though, line up with neither human sight nor the workings of a display.
And image files frequently park in other color spaces to squeeze better compression.

A sound linear workflow hinges on tagging both images and displays with the right color spaces.
Blender then runs the conversions into and out of scene linear color.

An example of a linear workflow. 

### Working Space 

Reference

Editor :

Properties

Panel :

Render Properties ‣ Color Management ‣ Working Space

File
The color space behind every scene linear color in this file, and the one shader, compositing and geometry node processing run in. It defaults to Linear Rec.709, with Linear Rec.2020 and ACEScg on hand for a broader gamut and ACES compatibility.

Since each data-block draws its colors from the working space, the pick weighs on render and composite results in a big way. Best to lock the working space in at a project's start and hold it across every blend file.

Blender can move between working spaces, but only as an approximation that usually wants hand correction. Link or append a data-block and its colors convert automatically to the current file.

Sequencer
The color space the Sequencer works in.
By default that is sRGB, though you may switch it to Linear, matching the Compositing nodes, or to another color space.
Color correction, crossfades and the like come out differently from one color space to the next.

The default supported color spaces are described in
Built-in Color Spaces.

### Images and Video 

With image and video files, Blender first tries to detect the color space on its own.
Guesses wrong, and you can set the file's color space by hand in the image settings.

The classic case for a manual change is loading or baking normal maps and displacement maps.
Those maps carry no real color, only data wearing a color disguise.
Flag such images as Non-Color Data .

For intermediate production image files, OpenEXR is the recommended format.
It always sits in scene linear color spaces at high precision, so nothing is lost.
That makes it a good home for renders you will later composite, color grade, and recast into other output formats.

### Built-in Color Spaces 

Blender's OCIO configuration file is equipped by default to read/write files in these color spaces

[Related references](INDEX.md).
