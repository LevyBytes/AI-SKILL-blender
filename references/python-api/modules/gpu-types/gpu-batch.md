# gpu.types.GPUBatch

class gpu.types. GPUBatch ( type , buf , elem = None )

Reusable container for drawable geometry.

Parameters :

- type ( Literal [ 'POINTS' , 'LINES' , 'TRIS' , '`LINE_STRIP`' , '`LINE_LOOP`' , '`TRI_STRIP`' , '`TRI_FAN`' , '`LINES_ADJ`' , '`TRIS_ADJ`' , '`LINE_STRIP_ADJ`' ] ) – The primitive type of geometry to be drawn.

- buf (gpu.types.GPUVertBuf) – Vertex buffer containing all or some of the attributes required for drawing.

- elem (gpu.types.GPUIndexBuf | None) – An optional index buffer.
draw ( shader = None )

Execute the drawing shader using the parameters bound to the batch.

Parameters :

shader (gpu.types.GPUShader | None) – Shader that performs the drawing operations.
If None is passed, the last shader set to this batch will run.
draw_instanced ( program , * , instance_start = 0 , instance_count = 0 )

Render several copies of the drawing program with the batch's bound parameters.
Inside the vertex shader, gl_InstanceID holds the index of the instance currently
being drawn.

Parameters :

- program (gpu.types.GPUShader) – Program that performs the drawing operations.

- instance_start ( int ) – Number of the first instance to draw.

- instance_count ( int ) – Number of instances to draw. When not provided or set to 0
the number of instances will be determined by the number of rows in the first
vertex buffer.
draw_range ( program , * , elem_start = 0 , elem_count = 0 )

Execute the drawing program with the batch's bound parameters. Restrict drawing to the elem_count elements of the index buffer beginning at elem_start .

Parameters :

- program (gpu.types.GPUShader) – Program that performs the drawing operations.

- elem_start ( int ) – First index to draw. When not provided or set to 0 drawing
will start from the first element of the index buffer.

- elem_count ( int ) – Number of elements of the index buffer to draw. When not
provided or set to 0 all elements from elem_start to the end of the
index buffer will be drawn.
program_set ( program )

Bind a shader to this batch so it serves for drawing unless replaced afterward.
Note: This method has to be called in the draw context that the batch will be drawn in.
This function does not need to be called when you always
set the shader when calling gpu.types.GPUBatch.draw().

Parameters :

program (gpu.types.GPUShader) – The program/shader the batch will use in future draw calls.
vertbuf_add ( buf )

Attach an extra vertex buffer to the Batch.
You cannot grow the batch's vertex count with this method.
What it does instead is let you layer more attributes onto the vertices already present.
A typical scenario is having one
vertex buffer for vertex positions and a separate one for vertex normals.
At present a batch is limited to at most `GPU_BATCH_VBO_MAX_LEN` vertex buffers.

Parameters :

buf (gpu.types.GPUVertBuf) – The vertex buffer that will be added to the batch.

[Related references](INDEX.md).
