# Quickstart: Internal Types, Mathutils Types, Animation

```python
### Setting multiple snap targets.
bpy.context.scene.tool_settings.snap_elements_base = {'VERTEX', 'EDGE'}

### Passing as an operator argument for report types.
self.report({'WARNING', 'INFO'}, "Some message!")
```

### Internal Types

bpy.types.bpy_struct backs Blender's data-blocks and collections, plus any data that carries its own attributes such as collections, meshes, bones, scenes, and the rest.

Two principal types wrap Blender's data: one stands in for data-blocks (referred to internally as bpy_struct), and the other for properties.

```pycon
>>> bpy.context.object
bpy.data.objects['Cube']
```

```pycon
>>> C.scene.objects
bpy.data.scenes['Scene'].objects
```

Because these types point back at Blender's own data, any edit you make to them shows up at once.

### Mathutils Types

The mathutils module exposes vectors, quaternions, Euler angles, matrices, and color types. Certain attributes, among them bpy.types.Object.location, bpy.types.PoseBone.rotation_euler, and bpy.types.View3DCursor.location, are surfaced as these dedicated math types, which combine and transform in many handy ways.

A sample of multiplying a matrix by a vector:

```python
bpy.context.object.matrix_world @ bpy.context.object.data.vertices[0].co
```

Note

mathutils types hold onto a reference back to Blender's internal data, so changes flow back to it.

Example:

```python
### Modifies the Z axis in place.
bpy.context.object.location.z += 2.0

### Location variable holds a reference to the object too.
location = bpy.context.object.location
location *= 2.0

### Copying the value drops the reference so the value can be passed to
### functions and modified without unwanted side effects.
location = bpy.context.object.location.copy()
```

### Animation

Python gives you two avenues for adding keyframes.

One keys the properties straight away, much as a user clicking the keyframe button would. The other has you assemble the curves and keyframe data by hand and then aim the path at the property. An example of each follows below, and in either case what gets keyed is the Z axis of whatever object is active.

Simple example:

[Related references](INDEX.md).
