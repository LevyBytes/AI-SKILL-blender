# API Overview: Python in Blender, The Default Environment, Script Loading, Add-ons

## API Overview

### API Overview

What this page sets out to do is explain how Python and Blender mesh together, touching on parts of the functionality that the API references and example scripts don't make obvious on their own.

### Python in Blender

Blender carries an embedded Python interpreter, loaded the moment Blender starts and kept alive for as long as Blender runs. That interpreter executes the scripts that draw the user interface and powers several of Blender's internal tools as well.

The embedded interpreter offers a standard Python environment, so code from ordinary tutorials on writing Python scripts runs under it too. Blender exposes its own Python modules — bpy and mathutils among them — to that interpreter, so a script can import them and reach Blender's data, classes and functions. Any script touching Blender data has to import the relevant modules to function.

Here's a small example that shifts a vertex belonging to an object named "Cube":

```python
import bpy
bpy.data.objects["Cube"].data.vertices[0].co.x += 1.0
```

That edits Blender's internal data straight away. Run it in the interactive console and you'll watch the 3D Viewport refresh.

### The Default Environment

When you're writing your own scripts, it helps to know how Blender lays out its Python environment. Plenty of Python scripts ship with Blender and make good reference material, because they're written against the very same API that tool authors use. Scripts get put to work on all sorts of jobs: building the user interface, handling import/export, reshaping the scene, automating tasks, rolling your own tool set, and customization.

As it boots, Blender looks through scripts/startup/ for any Python modules there and imports each one. Where that folder actually lives will vary with your installation; the directory layout docs cover this.

### Script Loading

It may sound obvious, but it's worth flagging the gap between running a script directly and importing one as a module.

Extending Blender by running a script outright means the classes that script defines stay around inside Blender after it has finished. Used that way, getting back at those classes later — to unregister them, for instance — is harder than if you'd imported the script as a module. Import a script as a module and its class instances stay within the module, reachable again later by re-importing it.

For that reason it's preferable to steer clear of directly running scripts that extend Blender by registering classes.

Several routes let you run a script outright inside Blender:

- Open it in the text editor and hit Run Script .

- Type or paste it straight into the interactive console.

- Hand a Python file to Blender on the command line, e.g:

```console
blender --python /home/me/my_script.py
```

And to load them as modules:

- The obvious one: issuing import some_module from the interactive console or the text editor.

- Open it as a text data-block and tick the Register option, so it loads alongside the blend-file.

- Drop it into one of the scripts/startup directories, from where it's imported automatically at startup.

- Build it into an add-on; once that add-on is enabled it comes in as a module.

### Add-ons

Some of what Blender does is best left optional. Alongside the scripts loaded at startup sit add-ons, which keep to their own directory scripts/addons , and which only load at startup once you've ticked them in the user preferences.

What sets an add-on apart from an ordinary built-in Python module comes down to one requirement: it has to declare a bl_info variable. Blender pulls its metadata from there — the author, the project link, the category, the name — and the add-on list under User Preferences uses bl_info to present each add-on's details. The bl_info dictionary is documented under Add-ons.

[Related references](INDEX.md).
