# This is the method called by Blender for both final renders (F12) and
# small preview for materials, world and lights.
def render(self, depsgraph):
    scene = depsgraph.scene
    scale = scene.render.resolution_percentage / 100.0
    self.size_x = int(scene.render.resolution_x * scale)
    self.size_y = int(scene.render.resolution_y * scale)

    # Fill the render result with a flat color. The frame-buffer is
    # defined as a list of pixels, each pixel itself being a list of
    # R,G,B,A values.
    if self.is_preview:
        color = [0.1, 0.2, 0.1, 1.0]
    else:
        color = [0.2, 0.1, 0.1, 1.0]

    pixel_count = self.size_x * self.size_y
    rect = [color] * pixel_count

    # Here we write the pixel values to the RenderResult
    result = self.begin_result(0, 0, self.size_x, self.size_y)
    layer = result.layers[0].passes["Combined"]
    layer.rect = rect
    self.end_result(result)
