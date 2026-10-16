# gpu: 2D Rectangle

```python
import bpy
import gpu
import numpy as np
from random import random
from gpu_extras.batch import batch_for_shader

mesh = bpy.context.active_object.data
mesh.calc_loop_triangles()

vertices = np.empty((len(mesh.vertices), 3), 'f')
indices = np.empty((len(mesh.loop_triangles), 3), 'i')

mesh.vertices.foreach_get(
    "co", np.reshape(vertices, len(mesh.vertices) * 3))
mesh.loop_triangles.foreach_get(
    "vertices", np.reshape(indices, len(mesh.loop_triangles) * 3))

vertex_colors = [(random(), random(), random(), 1) for _ in range(len(mesh.vertices))]

shader = gpu.shader.from_builtin('SMOOTH_COLOR')
batch = batch_for_shader(
    shader, 'TRIS',
    {"pos": vertices, "color": vertex_colors},
    indices=indices,
)

def draw():
    gpu.state.depth_test_set('LESS_EQUAL')
    gpu.state.depth_mask_set(True)
    batch.draw(shader)
    gpu.state.depth_mask_set(False)

bpy.types.SpaceView3D.draw_handler_add(draw, (), 'WINDOW', 'POST_VIEW')
```

### 2D Rectangle

```python
import bpy
import gpu
from gpu_extras.batch import batch_for_shader

vertices = (
    (100, 100), (300, 100),
    (100, 200), (300, 200))

indices = (
    (0, 1, 2), (2, 1, 3))

shader = gpu.shader.from_builtin('UNIFORM_COLOR')
batch = batch_for_shader(shader, 'TRIS', {"pos": vertices}, indices=indices)

def draw():
    shader.uniform_float("color", (0, 0.5, 0.5, 1.0))
    batch.draw(shader)

bpy.types.SpaceView3D.draw_handler_add(draw, (), 'WINDOW', 'POST_PIXEL')
```

### 2D Image

Running this example requires you to supply an image to be shown.

[Related references](INDEX.md).
