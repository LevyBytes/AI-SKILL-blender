# bpy.types.Mesh: overview

class bpy.types. Mesh ( ID )

A data-block that holds the geometric surfaces of a mesh
## See also

- [Bpy Struct](../data-types-bpy-struct/INDEX.md)
## Mesh(ID)

### Mesh(ID)
### Mesh Data

You reach the mesh data in object mode; it is laid out for tight storage, and when you need more flexible mesh editing from Python, reach for bmesh instead.

Four primary arrays hold the geometry of a Blender mesh.

- Mesh.vertices (each a point located in space)

- Mesh.edges (each pointing at a pair of vertices)

- Mesh.loops (each pointing at one vertex plus one edge)

- Mesh.polygons: (each pointing at a span of loops)

A polygon points at a span within the loop array; because of this it holds neither vertices nor corner data such as UVs on its own, just references to the loops it spans.

Since Mesh.loops, Mesh.uv_layers and Mesh.vertex_colors share the same alignment, one set of polygon loop indices retrieves the UVs and vertex colors just as it retrieves the vertices.

To compare mesh API options see: NGons and Tessellation Faces

The script below walks each polygon and prints its vertices and UVs; it assumes the active object is a mesh that has UVs.

```python
import bpy

me = bpy.context.object.data
uv_layer = me.uv_layers.active.data

for poly in me.polygons:
    print("Polygon index: {:d}, length: {:d}".format(poly.index, poly.loop_total))

    # Range is used here to show how the polygons reference loops,
    # for convenience 'poly.loop_indices' can be used instead.
    for loop_index in range(poly.loop_start, poly.loop_start + poly.loop_total):
        print("    Vertex: {:d}".format(me.loops[loop_index].vertex_index))
        print("    UV: {!r}".format(uv_layer[loop_index].uv))
```

base classes: bpy_struct, ID

[Related references](INDEX.md).
