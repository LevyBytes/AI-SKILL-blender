# Quickstart: Operators (Tools), Operator Poll(), Integration, Example Operator

Keep in mind context is read-only, so you can't assign to these values straight away. Changing them instead happens by invoking API functions or by reaching through the data API.

That's why bpy.context.active_object = obj throws an error, whereas bpy.context.view_layer.objects.active = obj behaves just fine.

Which context attributes exist shifts according to where you read them from. Members available in the 3D Viewport differ from those in the Python Console, so be mindful of the user's current state when you pull a context attribute.

See bpy.context API reference.

### Operators (Tools)

Operators are the tools a user normally triggers from buttons, menu entries, or shortcut keys. They look like tools from the user's side, but Python can fire them off with custom settings by way of the bpy.ops module.

Examples:

```pycon
>>> bpy.ops.mesh.flip_normals()
{'FINISHED'}
>>> bpy.ops.mesh.hide(unselected=False)
{'FINISHED'}
>>> bpy.ops.object.transform_apply()
{'FINISHED'}
```

Tip

The Operator Cheat Sheet lays out every operator alongside its default values in Python form, together with the auto-generated docs. It's a handy way to survey the full set of Blender operators at a glance.

#### Operator Poll()

A lot of operators carry a "poll" function that verifies the cursor sits in a suitable area or the object is in the right mode (Edit Mode, Weight Paint Mode, and similar). Should that poll function fail while called from Python, an exception gets thrown.

For instance, running bpy.ops.view3d.render_border() from the console produces this error:

```text
RuntimeError: Operator bpy.ops.view3d.render_border.poll() failed, context is incorrect
```

Here the context needs to be the 3D Viewport together with an active camera.

Rather than wrapping every operator call in a try-except block, you can first invoke the operator's own poll() function to find out whether it's able to run in the present context.

```python
if bpy.ops.view3d.render_border.poll():
    bpy.ops.view3d.render_border()
```

### Integration

Python scripts have several routes for plugging into Blender:

- by defining a render engine;

- by defining operators;

- by laying out panels, headers, and menus;

- by adding fresh buttons onto panels, headers, and menus that already exist.

However you go about it, in Python the mechanism is the same: you author a class that subclasses one of the types Blender already provides.

### Example Operator

[Related references](INDEX.md).
