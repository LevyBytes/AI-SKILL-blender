# bpy.app.handlers: overview

## Application Handlers (bpy.app.handlers)

### Application Handlers (bpy.app.handlers)
This module contains callback lists.

### Basic Handler Example
The simplest example of adding a handler:
```python
import bpy

def my_handler(scene):
    print("Frame Change", scene.frame_current)

bpy.app.handlers.frame_change_pre.append(my_handler)
```

### Persistent Handler Example
By default, handlers are freed when loading new files; sometimes you want one to keep running across multiple files (for instance when it's part of an add-on). For that, use the bpy.app.handlers.persistent decorator.
```python
import bpy
from bpy.app.handlers import persistent

@persistent
def load_handler(dummy):
    print("Load Handler:", bpy.data.filepath)

bpy.app.handlers.load_post.append(load_handler)
```

### Note on Altering Data
Be careful altering data from handlers. During rendering, the frame_change_pre and frame_change_post handlers run on one thread while the viewport updates on another, so if a handler changes data the viewport reads, Blender can crash. In such cases, lock the interface (Render → Lock Interface or bpy.types.RenderSettings.use_lock_interface) before starting a render. Here's an example of a mesh altered from a handler:
```python
def frame_change_pre(scene):
    # A triangle that shifts in the z direction.
    zshift = scene.frame_current * 0.1
    vertices = [(-1, -1, zshift), (1, -1, zshift), (0, 1, zshift)]
    triangles = [(0, 1, 2)]

    object = bpy.data.objects["The Object"]
    object.data.clear_geometry()
    object.data.from_pydata(vertices, [], triangles)
```

[Related references](INDEX.md).
