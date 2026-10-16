# File Paths & String Encoding

## File Paths & String Encoding

### File Paths & String Encoding

### Relative File Paths

The relative paths Blender uses don't sit well with the standard Python modules such as os and sys . To a built-in Python function, the leading // that Blender treats as the blend-file's directory means nothing.

You'll typically hit this when exporting a material that carries associated image paths:

```pycon
>>> bpy.path.abspath(image.filepath)
```

With Blender data drawn from linked libraries a snag appears: the path resolves relative to the library rather than to the blend-file currently open. If a data-block might originate in an external blend-file, supply the bpy.types.ID 's library argument.

```pycon
>>> bpy.path.abspath(image.filepath, library=image.library)
```

That hands back an absolute path you can feed to native Python modules.

### Unicode Problems

Python handles a wide range of encodings, so nothing stops you from authoring a script in latin1 or iso-8859-15 .
See PEP 263.

For Blender's Python API, though, that's a complication, because a .blend file carries no explicit encoding. To keep the headache away from Python integration and script writers, we've ruled that every string inside a blend-file must be UTF-8 , and ASCII-compatible at that. The upshot: assigning a string in some other encoding to, say, an object name throws an error.

Paths are the exception, because you can't simply pretend non-UTF-8 paths won't show up on a user's filesystem. That means even innocent-looking expressions can raise errors, e.g:

```pycon
>>> print(bpy.data.filepath)
UnicodeEncodeError: 'ascii' codec can't encode characters in position 10-21: ordinal not in range(128)
```

```pycon
>>> bpy.context.object.name = bpy.data.filepath
Traceback (most recent call last):
File " ", line 1, in
TypeError: bpy_struct: item.attr= val: Object.name expected a string type, not str
```

There are a couple of ways to route around filesystem-encoding snags:

```pycon
>>> print(repr(bpy.data.filepath))
```

```pycon
>>> import os
>>> filepath_bytes = os.fsencode(bpy.data.filepath)
>>> filepath_utf8 = filepath_bytes.decode('utf-8', "replace")
>>> bpy.context.object.name = filepath_utf8
```
Encoding and decoding Unicode is a deep subject with thorough Python documentation; to keep things brief, here are a few suggestions about encoding trouble:

- Stick with UTF-8 throughout, and when the input's encoding is a mystery, convert it to UTF-8.

- Rather than slicing file paths around as raw strings, lean on the os.path functions.

- For path work, prefer os.fsencode() or os.fsdecode() over Python's built-in string decoding calls.

- When you need to print a path or surface it in the interface, run it through repr(path) first,
or use "%r" % path via string formatting.

Note

Now and then the tidiest move is to dodge string-encoding problems entirely and operate on bytes instead of Python strings; reading input as binary data is often the simpler path, though you'll still need a plan for any strings you mean to hand to Blender — an approach taken by some importers.

[Related references](INDEX.md).
