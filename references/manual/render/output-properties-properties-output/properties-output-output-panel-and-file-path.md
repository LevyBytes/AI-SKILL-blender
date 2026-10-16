# Output: Output panel., File Path

## Output

### Output 

Output panel. 

This panel manages rendered frame storage location and saved image quality for animations.

File Path
Select where to save rendered output.

During animation rendering, frame numbers are appended to the filename using four zero-padded digits (e.g. image0001.png). Customize padding by inserting # characters in the filename (e.g. image_##_test.png converts to image_01_test.png).

This option respects Relative Paths, where // indicates the folder containing the active .blend file.

Saving – File Extensions
Adds the proper file extension per format to output.

Saving – Cache Result
Renders view layers and passes to a multi-layer OpenEXR image. The Compositor can leverage this cached file for enhanced performance during intensive compositing work.

Storage location is determined by the Render Cache folder in File Paths Preferences. You can retrieve it back to the Image Editor's Render Result even after closing and restarting Blender; see Open Cached Render.

Media Type
Output media classification.

Image :

Saves each input as a separate image.
Each input type supports independent image settings.

Multi-Layer EXR :

Combines all inputs into a single multi-layer OpenEXR file.

Video :

Encodes frames into a video format. Detailed codec options appear in the Encoding panel.

File Format Image
Select the image file format for saving. Different formats present different options such as channels, bit depth, and compression levels. Consult the image encoding options list.

Color Image Multi-Layer EXR
The output color format for the image or video. Some formats use this setting to optimize data storage. Note that RGBA is unavailable for certain formats; see the format list above.

BW :

Output using grayscale.

RGB :

Saves red, green, and blue channels.

RGBA :

Saves red, green, blue, and alpha channels.

Image Sequence – Overwrite Image Multi-Layer EXR
Replace existing files when rendering.

Image Sequence – Overwrite Image Multi-Layer EXR
Reserve placeholder files while rendering.

Hint

Primitive Render Farm

A simple setup for distributing rendering across multiple machines involves:

- Establish a shared directory over network file storage.

- Turn off Overwrite and turn on Placeholders in the Render Output panel.

- Trigger rendering on as many systems as desired pointing to the shared location.

[Related references](INDEX.md).
