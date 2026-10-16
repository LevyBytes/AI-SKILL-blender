# Find action slot users

Call users() to find the data-blocks animated by each slot of an action.

```python
import bpy

# Iterate through all actions in the Blender data.
print("Action & slot users:")
for action in bpy.data.actions:
    for slot in action.slots:
        # Return the data-blocks that are animated by this slot of this action
        users = slot.users()
        print(f"{action.name:20} slot={slot.identifier:12s} users: {users}")
```

[Related references](INDEX.md).
