# Tips And Tricks: Use the Terminal, Interface Tricks, Access Operator Commands, Access Data Path, Show All Operators, Use an External Editor, Executing External Scripts, Executing Modules

### Tips and Tricks

Below are a handful of pointers that may come in useful while you write scripts. A few are simply Python tricks you might not have considered applying to Blender; others are specific to Blender itself.

### Use the Terminal

It pays to keep a terminal handy when scripting in Python; not the embedded Python console, but the terminal application you use to launch Blender.

A terminal earns its keep in three main ways:

- You get to watch print() output as the script executes, which helps for inspecting debug info.

- The complete error traceback lands in the terminal, whereas Blender's interface won't always surface a report message for it (it depends on how the script was run).

- If a script drags on or you stumble into an infinite loop, hitting Ctrl - C in the terminal (Ctrl - Break on Windows) bails out of it early.

See also

Launching from the Command Line.

### Interface Tricks

### Access Operator Commands

As you may have spotted, the tooltip on menu entries and buttons carries the bpy.ops.[...] command that runs that button; a tidy (and not obvious) trick is that pressing Ctrl - C while hovering over any menu item or button copies that command onto the clipboard.

### Access Data Path

Working out the path from an ID data-block down to one of its settings isn't always straightforward, since the setting can be buried deep. A fast shortcut is to open the setting's context menu and pick Copy Data Path; when no full path can be produced, you just get the property name on its own.

Note

This relies on the same path-building machinery used for the animation paths behind bpy.types.FCurve.data_path and bpy.types.DriverTarget.data_path drivers.

### Show All Operators

Blender does record operators in the Info editor, but only those flagged with the REGISTER option, so the Info view doesn't get swamped with bpy.ops.view3d.smoothview and bpy.ops.view3d.zoom calls. For testing, though, it can help to watch every operator fire in a terminal; turn that on with the debug option, either by handing Blender the --debug-wm argument at startup or by flipping bpy.app.debug_wm to True while it's already running.

### Use an External Editor

Blender's text editor does fine for minor tweaks and dashing off tests, but it isn't fully featured, so on bigger projects you'll likely want a standalone editor or a Python IDE. You can edit a file externally while keeping the same text open in Blender, and it does function, just not ideally; so here are two ways to drive an external file from Blender. With the examples that follow you'll still need a text data-block inside Blender to kick things off, but it points at an external file instead of holding the code itself.

### Executing External Scripts

This amounts to the same thing as running the script directly, pointing at a script's path from a two-line block of code.

```python
filename = "/full/path/to/myscript.py"
exec(compile(open(filename).read(), filename, 'exec'))
```

Or perhaps, instead of an absolute path, you'd rather point at a script sitting relative to the blend-file itself.

```python
import bpy
import os

filename = os.path.join(os.path.dirname(bpy.data.filepath), "myscript.py")
exec(compile(open(filename).read(), filename, 'exec'))
```

### Executing Modules

Here's how you'd pull a script in as a module and then call a function from it.

```python
import myscript
import importlib

importlib.reload(myscript)
myscript.main()
```

[Related references](INDEX.md).
