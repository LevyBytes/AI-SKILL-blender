# GPU vertex and index buffers

### GPU Module (gpu)

The gpu module exposes Python bindings over Blender's internal GPU layer.
Additional convenience helpers live in the gpu_extras module.

### Geometry Batches

Drawing happens one batch at a time.
Each batch holds everything required to issue a draw call.
That means a mandatory Vertex Buffer plus an optional Index Buffer ,
both of which the sections below cover further.
On top of that a batch carries a draw type.
Common draw types include POINTS , LINES and TRIS .
This draw type controls how the stored data is read back and rendered.

### Vertex Buffers

The Vertex Buffer Object (VBO) (gpu.types.GPUVertBuf)
holds an array of the per-vertex attributes a given shader needs in order to draw.
Common examples of such attributes are location , normal , color , and uv .
Each vertex buffer carries a Vertex Format (gpu.types.GPUVertFormat)
along with a length matching how many vertices it stores.
The vertex format lays out which attributes sit on each vertex and what type each one is.

The snippet below builds a vertex buffer holding 6 vertices.
Two attributes are kept for every vertex: its position and its normal.

```python
import gpu
vertex_positions = [
    (-1, -1, 0), (1, -1, 0), (1, 1, 0),
    (-1, -1, 0), (1, 1, 0), (-1, 1, 0),
]
vertex_normals = [(0, 0, 1)] * len(vertex_positions)

fmt = gpu.types.GPUVertFormat()
fmt.attr_add(id="pos", comp_type='F32', len=3, fetch_mode='FLOAT')
fmt.attr_add(id="normal", comp_type='F32', len=3, fetch_mode='FLOAT')

vbo = gpu.types.GPUVertBuf(len=6, format=fmt)
vbo.attr_fill(id="pos", data=vertex_positions)
vbo.attr_fill(id="normal", data=vertex_normals)
```

From this single buffer you might render 6 points, 3 standalone lines, 5 chained lines, 2 standalone triangles, and so on.
With lines, for example, every consecutive pair of vertices forms one segment.
Exactly which primitive gets rendered is settled at the moment the batch is built later on.

### Index Buffers

It is common for neighbouring triangles and lines to reuse the same vertices.
Relying on a vertex buffer alone forces you to repeat all the attributes of those shared vertices over and over.
That wastes a lot of memory, since in a connected triangle mesh each vertex is touched roughly 6 times.
A leaner option is the Index Buffer (IBO) (gpu.types.GPUIndexBuf),
which also goes by the name Element Buffer .
An Index Buffer simply holds an array pointing at vertices by their position inside the vertex buffer.

As an illustration, a rectangle made from two triangles can be expressed with an index buffer.

```python
positions = (
    (-1,  1), (1,  1),
    (-1, -1), (1, -1))

indices = ((0, 1, 2), (2, 1, 3))

ibo = gpu.types.GPUIndexBuf(type='TRIS', seq=indices)
```

In this code the first tuple inside indices names the vertices that make up the first triangle
(and the second tuple does the same for the second one).
Notice that vertices 1 and 2, lying on the diagonal, belong to both triangles.
[Related references](INDEX.md).
