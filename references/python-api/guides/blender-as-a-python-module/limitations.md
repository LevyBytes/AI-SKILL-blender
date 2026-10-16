# Blender as a Python Module: Limitations

Blender’s Internal Modules
Blender bundles a number of modules, gpu and mathutils among them.
Be sure to import these only after bpy ; otherwise they will not be located.

Command Line Arguments Unsupported
Anything driven by command line arguments (which blender --help lists) is out of reach.

Usually that is no great loss, though a handful of command line arguments have no
counterpart in Blender's Python API ( --threads and --log being examples).

Note

These settings might gain exposure later on, if a need for them arises.

Resource Sharing (GPU)
It can happen that other Python modules grab the GPU in a manner that locks Blender/Cycles out of it.

Signal Handlers
Because Blender's usual signal handlers stay uninitialized, there is no dedicated handling of Control-C
to abort a render, and no crash log gets written should a crash occur.

Startup and Preferences
Loading the bpy module brings in the default startup scene
(rather than the “empty” blend-file you might assume), so a default cube, camera, and light are present.

To begin instead from a blank file, call: bpy.ops.wm.read_factory_settings(use_empty=True) .

To keep your local setup from coloring how the script runs, the user's startup and preferences are skipped.
The Python module acts just as though --factory-startup had been supplied as a command line argument.

Should you need them, the user's startup and preferences can be brought in through operators:

```python
import bpy

bpy.ops.wm.read_userpref()
bpy.ops.wm.read_homefile()
```

### Limitations

The bulk of Blender's constraints as an application carry over:

Reloading Unsupported
Trying to reload the bpy module through importlib.reload throws an exception
rather than reloading and resetting it.

To get the internal state back to a clean slate, reach for the bpy.ops.wm.read_factory_settings() operator instead.

Single Blend File Restriction
You can only have one .blend file open for editing at any moment.

Hint

As with the full application, nothing stops you from launching multiple instances at once,
each holding its own bpy and, by extension, its own Blender state.
For talking to those sub-processes more comfortably, Python ships the multiprocessing module.

For certain workflows the library API can stand in for spawning separate processes,
though it works by reading and writing ID data-blocks and therefore isn’t
a full replacement for opening .blend files, see:

- bpy.types.BlendDataLibraries.load()

- bpy.types.BlendDataLibraries.write()

- bpy.types.BlendData.temp_data()
supports a temporary data-context to avoid manipulating the current .blend file.

[Related references](INDEX.md).
