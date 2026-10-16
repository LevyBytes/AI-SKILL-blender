# bpy.types.ID: user_clear, user_remap, user_of_id

user_clear ( )

Drop a data-block's user count to zero so it goes unsaved, and the data is discarded at the next reload.

This function is for advanced use only, misuse can crash Blender since the user
count is used to prevent data being removed when it is used.

```python
### This example shows what _not_ to do, and will crash Blender.
import bpy

### Object which is in the scene.
obj = bpy.data.objects["Cube"]

### Without this, removal would raise an error.
obj.user_clear()

### Runs without an exception but will crash on redraw.
bpy.data.objects.remove(obj)
```
user_remap ( new_id )

Point every reference to this ID in the .blend file at the supplied replacement instead.

Parameters :

new_id (ID) – New ID to use (never None)
user_of_id ( id )

Count how many times this data-block points at the given ID.

Parameters :

id (ID) – ID to count usages (never None)

Returns :

Number of usages/references of given id by current data-block (in [0, inf])

Return type :

int

[Related references](INDEX.md).
