from .draw_data import CustomDrawData

# For viewport renders, this method is called whenever Blender redraws
# the 3D viewport. The renderer is expected to quickly draw the render
# with OpenGL, and not perform other expensive work.
# Blender will draw overlays for selection and editing on top of the
# rendered image automatically.
def view_draw(self, context, depsgraph):
    # Lazily import GPU module, so that the render engine works in
    # background mode where the GPU module can't be imported by default.
    import gpu

    region = context.region
    scene = depsgraph.scene

    # Get viewport dimensions
    dimensions = region.width, region.height

    # Bind shader that converts from scene linear to display space,
    gpu.state.blend_set('ALPHA_PREMULT')
    self.bind_display_space_shader(scene)

    if not self.draw_data or self.draw_data.dimensions != dimensions:
        self.draw_data = CustomDrawData(dimensions)

    self.draw_data.draw()

    self.unbind_display_space_shader()
    gpu.state.blend_set('NONE')
