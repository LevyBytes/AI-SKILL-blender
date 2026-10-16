# Rendering Animations: Workflow

## Rendering Animations

### Rendering Animations 

When rendering still images, you can view and save the result from the render buffer once complete. Animations, by contrast, are composed of sequential frames and are automatically stored to disk after rendering finishes.

The typical post-production workflow involves editing clips after rendering, or using the Compositor for tasks such as green-screen keying, matting, color adjustment, depth-of-field processing, and other enhancements applied to individual frames. These frames are then fed to the Sequencer where strips are edited, mixed, and final compositing is applied.

The final stage allows you to export from the Sequencer, encoding the frame sequence into a compressed video file.

### Workflow 

Most animation projects require multiple intermediate renders at different stages to validate timing, lighting, placement, material appearance, and other elements. Once you reach the desired quality level, you can proceed with the final render of the entire animation for distribution.

Two primary strategies exist for creating movies or animations with or without audio. Your choice depends on the total CPU time needed for rendering. You can estimate render time by timing a representative frame at the target resolution, then multiplying by the total number of frames. For example, a 60-second clip filmed at 24fps contains 1440 frames. If each frame takes 30 seconds to render, the total time would be 720 minutes—or 12 hours.

Rendering uses all available CPU resources. Typically you should render when the computer is idle (overnight, for example) or configure Blender to run at reduced priority while working on other tasks (though be mindful of available RAM).

Direct Approach

The Direct Approach is not recommended and represents outdated practice. In this method, you configure output as AVI or MOV format and press Animation to render directly to a movie file. Blender creates a single file containing all animation frames, which can later be processed in the Video Sequencer to add audio and output as MPEG format.

Frame Sequence

The Frame Sequence approach is significantly more reliable. You set output format to a still image type (JPG, PNG, or multi-layer format) and press Animation to render as a series of images where each file represents a single frame.

Blender produces one file per frame. You can then apply any frame-level adjustments in the Compositor, load the final image sequence into the Video Sequencer, add audio, and export to MPEG to create your final video. Though this method requires more storage space and additional steps, it provides greater flexibility during production.

These guidelines help you decide which approach suits your situation.

Direct Approach

- Shorter renders with total time under one hour.

- Steady power source.

- Computer not in use for other purposes.

Frame Sequence Approach

- Total render time exceeding one hour.

- Post-production adjustments needed:

- Color and lighting refinement

- Green screen or matte compositing

- Layering and effects

- Output in multiple resolutions or formats

- Adjustments to frames for compression optimization.

- Exact synchronization (such as audio alignment) in sections.

- May interrupt rendering to use the computer while preserving progress.

[Related references](INDEX.md).
