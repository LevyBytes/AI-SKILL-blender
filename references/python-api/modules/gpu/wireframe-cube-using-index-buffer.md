# gpu: Wireframe Cube using Index Buffer

```python
import bpy
import gpu
from gpu_extras.batch import batch_for_shader


vert_out = gpu.types.GPUStageInterfaceInfo("my_interface")
vert_out.smooth('VEC3', "pos")

shader_info = gpu.types.GPUShaderCreateInfo()
shader_info.push_constant('MAT4', "viewProjectionMatrix")
shader_info.push_constant('FLOAT', "brightness")
shader_info.vertex_in(0, 'VEC3', "position")
shader_info.vertex_out(vert_out)
shader_info.fragment_out(0, 'VEC4', "FragColor")

shader_info.vertex_source(
    "void main()"
    "{"
    "  pos = position;"
    "  gl_Position = viewProjectionMatrix * vec4(position, 1.0f);"
    "}"
)

shader_info.fragment_source(
    "void main()"
    "{"
    "  FragColor = vec4(pos * brightness, 1.0);"
    "}"
)

shader = gpu.shader.create_from_info(shader_info)
del vert_out
del shader_info

coords = [(1, 1, 1), (2, 0, 0), (-2, -1, 3)]
batch = batch_for_shader(shader, 'TRIS', {"position": coords})


def draw():
    matrix = bpy.context.region_data.perspective_matrix
    shader.uniform_float("viewProjectionMatrix", matrix)
    shader.uniform_float("brightness", 0.5)
    batch.draw(shader)


bpy.types.SpaceView3D.draw_handler_add(draw, (), 'WINDOW', 'POST_VIEW')
```

### Wireframe Cube using Index Buffer

```python
import bpy
import gpu
from gpu_extras.batch import batch_for_shader

coords = (
    (-1, -1, -1), (+1, -1, -1),
    (-1, +1, -1), (+1, +1, -1),
    (-1, -1, +1), (+1, -1, +1),
    (-1, +1, +1), (+1, +1, +1))

indices = (
    (0, 1), (0, 2), (1, 3), (2, 3),
    (4, 5), (4, 6), (5, 7), (6, 7),
    (0, 4), (1, 5), (2, 6), (3, 7))

shader = gpu.shader.from_builtin('POLYLINE_UNIFORM_COLOR')
batch = batch_for_shader(shader, 'LINES', {"pos": coords}, indices=indices)

def draw():
    shader.uniform_float("viewportSize", gpu.state.viewport_get()[2:])
    shader.uniform_float("lineWidth", 4.5)
    shader.uniform_float("color", (1, 0, 0, 1))
    batch.draw(shader)

bpy.types.SpaceView3D.draw_handler_add(draw, (), 'WINDOW', 'POST_VIEW')
```

### Mesh with Random Vertex Colors

[Related references](INDEX.md).
