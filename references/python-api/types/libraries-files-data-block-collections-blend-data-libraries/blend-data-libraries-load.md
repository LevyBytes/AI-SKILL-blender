# bpy.types.BlendDataLibraries: load ( filepath , * , link = False , pack = False , relative = False , set_fake = False , recursive = False , reuse_local_id = False , assets_only = False , clear_asset_data = False , create_liboverrides = False , reuse_liboverrides = False , create_liboverrides_runtime = False )

load ( filepath , * , link = False , pack = False , relative = False , set_fake = False , recursive = False , reuse_local_id = False , assets_only = False , clear_asset_data = False , create_liboverrides = False , reuse_liboverrides = False , create_liboverrides_runtime = False ) 

Open a context manager that grants access to 2 library objects on entry.
Each object has properties that map to bpy.data collections; the values are lists of names to acquire.

Parameters :

- filepath ( str | bytes ) – The path to a blend file.

- link ( bool ) – When False reference to the original file is lost.

- pack ( bool ) – If True, and link is also True, embed linked data-blocks into the current blend-file.

- relative ( bool ) – When True the path is stored relative to the open blend file.

- set_fake ( bool ) – If True, set fake user on appended IDs.

- recursive ( bool ) – If True, also make indirect dependencies of appended libraries local.

- reuse_local_id ( bool ) – If True, try to re-use previously appended matching ID on new append.

- assets_only ( bool ) – If True, only list data-blocks marked as assets.

- clear_asset_data ( bool ) – If True, clear the asset data on append (it is always kept for linked data).

- create_liboverrides ( bool ) – If True and link is True, liboverrides will
be created for linked data.

- reuse_liboverrides ( bool ) – If True and create_liboverride is True,
search for existing liboverride first.

- create_liboverrides_runtime ( bool ) – If True and create_liboverride is True,
create (or search for existing) runtime liboverride.

```python
import bpy

filepath = "//link_library.blend"

### Load a single scene we know the name of.
with bpy.data.libraries.load(filepath) as (data_src, data_dst):
    data_dst.scenes = ["Scene"]

### Load all meshes.
with bpy.data.libraries.load(filepath) as (data_src, data_dst):
    data_dst.meshes = data_src.meshes

### Link all objects starting with "A".
with bpy.data.libraries.load(filepath, link=True) as (data_src, data_dst):
    data_dst.objects = [name for name in data_src.objects if name.startswith("A")]

### Append everything.
with bpy.data.libraries.load(filepath) as (data_src, data_dst):
    for attr in dir(data_dst):
        setattr(data_dst, attr, getattr(data_src, attr))

### The loaded objects can be accessed from `data_dst` outside of the context
### since loading the data replaces the strings for the data-blocks or None
### if the data-block could not be loaded.
with bpy.data.libraries.load(filepath) as (data_src, data_dst):
    data_dst.meshes = data_src.meshes
### Now operate directly on the loaded data.
for mesh in data_dst.meshes:
    if mesh is not None:
        print(mesh.name)
```

[Related references](INDEX.md).
