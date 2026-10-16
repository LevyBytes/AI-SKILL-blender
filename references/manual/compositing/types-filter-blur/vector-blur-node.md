# Vector Blur Node

## Vector Blur Node

The Vector Blur node is a fast way to fake Motion Blur in compositing, using the vector speed render pass to blur the image pixels in 2D. Inputs: Image (linked to the "Combined" render pass); Speed (the "Vector" render pass; see Cycles render passes); Z (Z depth, linked to the "Depth" pass); Samples (a quality factor); and Shutter (the motion-blur duration in seconds, matching the per-frame exposure time). Output: Image (the motion-blurred result). Usage: even a correct Image/Z/Speed setup can still show artifacts, since the 2D passes lack 3D information so what's behind a moving object or off-camera is lost — better results come from rendering into multiple render layers, applying vector blur to each, then compositing them (typically an animated character on a separate layer from the background, especially with hair or transparency); for other artifacts, slightly blurring the Speed pass or setting a Maximum Speed limit can help smooth the motion, though too much blurring brings its own problems.

[Related references](INDEX.md).
