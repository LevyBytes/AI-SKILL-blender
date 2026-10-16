# Frame Range

## Frame Range

### Frame Range 

Frame Range panel. 

This panel establishes animation duration measured in frames. Dividing total frames by the scene's Frame Rate yields animation duration in seconds. For instance, a 250-frame sequence at 30 fps lasts 8.3 seconds.

Frame Start, End
Specify the first and final frames to use for Rendering Animations.

Step
Determines frame increment per render iteration. Values above 1 skip intermediate frames. This parameter also applies when reviewing rendered results.

### Time Stretching 

Rescale animation playback to make it run faster or slower. The Old and New values can function either as absolute frame counts or as a ratio: for example, setting Old to 2 and New to 1 accelerates the animation by half.

Warning

Time Stretching does not affect the Start or End frames configured above. Ensure your animation runs completely within these bounds without truncation or trailing blank frames.

Old
The original animation length in frames.

New
The target duration in frames for the remapped animation.

[Related references](INDEX.md).
