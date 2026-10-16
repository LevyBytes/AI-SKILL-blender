# Boolean Modifier

## Boolean Modifier

The Boolean modifier combines multiple meshes using a Boolean operation (for example, applying the Intersection, Union, and Difference of a sphere and a cube).
Warning: only Manifold meshes are guaranteed to give proper results; non-manifold ones (especially meshes with holes) usually work but may produce odd glitches and artifacts, and the Manifold Solver won't work at all on non-manifold meshes.
Tip: if your objects show their edges (Properties ‣ Object ‣ Viewport Display, enable Wireframe), you'll see the edge-creation process as you move objects around; you can also enable X-Ray to see inside the objects.
See also Intersect (Boolean) for one-off Boolean operations within a mesh in Edit Mode.

Options:
Operation:
- Intersect: keep only the volume that's inside both the modified mesh and all the source meshes.
- Union: add the source meshes to the modified mesh while removing any interior faces.
- Difference: cut the source meshes out of the modified mesh.
Operand Type:
- Object: the source is a single mesh object.
- Collection: the source is a collection of any number of mesh objects; if the Solver is Float, the Intersect operation isn't allowed.
Object — the source mesh object.
Collection — the source collection; may be empty if the Solver is Exact, in which case the modifier simply removes the modified mesh's interior (self-intersecting) geometry.
Solver — the algorithm used to perform the Boolean operation.
- Float: a simple solver offering good performance but no support for overlapping geometry.
- Exact: a complex solver offering the best results with full support for overlapping geometry, but much slower.
- Manifold: usually the fastest solver, but only works on Manifold meshes (plus the special case of Difference with a plane).

Solver Options:
Materials (Exact solver) — the method for setting materials on the new faces.
- Index Based: map the source mesh's first material to the modified mesh's first, the second to the second, and so on; if a source face's material index exceeds the modified mesh's material-slot count, the modified mesh's first material is used.
- Transfer: use the same materials as the source mesh, adding new material slots to the modified mesh as needed, and for empty slots fall back to the source mesh's material index.
Self Intersection (Exact solver) — correctly handle self-intersection in the participating meshes, at the cost of performance.
Hole Tolerant (Exact solver) — optimize the Boolean output for non-manifold geometry at the cost of increased computation time; because of the performance impact, enable it only when the Exact solver shows errors with non-manifold geometry.
Overlap Threshold (Float solver) — the maximum distance between two faces to consider them overlapping; this helps work around the solver's limitation, and if the result still isn't as expected, try the Exact solver.

[Related references](INDEX.md).
