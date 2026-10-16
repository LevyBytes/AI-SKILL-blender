# Troubleshooting Errors & Crashes: Undo/Redo, Modifying Blender Data & Undo, Undo & Library Data, Abusing RNA property callbacks, Edit-Mode / Memory Access

### Undo/Redo

To stay safe, treat every undo and redo as invalidating all bpy.types.ID instances (Object, Scene, Mesh, Light, etc.), and of course all of their sub-data along with them.

The snippet below demonstrates how undo shifts where things sit in memory:

```pycon
>>> hash(bpy.context.object)
-9223372036849950810
>>> hash(bpy.context.object)
-9223372036849950810
```

Delete the active object, then undo:

```pycon
>>> hash(bpy.context.object)
-9223372036849951740
```

As said above, the one dependable way to keep a script stable is simply to avoid holding references to data while a person is working in Blender interactively.

Note

The modern undo/redo system no longer wipes every pointer without exception. Data that a given history step found unchanged — which, in ordinary use, is most of it — can stay put, and so its pointers can stay valid.

Keep in mind, though, that should you decide to lean on that behavior for whatever reason, there's no guarantee at all of safety or consistency — doing so is at your own risk.

#### Modifying Blender Data & Undo

As a rule, changing Blender data should always spawn an undo step. Skip it and you invite trouble, anywhere from a corrupt or broken undo stack to outright crashes on undo/redo.

That holds doubly when you edit Blender data inside operators.

#### Undo & Library Data

A nice property of Blender's library linking is that undo can skip diffing library data, on the premise that it stays static. Blender's own tools aren't permitted to alter library data — but Python doesn't impose that limit.

That can be handy at times, say a script that nudges material values. Yet you could also script library data into pointing at freshly made local data, which isn't supported: a later undo strips the local data while leaving the library still referencing it, and that will likely crash.

So treat editing library data as an advanced corner of the API, and only reach for it when you're sure of what you're doing.

### Abusing RNA property callbacks

RNA properties defined in Python can carry custom callbacks. Doing anything heavy from inside one — calling an operator, for instance — might work, but it's neither officially advised nor supported.

Chiefly it's because such callbacks are supposed to be very fast; on top of that, code like this can, for instance, tangle up undo/redo (a history step gets stored by most operators, and the same happens when you edit an RNA property), kick off never-ending update cycles, and the like.

### Edit-Mode / Memory Access

Switching mode with bpy.ops.object.mode_set(mode='EDIT') or bpy.ops.object.mode_set(mode='OBJECT') relocates an object's data, so any references you held to a mesh's vertices/polygons/UVs, an armature's bones, a curve's points, and so on, can't be used once the mode flips.

It's only the reference to the data itself that you can fetch again; the snippet below will crash.

```python
mesh = bpy.context.active_object.data
polygons = mesh.polygons
bpy.ops.object.mode_set(mode='EDIT')
bpy.ops.object.mode_set(mode='OBJECT')

### This will crash!
print(polygons)
```

That's why, after a mode switch, you have to re-fetch any object-data variables; the version below shows how to dodge the crash above.

```python
mesh = bpy.context.active_object.data
polygons = mesh.polygons
bpy.ops.object.mode_set(mode='EDIT')
bpy.ops.object.mode_set(mode='OBJECT')

### Polygons have been re-allocated.
polygons = mesh.polygons
print(polygons)
```

[Related references](INDEX.md).
