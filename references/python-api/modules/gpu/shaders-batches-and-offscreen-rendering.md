# GPU shaders, batches and offscreen rendering

### Shaders

Think of a shader as a small program executed by the GPU (here authored in GLSL).
Several shader kinds exist.
The two you care about most are the Vertex Shaders and the Fragment Shaders .
In general several shaders get linked together to form a Program .
Within Blender's Python API, though, the word Shader is used to mean an OpenGL Program.
A single gpu.types.GPUShader is made up of a vertex shader, a fragment shader, and optionally a geometry shader.
Blender ships a handful of ready-made shaders, reachable through gpu.shader.from_builtin
via identifiers like `UNIFORM_COLOR` or `FLAT_COLOR` . Dedicated builtins also exist for
rendering triangles, lines, and points.

Every shader declares the attributes and uniforms you must supply before it can run.
Attributes come from a vertex buffer and may vary from one vertex to the next.
Uniforms stay fixed for the whole draw call.
You assign them through the shader.uniform_* calls once the shader is bound.

Note

Keep in mind that on Apple operating systems the GLSL sources are translated into MSL (Metal Shading Language).
A thin compatibility layer handles this, and it does not implement every part of the GLSL specification.
The points below list the divergences worth remembering when you aim for Apple compatibility:

- Only these matrix constructors are supported:

- diagonal scalar (example: mat2(1) )

- all scalars (example: mat2(1, 0, 0, 1) )

- column vector (example: mat2(vec2(1,0), vec2(0,1)) )

- reshape constructors work only for square matrices (example: mat3(mat4(1)) )

- vertex , fragment and kernel are reserved keywords.

- every type and keyword laid down by the
MSL specification
counts as reserved and must be avoided.

### Batch Creation

You can assemble a batch the manual way by constructing VBOs and IBOs yourself.
Even so, reaching for the gpu_extras.batch.batch_for_shader helper is the recommended path.
It guarantees that all the vertex attributes a particular shader expects are present.
Because of that, you also have to hand the shader to the function.
Going this route, you seldom need to think about the vertex format, VBOs, or IBOs that get spun up behind the scenes.
You should still understand all of that when you start drawing, though.

Given that a batch can be reused across many draws, cache it and reuse it wherever you can.

### Offscreen Rendering

The image visible on screen once rendering finishes is known as the Front Buffer .
As draw calls fire, the batches land on a Back Buffer , and that only appears
once every draw has completed and the current back buffer is promoted to the new front buffer.
There are times when you would rather render the batches into a separate buffer, perhaps to use as a
texture on some other object or to save out as an image file.
That technique is Offscreen Rendering.
Blender handles Offscreen Rendering through the gpu.types.GPUOffScreen type.

Warning

gpu.types.GPUOffScreen objects stay tied to the OpenGL context in which they were created.
So as soon as Blender lets go of that context (for instance when the window closes),
the offscreen instance is released.
### Examples

To give these examples a spin, paste them straight into Blender's text editor and run them.
So that the examples stay short, they merely register a draw function that can no longer be removed easily.
You will need to restart Blender to clear out the draw handlers.

[GPU drawing examples](INDEX.md).

[Related references](INDEX.md).
