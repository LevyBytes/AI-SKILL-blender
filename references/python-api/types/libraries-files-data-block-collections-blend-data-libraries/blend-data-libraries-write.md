# bpy.types.BlendDataLibraries: write

write ( filepath , datablocks , * , path_remap = 'NONE' , fake_user = False , compress = False ) 

Serialize a set of data-blocks into a blend file.

Note

Indirectly referenced data-blocks will be expanded and written too.

Parameters :

- filepath ( str | bytes ) – The path to write the blend-file.

- datablocks (set[bpy.types.ID]) – set of data-blocks.

- path_remap ( str ) – Optionally remap paths when writing the file:

- NONE No path manipulation (default).

- RELATIVE Remap paths that are already relative to the new location.

- `RELATIVE_ALL` Remap all paths to be relative to the new location.

- ABSOLUTE Make all paths absolute on writing.

- fake_user ( bool ) – When True, data-blocks will be written with fake-user flag enabled.

- compress ( bool ) – When True, write a compressed blend file.

```python
import bpy

filepath = "//new_library.blend"

### Write selected objects and their data to a blend file.
data_blocks = set(bpy.context.selected_objects)
bpy.data.libraries.write(filepath, data_blocks)

### Write all meshes starting with a capital letter and
### set them with fake-user enabled so they aren't lost on re-saving.
data_blocks = {mesh for mesh in bpy.data.meshes if mesh.name[:1].isupper()}
bpy.data.libraries.write(filepath, data_blocks, fake_user=True)

### Write all materials, textures and node groups to a library.
data_blocks = {*bpy.data.materials, *bpy.data.textures, *bpy.data.node_groups}
bpy.data.libraries.write(filepath, data_blocks)
```
write ( filepath , datablocks , * , path_remap = 'NONE' , fake_user = False , compress = False )
Writes data-blocks into a blend file.
Note: indirectly referenced data-blocks will be expanded and written too.
Parameters:
- filepath ( str | bytes ) – The path to write the blend-file.
- datablocks (set[bpy.types.ID]) – set of data-blocks.
- path_remap ( str ) – Optionally remap paths when writing the file:
- NONE No path manipulation (default).
- RELATIVE Remap paths that are already relative to the new location.
- `RELATIVE_ALL` Remap all paths to be relative to the new location.
- ABSOLUTE Make all paths absolute on writing.
- fake_user ( bool ) – When True, data-blocks will be written with fake-user flag enabled.
- compress ( bool ) – When True, write a compressed blend file.
```python
import bpy

filepath = "//new_library.blend"

# Write selected objects and their data to a blend file.
data_blocks = set(bpy.context.selected_objects)
bpy.data.libraries.write(filepath, data_blocks)

# Write all meshes starting with a capital letter and
# set them with fake-user enabled so they aren't lost on re-saving.
data_blocks = {mesh for mesh in bpy.data.meshes if mesh.name[:1].isupper()}
bpy.data.libraries.write(filepath, data_blocks, fake_user=True)

# Write all materials, textures and node groups to a library.
data_blocks = {*bpy.data.materials, *bpy.data.textures, *bpy.data.node_groups}
bpy.data.libraries.write(filepath, data_blocks)
```

[Related references](INDEX.md).
