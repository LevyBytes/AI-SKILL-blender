# gpu: Triangle with Custom Shader

```python
import bpy
import gpu
from gpu_extras.batch import batch_for_shader

coords = [(1, 1, 1), (-2, 0, 0), (-2, -1, 3), (0, 1, 1)]
shader = gpu.shader.from_builtin('POINT_UNIFORM_COLOR')
batch = batch_for_shader(shader, 'POINTS', {"pos": coords})

def draw():
    shader.uniform_float("color", (1, 1, 0, 1))
    gpu.state.point_size_set(4.5)
    batch.draw(shader)

bpy.types.SpaceView3D.draw_handler_add(draw, (), 'WINDOW', 'POST_VIEW')

"""

3D Lines with Single Color
--------------------------
"""

import bpy
import gpu
from gpu_extras.batch import batch_for_shader

coords = [(1, 1, 1), (-2, 0, 0), (-2, -1, 3), (0, 1, 1)]
shader = gpu.shader.from_builtin('POLYLINE_UNIFORM_COLOR')
batch = batch_for_shader(shader, 'LINES', {"pos": coords})

def draw():
    shader.uniform_float("viewportSize", gpu.state.viewport_get()[2:])
    shader.uniform_float("lineWidth", 4.5)
    shader.uniform_float("color", (1, 1, 0, 1))
    batch.draw(shader)

bpy.types.SpaceView3D.draw_handler_add(draw, (), 'WINDOW', 'POST_VIEW')
```

### Triangle with Custom Shader

[Related references](INDEX.md).
