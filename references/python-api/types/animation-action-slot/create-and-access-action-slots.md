# Create and access action slots

Start with an object named Suzanne. Keyframe insertion creates an action and slot automatically.

```python
import bpy

# Assume Suzanne mesh is present in the scene.
suzanne = bpy.data.objects["Suzanne"]

# Create animation data and an action for Suzanne:
# Slot will be automatically created.
suzanne.keyframe_insert("location", index=0)

# Action slots can be accessed like this:
action = suzanne.animation_data.action
for slot in action.slots:
    print(f"Slot Identifier {slot.identifier!r} "
          f"with name {slot.name_display!r} "
          f"targets ID type {slot.target_id_type!r}")
```

[Related references](INDEX.md).
