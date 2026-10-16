# gpu: Custom Shader for dotted 3D Line

```python
import bpy
import gpu
from gpu_extras.presets import draw_texture_2d

WIDTH = 512
HEIGHT = 256

offscreen = gpu.types.GPUOffScreen(WIDTH, HEIGHT)

def draw():
    context = bpy.context
    scene = context.scene

    view_matrix = scene.camera.matrix_world.inverted()

    projection_matrix = scene.camera.calc_matrix_camera(
        context.evaluated_depsgraph_get(), x=WIDTH, y=HEIGHT)

    offscreen.draw_view3d(
        scene,
        context.view_layer,
        context.space_data,
        context.region,
        view_matrix,
        projection_matrix,
        do_color_management=True)

    gpu.state.depth_mask_set(False)
    draw_texture_2d(offscreen.texture_color, (10, 10), WIDTH, HEIGHT)

bpy.types.SpaceView3D.draw_handler_add(draw, (), 'WINDOW', 'POST_PIXEL')
```

### Custom Shader for dotted 3D Line

Here, each vertex computes its arc length, meaning the distance back to the line's first point.
That figure is then interpolated automatically across the vertex and fragment shaders
for every on-screen point in between.
The fragment shader takes the sine of that arc length.
From the outcome it decides whether or not to draw the fragment.

[Related references](INDEX.md).
