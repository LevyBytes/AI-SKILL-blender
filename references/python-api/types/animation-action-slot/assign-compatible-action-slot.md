# Assign a compatible action slot

Start with an object named Suzanne. Assign the action before reading action_suitable_slots; it contains only slots compatible with the animated data-block.

```python
import bpy

# Assume Suzanne mesh is present in the scene.
suzanne = bpy.data.objects["Suzanne"]

# Create an action with an object slot.
action = bpy.data.actions.new("SuzanneAction")
action.slots.new(id_type='OBJECT', name="Suzanne")

# If there are multiple slots on the Action, pick the first one that's compatible.
anim_data = suzanne.animation_data_create()
anim_data.action = action
assert anim_data.action_suitable_slots, "expecting at least one suitable slot"
anim_data.action_slot = anim_data.action_suitable_slots[0]
```

[Related references](INDEX.md).
