# Tips And Tricks: Use Blender without its User Interface, Use External Tools, Bundled Python & Extensions

See how the script gets reloaded each time; that's what forces the updated copy to be used, since otherwise the cached version sitting in sys.modules would stick around until Blender restarted.

What sets this apart from running the script outright is that it has to invoke a function within the module, main() in this case, though any function will do. One upside is that you can feed arguments into the function from this little script, which often comes in handy for quickly testing different settings.

The catch here is that the script needs to live on Python's module search path. Extending the search path isn't best practice, but for testing it's fine; the next example tacks the current blend-file's directory onto the search path and then brings the script in as a module.

```python
import sys
import os
import bpy

blend_dir = os.path.dirname(bpy.data.filepath)
if blend_dir not in sys.path:
   sys.path.append(blend_dir)

import myscript
import importlib
importlib.reload(myscript)
myscript.main()
```

### Use Blender without its User Interface

While you're developing scripts of your own, Blender's interface can become a nuisance; all the manual reloading, re-running, opening file imports, and so on piles on overhead. For scripts that don't need interaction, it can turn out faster to skip Blender's interface entirely and run the script from the command line.

```console
blender --background --python myscript.py
```

You'll probably want to launch it against a blend-file so the script has data to work with.

```console
blender myscene.blend --background --python myscript.py
```

Note

On some setups the Blender executable won't be found unless you give its location in full.

With the script ticking over nicely under background mode, your next concern is reading back what it produced; the right way to do that turns entirely on the task, though here are a few ideas:

- Render to an image, open it in an image viewer, and keep overwriting the same file each pass.

- Save out a fresh blend-file, or push the file through one of Blender's exporters.

- When the results lend themselves to text, print them or write them to a file.

Setting this up takes a moment, but it can repay the effort handsomely by trimming the turnaround on testing changes. You can even leave Blender re-running the script every few seconds with a viewer refreshing the output, so there's no need to step away from your editor to watch the changes.

### Use External Tools

When no off-the-shelf Python module covers the task at hand, it's worth remembering you can often have Python run an external command against your data and read the output back in.

Leaning on outside programs introduces an extra dependency and may narrow who can run the script, but for quickly rigging up your own custom pipeline or knocking out one-off scripts it can be very convenient.

A few examples:

- Drive Gimp in batch mode to run custom scripts for heavier image processing.

- Export 3D models out to external mesh-editing tools and then read the results back.

- Convert files into a recognizable format ahead of reading them.

### Bundled Python & Extensions

Blender's official releases from blender.org ship a full Python installation across every platform; the downside is that any extensions sitting in your system's own Python environment stay invisible to Blender.

There are a couple of ways around this:

- Delete Blender's Python subdirectory, at which point Blender drops back to the system's Python and uses that.

Your platform may require you to point explicitly at where your Python lives, by way of the PYTHONPATH environment variable, for example:

[Related references](INDEX.md).
