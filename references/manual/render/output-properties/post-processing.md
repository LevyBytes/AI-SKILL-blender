# Post Processing

## Post Processing

### Post Processing 

Reference

Panel :

Properties ‣ Output ‣ Post Processing

The Post Processing panel configures different output processing parameters applied after rendering.

Post Processing panel. 

Pipeline – Compositing
Executes the compositing node network, applying the Composite node tree across all rendered images and outputting the result from the Group Output node.

Pipeline – Sequencer
Outputs the Video Sequence editor instead of the 3D camera view. If the sequence incorporates Scene strips, these render as part of the workflow. When Compositing is enabled, Scene strip output is post-processed via the Compositor.

Dither
Dithering minimizes color banding artifacts in gradient regions where stair-stepping appears between hues. These artifacts become more conspicuous with extended or shallow gradients. Historically developed for reduced-color graphics with restricted palettes.

Dithering works by comparing pixel intensity against neighboring pixels and applying calculations to produce suitable colors. The process generates an impression of extended color palette through visual color blending. For instance, alternating red and yellow pixels create an orange appearance.

[Related references](INDEX.md).
