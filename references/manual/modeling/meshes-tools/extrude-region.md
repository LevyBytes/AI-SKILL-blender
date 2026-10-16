# Extrude Region

## Extrude Region

Extrude Region

Mode: Edit Mode
Toolbar: Extrude Region
Shortcut: E

Extrusion duplicates vertices while maintaining connectivity to original geometry. Vertices become edges; edges become faces. This is a core operation for building new mesh topology.

You can create boxes from squares, cylinders from circles, and tree branches or organic structures. The extrusion direction is interactive and defaults to the surface normal for faces. Extrusion can be restricted to a single axis (see Axis Locking).

Different extrusion tools vary in how new geometry connects internally. The border loop of the selection extrudes while the interior stays in place.

The Algorithm

Extrude operates through several steps:

First, the algorithm finds the outer edge boundary of the extrusion region. By default, edges belonging to two or more selected faces are treated as internal and excluded from the boundary.

Boundary edges are converted to faces.

If boundary edges belong to only one face in the entire mesh, all selected faces are duplicated and linked to the new faces (producing boxes from rectangles, for example).

Otherwise, selected faces link to new faces without duplication, preventing unwanted interior faces in the result.

For fully closed volumes (like a cube with all six faces), extrusion simply duplicates the volume without connecting it to the original.

Edges in "open" loops (not part of selected faces) are duplicated, with a new face created between the original and duplicate edge.

Single isolated vertices duplicate and form a new edge between the original and new vertex.

[Related references](INDEX.md).
