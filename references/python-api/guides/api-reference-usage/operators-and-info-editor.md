# API Reference Usage: Operators, Info Editor

Or reach the brush directly:

```python
bpy.data.textures["Texture"].contrast
```

For a user-facing tool you'll generally route through bpy.context, since people expect the tool to act on whatever they've selected. Automation leans the other way toward bpy.data, because there you want to address and edit specific data no matter where the user's view happens to be.

### Operators

The bulk of Blender's buttons and hotkeys fire an operator, and those operators are exposed to Python through bpy.ops as well.

For the Python form, hover the button and read its tooltip, e.g Python: bpy.ops.render.render() . When no tooltip shows or the Python: line is absent, that button isn't backed by an operator and Python can't reach it.

To grab it for a script, hover the button and hit Ctrl - C , which copies it onto the clipboard. From the same button's context menu there's Online Python Reference too; that mostly enumerates the arguments and their defaults, and for Python-written operators it also names the file and line — useful if you want a look at the source.

Note

A Python call to certain operators won't accomplish anything useful;
the using operators section goes into this.

### Info Editor

Operators you run get logged by Blender and shown in the Info editor. Open the Scripting workspace that comes with Blender by default to view that log. Carry out a few actions and watch them appear — deleting a vertex, for instance.

Select any entry and copy it via Ctrl - C , usually so you can paste it into the Python console or text editor.

Note

Not every operator is recorded for display;
re-running a view zoom, say, isn't worth repeating, so it's left out.

To surface every operator that fires, see Show All Operators.

[Related references](INDEX.md).
