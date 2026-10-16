# Blender as a Python Module: Use Cases, Usage

## Blender as a Python Module

### Blender as a Python Module

You can compile Blender into a Python module, which then lets
import bpy slot into any Python script and unlock Blender's capabilities.

Note

You won't find the Blender as a Python Module build listed among the official downloads on Blender's site.

- You can pull a ready-built bpy module
straight from PIP.

- Alternatively, build it from source by following the
build instructions.

### Use Cases

A Python developer might want to fold Blender scripts into projects whose focus lies elsewhere than Blender.

A few of the possibilities it opens up:

- Turning datasets into rendered stills and animations.

- Running images through Blender’s compositor.

- Cutting video by way of Blender’s sequencer.

- Converting between 3D file formats.

- Development work, such as reaching bpy from Python IDEs and debugging tools.

- Automation.

### Usage

By and large, treating Blender as a Python module mirrors running a script in background-mode
(the one you get by passing the command-line arguments --background or -b ),
yet a few distinctions are worth keeping in mind.

Blender’s Executable Access
The bpy.app.binary_path attribute starts out as an empty string.

Should you want it aimed at a known executable, you are free to assign the value.

The snippet below hunts for the binary and assigns it once located:

```python
import bpy
import shutil

blender_bin = shutil.which("blender")
if blender_bin:
   print("Found:", blender_bin)
   bpy.app.binary_path = blender_bin
else:
   print("Unable to find blender!")
```

[Related references](INDEX.md).
