# API Reference Usage: Copy Data Path, Indirect Data Access

```python
### Access the number of samples for the Cycles render engine.
bpy.context.scene.cycles.samples

### Access to the current weight paint brush size.
bpy.context.tool_settings.weight_paint.brush.size

### Check if the window is full-screen.
bpy.context.window.screen.show_fullscreen
```

So in places the data you're after sits buried, and reaching it means stepping through several layers of indirection. The property layout mirrors how Blender stores things internally in its C code — often sensible, yet not always matching the mental model you build from using Blender. Picking that up takes a while; the upside is it teaches you how Blender's data interlocks, which is worth understanding when you script.

Early on the recurring snag is simply not knowing how to reach a given piece of data. A handful of approaches help:

- Lean on the Python console's auto-complete to poke at properties.
This is somewhat unreliable but lets you read property values and set them to watch the effect interactively.

- Copy the data path straight out of the user interface.
Covered below under Copy Data Path.

- Walk the references in the documentation.
Covered below under Indirect Data Access.

### Copy Data Path

The tooltip already shows the Python string for a property, on the line beginning Python: ... . That spares you a trip to the API references just to learn the access path. The context menu also carries a copy data-path tool, which returns the route from a bpy.types.ID data-block down to its property.

For a worked example you'll grab the path to the Levels setting on the Subdivision Surface modifier. From the default scene open the Modifiers tab, then give the cube a Subdivision Surface modifier. Hover over the button marked Levels Viewport . Its tooltip reads bpy.types.SubsurfModifier.levels , yet what you're after is the route from the object to that property.

Note that what gets copied omits the bpy.data.collections["name"]. prefix. The reasoning: collection look-ups on every access aren't the norm, and most of the time you'll go through the context rather than addressing each bpy.types.ID instance by its name.

Enter the ID path bpy.context.active_object into a Python console. Keep the dot at the end and hold off on running it.

Now from the button's context menu pick Copy Data Path , then paste what you get into the console:

```python
bpy.context.active_object.modifiers["Subdivision"].levels
```

Hit Return and the current value 1 comes back. Next set it to 2:

```python
bpy.context.active_object.modifiers["Subdivision"].levels = 2
```

The change shows up at once both in the Subdivision Surface modifier's UI and on the cube itself.

### Indirect Data Access

This tougher example walks through reaching the texture on the active sculpt brush — say you want to tweak its contrast from Python.

- Open the default scene and switch on Sculpt Mode from the 3D Viewport header.

- In the Sidebar open the Texture subpanel under Brush Settings and add a fresh texture.
You'll notice the texture data-block menu offers few helpful links (check the tooltips to confirm).

- Since contrast isn't surfaced in the Sidebar, look at the texture through the
Properties Editor.

- Right-click the contrast field for its context menu and choose Online Python Reference .
That lands you on bpy.types.Texture.contrast , confirming contrast belongs to texture.

- To learn how the brush reaches the texture, look over the reference list down at the page's foot.
That list can run long, and identifying the correct entry sometimes takes a bit of guesswork, but in this instance it proves to be tool_settings.sculpt.brush.texture .

- You now have bpy.data.brushes["BrushName"].texture as the way to the texture, though indexing the brush by name is rarely what you want — the active brush is. So the following step is to check the references for where brushes come from.

At this point the Python console lets you assemble the chain of nested properties down to the brush texture's contrast:
Context ‣ Tool Settings ‣ Sculpt ‣ Brush ‣ Texture ‣ Contrast .

Because each step hands you its attribute, you can stitch the data path together in the Python console:

```python
bpy.context.tool_settings.sculpt.brush.texture.contrast
```

[Related references](INDEX.md).
