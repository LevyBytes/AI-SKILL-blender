# bpy.types.Object: overview

class bpy.types. Object ( ID ) 

A data-block that describes an object inside a scene
### Object(ID)
### Basic Object Operations Example 

The snippet below walks through the everyday handling of an object: building a
new one, dropping it into a view layer, selecting it, and setting it active.

```python
import bpy

view_layer = bpy.context.view_layer

### Create new light data-block.
light_data = bpy.data.lights.new(name="New Light", type='POINT')

### Create new object with our light data-block.
light_object = bpy.data.objects.new(name="New Light", object_data=light_data)

### Link light object to the active collection of current view layer,
### so that it'll appear in the current scene.
view_layer.active_layer_collection.collection.objects.link(light_object)

### Place light to a specified location.
light_object.location = (5.0, 5.0, 5.0)

### And finally select it and make it active.
light_object.select_set(True)
view_layer.objects.active = light_object
```

base classes: bpy_struct, ID

- WORLD
World Space – Blender's outermost, most global space.

- POSE
Pose Space – A bone's pose space, equivalent to its armature's object space.

- `LOCAL_WITH_PARENT`
Local With Parent – A bone's rest-pose local space, carrying parent transforms within the matrix.

- LOCAL
Local Space – The local space belonging to an object or bone.

- to_space ( Literal [ 'WORLD' , 'POSE' , '`LOCAL_WITH_PARENT`' , 'LOCAL' ] ) – The space to which you want to transform ‘matrix’ (optional)

- WORLD
World Space – Blender's outermost, most global space.

- POSE
Pose Space – A bone's pose space, equivalent to its armature's object space.

- `LOCAL_WITH_PARENT`
Local With Parent – A bone's rest-pose local space, carrying parent transforms within the matrix.

- LOCAL
Local Space – The local space belonging to an object or bone.

Returns :

The transformed matrix (multi-dimensional array of 4 * 4 items, in [-inf, inf])

Return type :

mathutils.Matrix

[Related references](INDEX.md).
