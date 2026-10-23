# Quickstart: Custom Properties, Context

```pycon
>>> bpy.types.Mesh()
Traceback (most recent call last):
File " ", line 1, in
TypeError: bpy_struct.__new__(type): expected a single argument
```

That restriction is deliberate. Blender's Python API won't let you make Blender data that lives outside the central Blender database (reached via bpy.data), since Blender itself looks after that data across save, load, undo, append, and so on.

Adding and removing data happens through methods on the bpy.data collections, for instance:

```pycon
>>> mesh = bpy.data.meshes.new(name="MyMesh")
>>> print(mesh)
```

```pycon
>>> bpy.data.meshes.remove(mesh)
```

#### Custom Properties

From Python you can attach properties to any data-block carrying an ID (data that gets linked in and shows up under bpy.data). You're free to choose your own property names when assigning; they spring into existence as required, or replace an existing one of the same name.

Such data rides along in the blend-file and travels with copied objects, for example:

```python
bpy.context.object["MyOwnProperty"] = 42

if "SomeProp" in bpy.context.object:
    print("Property found")

### Use the get function like a Python dictionary
### which can have a fallback value.
value = bpy.data.scenes["Scene"].get("test_prop", "fallback value")

### Dictionaries can be assigned as long as they only use basic types.
collection = bpy.data.collections.new("MyTestCollection")
collection["MySettings"] = {"foo": 10, "bar": "spam", "baz": {}}

del collection["MySettings"]
```

Keep in mind that what you store here is limited to the elementary Python types:

- the scalars int, float and string;

- an array whose entries are all ints, or all floats;

- a dictionary: its keys have to be strings, and its values likewise must stay within these basic types.

Their reach extends beyond Python itself: such properties can feed animation curves or turn up inside driver paths.

For the set of types that allow custom properties, refer to: types supporting custom properties.

### Context

Pulling data straight by name or as a list has its place, yet far more often you'll want to act on whatever the user has selected. That's where context comes in: it's always reachable through bpy.context and hands you the active object, scene, tool settings, plus a wide range of other attributes.

A few typical situations:

```pycon
>>> bpy.context.object
>>> bpy.context.selected_objects
>>> bpy.context.visible_bones
```

[Related references](INDEX.md).
