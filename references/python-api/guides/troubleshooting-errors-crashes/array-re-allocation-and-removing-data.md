# Troubleshooting Errors & Crashes: Array Re-Allocation, Removing Data, Unfortunate Corner Cases, Collection Objects, Data-Blocks Renaming During Iteration

The same class of problem can crop up for any function that relocates object data, though switching mode is where it shows up most.

### Array Re-Allocation

When you append new points onto a curve — or new vertices, edges or polygons onto a mesh — the internal array storing that data gets relocated by Blender.

```python
bpy.ops.curve.primitive_bezier_curve_add()
point = bpy.context.object.data.splines[0].bezier_points[0]
bpy.context.object.data.splines[0].bezier_points.add()

### This will crash!
point.co = 1.0, 2.0, 3.0
```

You can sidestep this by re-fetching the point variables after the new one goes in, or by keeping indices to the points rather than the point objects.

The cleanest fix, though, is to dodge the whole issue by adding every point to the curve in one go. Then there's no array re-allocation to worry about, and it's quicker as well, since rebuilding the entire array for each individual point is wasteful.

### Removing Data

After data is removed, reading or modifying it is off-limits. The rule spans constraints and modifiers, markers on the timeline, render layers, drivers and F-Curves, as well as bones, collections, scenes, objects, and the rest.

The remove() API calls deliberately invalidate whatever they free, heading off common slip-ups. The example below shows that safeguard in action:

```python
mesh = bpy.data.meshes.new(name="MyMesh")
### Normally the script would use the mesh here.
bpy.data.meshes.remove(mesh)
print(mesh.name)  # <- Give an exception rather than crashing:
```
```python
mesh = bpy.data.meshes.new(name="MyMesh")
vertices = mesh.vertices
bpy.data.meshes.remove(mesh)
print(vertices)  # <- This may crash.
```
### Unfortunate Corner Cases

On top of every expected case above, a handful of others ought to be fine but, owing to internal implementation quirks, currently aren't:

#### Collection Objects

Setting Object.hide_viewport , Object.hide_select or Object.hide_render kicks off a rebuild of the Collection caches, which derails any in-progress iteration over Collection.all_objects .

Do not:

```python
### `all_objects` is an iterator. Using it directly while performing operations on its members that will update
### the memory accessed by the `all_objects` iterator will lead to invalid memory accesses and crashes.
for object in bpy.data.collections["Collection"].all_objects:
     object.hide_viewport = True
```

Do:

```python
### `all_objects[:]` is an independent list generated from the iterator. As long as no objects are deleted,
### its content will remain valid even if the data accessed by the `all_objects` iterator is modified.
for object in bpy.data.collections["Collection"].all_objects[:]:
     object.hide_viewport = True
```

#### Data-Blocks Renaming During Iteration

Whenever a data-block reached through bpy.data has its name set, the collection re-sorts. So any loop walking data such as bpy.data.objects that also assigns names must grab every item from the iterator up front (usually by turning it into a list or tuple), or it risks skipping some objects and visiting others more than once.

[Related references](INDEX.md).
