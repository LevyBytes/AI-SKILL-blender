# BMesh attributes and valid mesh state

The snippets use a live BMesh named `bm`; the vertex-group example also needs its owning mesh object `obj`. Read [BMesh ownership, editing and tessellation](mesh-ownership-and-editing.md) to obtain and release that BMesh. UV and shape-key examples require the referenced layers to exist.

## BMesh Module (bmesh)

### BMesh Module (bmesh) 

This module provides access to Blender's bmesh data structures.
### CustomData Access 

BMesh has a unified way to access mesh attributes such as UVs, vertex colors, shape keys, edge crease, etc.
This works by having a layers property on BMesh data sequences to access the custom data layers
which can then be used to access the actual data on each vert, edge, face or loop.

Here are some examples:

```python
uv_lay = bm.loops.layers.uv.active

for face in bm.faces:
    for loop in face.loops:
        uv = loop[uv_lay].uv
        print("Loop UV: %f, %f" % uv[:])
        vert = loop.vert
        print("Loop Vert: (%f,%f,%f)" % vert.co[:])
```

```python
shape_lay = bm.verts.layers.shape["Key.001"]

for vert in bm.verts:
    shape = vert[shape_lay]
    print("Vert Shape: %f, %f, %f" % (shape.x, shape.y, shape.z))
```

```python
### In this example the active vertex group index is used,
### this is stored in the object, not the `BMesh`.
group_index = obj.vertex_groups.active_index

### Only ever one deform weight layer.
dvert_lay = bm.verts.layers.deform.active

for vert in bm.verts:
    dvert = vert[dvert_lay]

    if group_index in dvert:
        print("Weight %f" % dvert[group_index])
    else:
        print("Setting Weight")
        dvert[group_index] = 0.5
```

### Keeping a Correct State 

When modeling in Blender there are certain assumptions made about the state of the mesh:

- Hidden geometry isn't selected.

- When an edge is selected, its vertices are selected too.

- When a face is selected, its edges and vertices are selected.

- Duplicate edges / faces don't exist.

- Faces have at least three vertices.

To give developers flexibility these conventions are not enforced,
yet tools must leave the mesh in a valid state or else other tools may behave incorrectly.
Any errors that arise from not following these conventions is considered a bug in the script,
not a bug in Blender.

### Selection / Flushing 

As mentioned above, it is possible to create an invalid selection state
(by selecting a face and then deselecting one of its vertices for example),
mostly the best way to solve this is to flush the selection
after performing a series of edits. This validates the selection state.

[bmesh creation, edit-mode access and updates](create-access-and-update-mesh.md).

[Related references](INDEX.md).
