# Keyframe and action construction

Run in Blender with an active object. Each code block demonstrates an alternative way to key its Z location.

```python
import bpy

obj = bpy.context.object
obj.location[2] = 0.0
obj.keyframe_insert(data_path="location", frame=10.0, index=2)
obj.location[2] = 1.0
obj.keyframe_insert(data_path="location", frame=20.0, index=2)
```

Using low-level functions:

```python
import bpy

obj = bpy.context.object

### Create the action, with a slot for the object, a layer, and a keyframe strip:
action = bpy.data.actions.new(name="MyAction")
slot = action.slots.new(obj.id_type, obj.name)
strip = action.layers.new("MyLayer").strips.new(type='KEYFRAME')

### Create a channelbag to hold the F-Curves for the slot:
channelbag = strip.channelbag(slot, ensure=True)

### Create the F-Curve with two keyframes:
fcu_z = channelbag.fcurves.new(data_path="location", index=2)
fcu_z.keyframe_points.add(2)
fcu_z.keyframe_points[0].co = 10.0, 0.0
fcu_z.keyframe_points[1].co = 20.0, 1.0

### Assign the action and the slot to the object:
adt = obj.animation_data_create()
adt.action = action
adt.action_slot = slot
```

[Related references](INDEX.md).
