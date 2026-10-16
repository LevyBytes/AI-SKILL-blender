# Internal Data & Their Python Objects: Life-Time of Python Objects Wrapping Blender Data, Data Names, Naming Limitations, Library Collisions

## Internal Data & Their Python Objects

### Internal Data & Their Python Objects

Compared with ordinary Python data, the wrappers around Blender's internal data carry certain restrictions and constraints. This section collects the points that matter most.

### Life-Time of Python Objects Wrapping Blender Data

As a rule, the Python objects that stand in for (wrap) Blender data don't live long. They're spun up when something asks for them and torn down the moment Python stops using them.

The practical lesson: don't stash Python-only data on these objects whenever you need it to persist.

There are a few carve-outs. IDs, once they've made their Python instance, keep it and reuse it instead of minting a fresh Python object on every access. And a modal operator holds onto its instance for as long as it's running. But that's done for speed and counts as an internal implementation detail; leaning on it from Python for any purpose isn't recommended.

Beyond that, when Blender frees internal data it will try to invalidate whatever Python object it knows wraps that data. This isn't always possible, and the result can be an invalid memory access — one more argument for never keeping these around persistently in Python code. The troubleshooting crashes documentation covers this as well.

### Data Names

### Naming Limitations

It's a common mistake to expect newly made data to take precisely the name you requested. The bugs surface when you add data — typically during import — and later try to fetch it back by that name:

```python
bpy.data.meshes.new(name=meshid)

### Normally some code, function calls, etc.
bpy.data.meshes[meshid]
```

Or when assigning the name:

```python
obj.name = objname

### Normally some code, function calls, etc.
obj = bpy.data.meshes[objname]
```

Data names can diverge from the values you assigned if those run past the maximum length, are already taken, or are empty.

The better practice is to avoid name references for objects entirely; after creating the data, hold it in a dictionary, a list, on a class, or wherever suits — rarely is there cause to keep looking the same data up by name over and over.

If name references are genuinely necessary, your best bet is a dictionary mapping the imported assets' names to the newly created data; that way you avoid the risk of grabbing — or worse, mutating — data that already exists in the blend-file.

```python
### Typically declared in the main body of the function.
mesh_name_mapping = {}

mesh = bpy.data.meshes.new(name=meshid)
mesh_name_mapping[meshid] = mesh

### Normally some code, or function calls, etc.

### Use own dictionary rather than `bpy.data`.
mesh = mesh_name_mapping[meshid]
```

### Library Collisions

Data names are kept unique by Blender (bpy.types.ID.name), which stops you from accidentally handing the same name to two scenes, meshes, objects and so on. Pulling in library data from a separate blend-file, though, can throw up name collisions — yet another argument against addressing data by name.

It can get tricky, and Blender itself doesn't always resolve it correctly (when choosing the modifier object, say, you have no way to pick among several same-named objects); even so, it's worth heading the issue off here. Should you need to tell local data apart from library data, there's a facility on bpy.data members for it.

[Related references](INDEX.md).
