# bpy.app: bpy.app. driver_namespace

bpy.app. driver_namespace
Dictionary for the drivers namespace, editable in place, reset on file load (read-only).
Type: dict[str, Any]
File Loading & Order of Initialization: since drivers may be evaluated right after a blend-file loads, the driver name-space must be initialized beforehand. Do this by registering text data-blocks to run on startup, so the scripts execute before drivers are evaluated (see Text → Register in Blender's text editor).
Hint: you may prefer external files over Blender's text-blocks, using a text-block that executes an external file. This example runs driver_namespace.py from the same directory as the text-blocks' blend-file:
```python
import os
import bpy
blend_dir = os.path.normpath(os.path.join(__file__, "..", ".."))
bpy.utils.execfile(os.path.join(blend_dir, "driver_namespace.py"))
```
Using __file__ keeps the text resolving to the expected path even when library-linked from another file. Other ways to populate the driver name-space work but tend to be error-prone: the --python command-line argument often fails because the first evaluation looks up a function that doesn't exist yet, marking the driver invalid and stopping further evaluation; and populating it before the blend-file loads also fails, since opening a file clears the name-space. You can instead run a script via --python before the blend file that registers a load-post handler (bpy.app.handlers.load_post) to initialize the name-space — this works for background tasks but won't set up the name-space when opening the file from the file selector.

[Related references](INDEX.md).
