# Internal Data & Their Python Objects: Stale Data, No updates after setting values, No updates after changing UI context, Can I redraw during script execution?

```python
### Typical name lookup, could be local or library.
obj = bpy.data.objects["my_obj"]

### Library object name lookup using a pair,
### where the second argument is the library path matching bpy.types.Library.filepath.
obj = bpy.data.objects["my_obj", "//my_lib.blend"]

### Local object name look up using a pair,
### where the second argument excludes library data from being returned.
obj = bpy.data.objects["my_obj", None]

### Both the examples above also work for `get`.
obj = bpy.data.objects.get(("my_obj", None))
```

### Stale Data

### No updates after setting values

There are times you set a value from Python and want to read the updated result straight away, e.g: after changing an object's bpy.types.Object.location you might reach for its transform immediately via bpy.types.Object.matrix_world, only to find it doesn't behave as you'd hope. Changes to the UI have comparable issues, covered in the next section.

Consider all the inputs that may shape where an object finally ends up, among them:

- F-curves driving animation.

- Drivers, along with the Python expressions behind them.

- Constraints

- The parents of the object — and in turn their constraints, F-Curves, and the rest.

To avoid pricey recomputation every time a property changes, Blender holds off on evaluating until the result is actually needed. While your script runs, though, you may want the fresh values right away. For that, call bpy.types.ViewLayer.update once you've changed values, for example:

```python
bpy.context.object.location = 1, 2, 3
bpy.context.view_layer.update()
```

Once that runs, every piece of dependent data — modifiers, drivers, child objects and the like — gets recalculated for the active view layer and is then there for the script to read.

### No updates after changing UI context

Much like the previous case, some UI changes don't take effect at once. Setting bpy.types.Window.workspace, for instance, appears to do nothing in the code right after it (bpy.types.Window.workspace still reads the same), yet the UI does end up reflecting the change. A few of the properties that act this way are:

- bpy.types.Window.workspace

- bpy.types.Window.screen

- bpy.types.Window.scene

- bpy.types.Area.type

- bpy.types.Area.ui_type

Changes like these reshape the UI, and with it the context (bpy.context), quite sharply. That can wreck Blender's context handling. So Blender postpones the change until after operators have finished and just before the UI redraws, which keeps the context switch safe.

When your code depends on running against an updated context, the way around it is to defer that code's execution too. Some options:

- Modal Operator.

- bpy.app.handlers.

- bpy.app.timers.

You can also tie it to drawing callbacks, but that's usually best steered clear of: if a hidden panel, cursor, region or similar fails to draw, your script could turn unreliable.

### Can I redraw during script execution?

The official line on this is no — or, put another way, "You don't want to do that". For some background on why:

For the duration of a script's run, Blender sits and waits for it to finish, effectively locked until it's done; in that state Blender neither redraws nor reacts to user input. Usually that's no great hardship, since the scripts shipped with Blender tend to be short-lived — yet a script can take a while, and it'd be pleasant to watch progress in the viewport.

Tools that pin Blender inside a redraw loop are firmly discouraged, because they fight against Blender's capacity to juggle several operators at once and to refresh different bits of the interface while a tool runs.

The answer here, then, is to write a modal operator — one that supplies a modal() function; the text editor ships a template for exactly this. Such operators fire on user input, or set up their own timers to run at intervals; they can consume the events or let them fall through to the keymap or to other modal operators. Transform, Painting, Fly Navigation and File Select are all examples of modal operators.

Authoring a modal operator takes more effort than a bare for loop crammed with draw calls, yet it's the more flexible choice and meshes far more cleanly with how Blender is built.

Fine, fine — drawing from Python anyway

Should you insist, then yes, the trick exists — but any script relying on it is barred from being bundled with Blender, won't have its resulting issues counted as bugs, and carries no guarantee of still working in later releases.

[Related references](INDEX.md).
