# Rendering Animations: Frame Sequence Workflow, Hints

### Frame Sequence Workflow 

- Prepare your animation first.

- In the Format panel, specify render dimensions, Pixel Aspect Ratio, and Frame Range (Start and End), with frame rate typically pre-configured.

- In the Output panel, configure your animation to export as images, choosing a format that preserves quality.

- Define the output folder and file format in the Output panel, for instance //render/my-anim- .

- Verify your animation's start and end frames.

- Save your .blend file.

- Press the Animation button. Once rendering completes, open your file manager and browse to the output location (render in this example). A numbered series of image files awaits you—each corresponds to a single frame.

- Open the Video Sequencer in Blender.

Note

The Video Sequencer lacks multi-layer EXR support. To produce video, omit the following three operations and route your sequence through an Image Input node in the Compositor instead.

- From the add menu, select Add Image. Choose all desired frames from your output folder and import them as a strip in the Sequence editor.

- Edit the strip, apply effects if desired, or leave it unchanged. Combine with additional strips such as audio.

- Play through the animation to confirm all frames are present.

- In the Output panel, choose the video container and codec (for example, MPEG H.264) and adjust settings. Video codec specifications appear in Output Options.

- Press the Animation render button to encode the Sequence editor contents into a video file.

### Hints 

If your computer unexpectedly turns off during rendering, recovery is simplest with image-based output. Instead of rendering directly to a compressed video file, use a lossless format (PNG). This makes recovery straightforward—already-rendered frames remain in the output directory.

Simply uncheck the Overwrite option to resume from the last completed frame.

Create your final video using Blender's Sequence editor or external encoding tools.

Animation Preview
Previewing a subset of your animation can help isolate errors within specific sections.

Using image output format, the Frame Step option renders every Nth frame. Then disable Overwrite and re-render with Frame Step set to 1.

[Related references](INDEX.md).
