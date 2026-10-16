# bpy.types.RenderEngine: overview

class bpy.types. RenderEngine ( bpy_struct ) 

Render engine
## RenderEngine(bpy_struct)

### RenderEngine(bpy_struct)
### Simple Render Engine

[Open the complete example modules](../../examples/custom-render-engine/INDEX.md).



### GPU Render Engine 

```python
import bpy

class CustomGPURenderEngine(bpy.types.RenderEngine):
    bl_idname = "CUSTOM_GPU"
    bl_label = "Custom GPU"

    ### Request a GPU context to be created and activated for the render method.
    ### This may be used either to perform the rendering itself, or to allocate
    ### and fill a texture for more efficient drawing.
    bl_use_gpu_context = True

    def render(self, depsgraph):
        ### Lazily import GPU module, since GPU context is only created on demand
        ### for rendering and does not exist on register.
        import gpu

        ### Perform rendering task.
        pass

def register():
    bpy.utils.register_class(CustomGPURenderEngine)

def unregister():
    bpy.utils.unregister_class(CustomGPURenderEngine)

if __name__ == "__main__":
    register()
```

base class — bpy_struct

subclasses —
HydraRenderEngine

[Related references](INDEX.md).
