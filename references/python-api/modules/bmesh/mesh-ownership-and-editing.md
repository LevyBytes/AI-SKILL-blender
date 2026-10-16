# BMesh ownership, editing and tessellation

### Introduction 

This API grants access to Blender's internal mesh editing system, including geometry connectivity and
editing operations such as split, separate, collapse, and dissolve.
The exposed features closely match the C API,
providing Python access to the underlying functions used by Blender's mesh editing tools.

For a detailed explanation of BMesh data types and their relationships see:
BMesh Design Document.

Note

Disk and Radial data is not exposed by the Python API since this is for internal use only.

Warning

TODO items are…

- add access to BMesh walkers .

- add custom-data manipulation functions add, remove or rename.

### Example Script 

```python
### This example assumes we have a mesh object selected

import bpy
import bmesh

### Get the active mesh
me = bpy.context.object.data

### Get a BMesh representation
bm = bmesh.new()   # create an empty BMesh
bm.from_mesh(me)   # fill it in from a Mesh

### Modify the BMesh, can do anything here...
for v in bm.verts:
    v.co.x += 1.0

### Finish up, write the bmesh back to the mesh
bm.to_mesh(me)
bm.free()  # free and prevent further access
```

### Standalone Module 

The BMesh module is written to be standalone except for mathutils
which is used for vertex locations and normals.
The only other exception to this are when converting mesh data to and from bpy.types.Mesh.

### Mesh Access 

There are two ways to access BMesh data, you can create a new BMesh by converting a mesh from
bpy.types.BlendData.meshes or by accessing the current Edit-Mode mesh.
See: bmesh.types.BMesh.from_mesh() and bmesh.from_edit_mesh() respectively.

When explicitly converting from mesh data Python owns the data, that means that
the mesh only exists while Python holds a reference to it.
The script is responsible for putting it back into a mesh data-block when the edits are done.

Note that unlike bpy , a BMesh does not necessarily correspond to data in the currently open blend-file,
a BMesh can be created, edited and freed without the user ever seeing or having access to it.
Unlike Edit-Mode, the BMesh module can use multiple BMesh instances at once.

Take care when dealing with multiple BMesh instances since the mesh data can use a lot of memory.
While a mesh that the Python script owns will be freed when the script holds no references to it,
it's good practice to call bmesh.types.BMesh.free() which will remove all the mesh data immediately
and disable further access.

### Edit-Mode Tessellation 

When writing scripts that operate on Edit-Mode data you will normally want to re-calculate the tessellation after
running the script, this needs to be called explicitly.
The BMesh itself does not store the triangulated faces, instead they are stored in the bpy.types.Mesh,
to refresh tessellation triangles call bpy.types.Mesh.calc_loop_triangles().

[Related references](INDEX.md).
