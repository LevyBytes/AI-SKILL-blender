# Create an action slot manually

A slot targets a data-block type. Its identifier combines the type prefix and name; OBSuzanne and MESuzanne may coexist with the same display name.

```python
import bpy

# Actions creation.
action = bpy.data.actions.new("SuzanneAction")

# Creation of slots requires an ID type and a name.
slot = action.slots.new(id_type='OBJECT', name="Suzanne")
print(f"slot type={slot.target_id_type!r} "
      f"name={slot.name_display!r} "
      f"identifier={slot.identifier!r}")

# Output:
#   slot type=OBJECT name=Suzanne identifier=OBSuzanne
```

[Related references](INDEX.md).
