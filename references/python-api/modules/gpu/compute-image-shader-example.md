# gpu: compute image shader example

### Custom compute shader (using image store) and vertex/fragment shader

This sample shows the workflow of running a custom compute shader
that writes into a texture, then feeding that texture to a vertex/fragment shader.
What you should see is a 2x2 plane (matching the default cube's size),
whose color shifts from a green-to-black gradient over to a green-to-red gradient,
driven by the current time.

The complete program is in the [upstream source](https://docs.blender.org/api/5.1/gpu.html#custom-compute-shader-using-image-store-and-vertex-fragment-shader).

[Related references](INDEX.md).
