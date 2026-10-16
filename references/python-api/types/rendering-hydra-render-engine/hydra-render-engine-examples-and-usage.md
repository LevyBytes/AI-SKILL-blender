# bpy.types.HydraRenderEngine: overview

class bpy.types. HydraRenderEngine ( RenderEngine )

Base class from USD Hydra based renderers
## HydraRenderEngine(RenderEngine)

### HydraRenderEngine(RenderEngine)

Base class for plugging USD Hydra renderers into Blender.
### USD Hydra Based Renderer

```python
import bpy

class CustomHydraRenderEngine(bpy.types.HydraRenderEngine):
    ### Identifier and name in the user interface.
    bl_idname = "CUSTOM_HYDRA_RENDERER"
    bl_label = "Custom Hydra Renderer"

    ### Name of the render plugin.
    bl_delegate_id = "HdCustomRendererPlugin"

    ### Use MaterialX instead of `UsdPreviewSurface` for materials.
    bl_use_materialx = True

    ### Register path to plugin.
    @classmethod
    def register(cls):
        ### Make `pxr` module available, for running as `bpy` PIP package.
        bpy.utils.expose_bundled_modules()

        import pxr.Plug
        pxr.Plug.Registry().RegisterPlugins(['/path/to/plugin'])

    ### Render settings that will be passed to the delegate.
    def get_render_settings(self, engine_type):
        return {
            'myBoolean': True,
            'myValue': 8,
            'aovToken:Depth': "depth",
        }

    ### RenderEngine methods for update, render and draw are implemented in
    ### HydraRenderEngine. Optionally extra work can be done before or after
    ### by implementing the methods like this.
    def update(self, data, depsgraph):
        super().update(data, depsgraph)
    ### Do extra work here.

    def update_render_passes(self, scene, render_layer):
        if render_layer.use_pass_z:
            self.register_pass(scene, render_layer, 'Depth', 1, 'Z', 'VALUE')

### Registration.
def register():
    bpy.utils.register_class(CustomHydraRenderEngine)

def unregister():
    bpy.utils.unregister_class(CustomHydraRenderEngine)

if __name__ == "__main__":
    register()
```

base classes — bpy_struct, RenderEngine

[Related references](INDEX.md).
