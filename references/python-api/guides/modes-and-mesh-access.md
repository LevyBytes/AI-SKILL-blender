# Modes and Mesh Access

## Modes and Mesh Access

### Modes and Mesh Access

Working with mesh data, you can run into a script that misbehaves under Edit-Mode. The cause is that Edit-Mode keeps its own copy of the data, which only gets written back into the mesh when you leave Edit-Mode.

Take a common case: with the user in Edit-Mode, an exporter gets at the mesh via obj.data (a bpy.types.Mesh) — the data is there, but it's drifted out of sync with the live edit mesh.

When you hit this, your options are…

- Leave Edit-Mode first, then run the tool.

- Force the mesh to sync up with a call to bmesh.types.BMesh.to_mesh().

- Rework the script so it operates on the edit-mode data straight away, see: bmesh.from_edit_mesh().

- Flag the context as wrong, permitting the script only when outside Edit-Mode.

### N-Gons and Tessellation

N-gons have been supported since 2.63, which adds a wrinkle, because in certain situations (some exporters, say) you still need triangles.

Faces can now be reached three ways:

- bpy.types.MeshPolygon –
these days the structure storing faces in Object-Mode
(its accessor is mesh.polygons , not the old mesh.faces ).

- bpy.types.MeshLoopTriangle –
the product of tessellating polygons into triangles
(its accessor is mesh.loop_triangles ).

- bmesh.types.BMFace –
how the faces show up while in Edit-Mode.

In the documentation that follows, the three will be named polygons, loop triangles and BMesh-faces, in that order.

Faces carrying five or more sides are called ngons .

### Support Overview

| Usage | bpy.types.MeshPolygon | bpy.types.MeshLoopTriangle | bmesh.types.BMFace |
| --- | --- | --- | --- |
| Import/Create | Poor (inflexible) | Unusable (read-only) . | Best |
| Manipulate | Poor (inflexible) | Unusable (read-only) . | Best |
| Export/Output | Good (n-gon support) | Good (When n-gons cannot be used) | Good (n-gons, extra memory overhead) |

Note

The bmesh API stands entirely apart from bpy ; which one you pick usually comes down to how much editing you need, not merely a different doorway to the same faces.

### Creating

Faces can be built from any of the three data types:

- Polygons make faces with the least overhead, but the structure is stiff and unbending — every vertex and face has to be ready so you can create them all in one shot. It's made fiddlier still by the fact that a polygon doesn't carry its own vertices; instead it points at an index and a length in bpy.types.Mesh.loops , itself a fixed array.

- BMesh-faces are likely the easiest route to creating faces in new scripts: faces go in one by one, and the API is designed around mesh editing. Although bmesh.types.BMesh uses up more memory, processing just one mesh at any given moment keeps that under control.

### Editing

Of the three, editing is where they differ the most.

- Polygons are quite restricted for editing; swapping materials and toggling options like smooth works, but for anything beyond that they're too rigid and exist purely for storage.

- Loop-triangles shouldn't be used to edit geometry, since doing so tessellates any existing n-gons.

- BMesh-faces are comfortably the best choice for reshaping geometry.

### Exporting

All three can serve for export; the pick mostly turns on whether the destination format handles n-gons.

- Polygons give the most direct, efficient export, provided they map cleanly into the target format.

- Loop-triangles suit exporting to formats that lack n-gon support — in fact that's the one place their use is recommended.

- BMesh-Faces can export too, but may be overkill where polygons would do, since BMesh carries some overhead for not being the native storage in Object-Mode.

[Related references](INDEX.md).
