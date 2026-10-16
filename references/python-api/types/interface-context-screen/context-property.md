# bpy.types.Context: Screen Context: property

property

Type :

AnyType | str | int

Fetches the property under whatever button the pointer is over.
Comes back as a tuple holding the data-block, the data path leading to the property, and an array index.

Note

If no bpy.types.ID is tied to the property, what you get back may be non-ID data.
That can happen when reaching into windowing data — operator properties, for instance.

```python
import bpy

### Example inserting keyframe for the hovered property.
active_property = bpy.context.property
if active_property:
    datablock, data_path, index = active_property
    datablock.keyframe_insert(data_path=data_path, index=index, frame=1)
```

[Related references](INDEX.md).
