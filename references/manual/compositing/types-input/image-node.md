# Image Node

## Image Node

The Image node injects any image format Blender supports. It has no input sockets. Properties: Image (a selection of media types — for controls see the Data-Block Menu, for options Image Settings); Source (the image type — Single Image, Movie, etc.; see Image Settings); Frames (how many frames of a movie-type image to play, after which it pauses unless Cyclic is on — to play the whole video, use Match Movie Length in the Image Editor's Sidebar and copy its Frames here); Start Frame (the scene frame at which the video starts); Offset (frames to offset the video earlier — i.e. how many starting frames to skip); Cyclic (loop after the last frame); Auto-Refresh (update the video texture in the 3D Viewport while moving through the timeline); Color Space (the space the file was saved in; see Image Settings); and Alpha (how the image uses its alpha channel; see Image Settings). A hint notes Blender plays video textures at the scene's frame rate rather than their own, so they run faster or slower if the rates differ, and you can work around this with a Driver on Offset: `#(frame - StartFrame) * (VideoFrameRate - SceneFrameRate) / SceneFrameRate`, replacing the names with the numbers. Outputs (the first two are the minimum): Image (standard color output) and Alpha (a separate alpha value) — and for a multi-layer format like EXR, each layer becomes its own socket.

The Image node loads an external image.

Inputs: this node takes no inputs.

Properties:
Image: see Data-Block Menu.

Outputs:
Color: the usual color output.

Extension
How the image extends when Vector lands outside the usual (0, 0, 0) to (1, 1, 1) bounds:

Repeat :

Tile the image across both axes.

Extend :

Stretch the image out by repeating its edge pixels.

Clip :

Crop to the original image size and make every pixel beyond it transparent black.

Mirror :

Flip the image over and over across both axes.

Source
Type of image (Single Image, Movie…). See Image Settings.

Frames
Frame count to play from a Movie-type image (video). Beyond it the clip halts unless Cyclic is on.

For the full clip, hit Match Movie Length in the Image Editor's Sidebar and copy the resulting Frames count onto the node.

Start Frame
Which scene frame the video starts on.

Offset
How far, in frames, to drag the video back in time — equivalently, how many opening frames to skip.

Hint

Video textures run at the scene's frame rate, not the clip's own, so a mismatch leaves them fast or slow. Park a Driver on the Offset to compensate: drop the expression below into the field, with StartFrame , VideoFrameRate and SceneFrameRate swapped for your actual numbers:

#(frame - StartFrame) * (VideoFrameRate - SceneFrameRate) / SceneFrameRate

Cyclic
Loop back to the start after the final frame for a continuous cycle.

Auto Refresh
Refresh the video texture in the 3D Viewport as you scrub the timeline.

Color Space
Whichever Color Space the file was written in. See Image Settings for details.

Alpha
The way this image handles its Alpha Channel. See Image Settings for details.

### Outputs

Color
RGB colour from the image. Where the image has transparency, the colour comes out premultiplied if the Alpha output is used, and straight (non-premultiplied) otherwise.

Alpha
Alpha channel from image.

### Examples

Image texture from GoodTextures.com.

[Related references](INDEX.md).
