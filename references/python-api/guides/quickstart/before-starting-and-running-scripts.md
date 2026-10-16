# Quickstart: Before Starting, Running Scripts, Key Concepts, Data Access, Accessing Data-Blocks

### Quickstart

For the most part this API has settled, though a handful of areas continue to receive additions and refinements.

What the Blender Python API lets you do:

- Reach into any data the interface touches (Scenes, Meshes, Particles, and so on).

- Adjust user preferences, keymaps, and themes.

- Invoke tools while supplying your own parameters.

- Build interface components like menus, headers, and panels.

- Author brand-new tools.

- Author tools that respond interactively.

- Add rendering engines that hook into Blender.

- Watch for changes on data and its properties.

- Register additional settings onto Blender's existing data.

- Render directly into the 3D Viewport from Python.

Features that aren't available (yet):

- Defining entirely new space types.

- Attaching custom properties to absolutely every type.

### Before Starting

The aim here is to get you oriented with Blender's Python API rather than to walk through every subject exhaustively.

A short rundown of things worth knowing in advance:

- Turn on Developer Extra and Python Tooltips.

- The Python Console shines for trying out single lines; its autocompletion lets you probe the API on the fly.

- Hovering over a button shows its Python attribute and operator name (once the option above is on).

- Right-clicking a button to open its context menu jumps straight to the matching page in this documentation (once enabled, as noted above).

- The text editor's template menu is a good source of ready-made Python examples.

- For a deeper look at the scripts shipped alongside Blender, check:

- scripts/startup/bl_ui for the user interface.

- scripts/startup/bl_operators for operators.

Where exactly these sit varies by platform; consult the directory layout docs.

### Running Scripts

When it comes to running Python, two routes dominate: the bundled text editor, or typing straight into the console. As space types, the editor and the console alike can be picked from the header. And rather than hand-arrange spaces for Python work yourself, just reach for the Scripting workspace over in the Topbar tabs.

In the text editor you can load .py files or drop them in from the clipboard, then try them out with Run Script. People generally lean on the Python Console for short snippets and quick experiments where the feedback is instant, though you can also paste whole scripts into it. Blender can run scripts from the command line as well, but that's not something you need in order to pick up scripting inside Blender.

### Key Concepts

### Data Access

#### Accessing Data-Blocks

Reaching Blender's data through the Python API mirrors how the animation system or the interface does it; the upshot is that whatever a button can change, Python can change too. To get at the data in the blend-file currently open, go through the bpy.data module. That gives you a way into library data, such as:

```pycon
>>> bpy.data.objects
```

```pycon
>>> bpy.data.scenes
```

[Related references](INDEX.md).
