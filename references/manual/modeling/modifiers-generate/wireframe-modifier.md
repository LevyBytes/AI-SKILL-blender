# Wireframe Modifier

## Wireframe Modifier

### Wireframe Modifier

Turning a mesh into a wireframe is the job of the Wireframe modifier: it steps through every face, collects all the edges it finds, and swaps each edge out for a four-sided polygon. Bear in mind this only functions on a mesh that actually has faces. The thickness, the assigned material, and a number of further traits of the wireframe it builds can all be driven on the fly through the modifier's settings.

### Options

The Wireframe modifier.

Thickness
How thick the wireframe bars are.

Offset
A figure from -1 to 1 that decides whether the wireframes form on the inside or the outside of the original mesh.
At zero, Offset sits the wireframes centered on the original edges.

Boundary
Builds wireframes along the boundaries of mesh islands.

Replace Original
Turn this on and the source mesh gives way to the wireframe that was built.
Leave it off and the wireframe sits over the top of it instead.

Thickness

Even
Holds thickness steady by compensating at sharp corners.
This can sharpen quality in places, at the price of longer computation.

Relative
Sets each edge's thickness from how long that edge is, so longer edges come out thicker.

Crease Edges
Meant to pair with
the Subdivision modifier.
Switch it on to crease edges at their junctions, heading off broad curved intersections.

Crease Weight
Controls the crease applied at junction edges, from 0 (none) up to 1 (full).

Material Offset
Picks the named material index to use for the wireframe,
applied as an offset counted from the first material.

Warning

Wireframe thickness is only an estimate. Even Thickness does fine much of the time, yet
narrow faces can throw off unsightly spikes. When that happens, either ease the steep angles out of the geometry
or turn the Even Thickness option off.

### Vertex Group

Each weight in the chosen vertex group is multiplied against the Thickness,
which makes lower-weighted vertices come out thinner. Any vertex left out
of the group behaves as though its weight were zero.

Invert
Flips the vertex group weights so the weight actually applied becomes one minus the real weight.

Factor
The degree to which the vertex weights count toward the result.

- At 0.0 , a zero-weight vertex ends up with no thickness whatsoever.

- At 0.5 , a zero-weight vertex comes out half as thick as a full-weight one.

- At 1.0 , weights drop out of the picture and Thickness applies to every vertex alike.

Note

Even where a vertex ends up at zero thickness, a wireframe is still produced.
That leaves duplicate geometry behind, which can occasionally call for extra attention.

### Examples

Wireframes on a displaced plane.

Here the wireframes are given a second, darker material, while the displaced plane keeps the one it started with.

Vertex group weighting.

The weights of the vertex group gradually change from 0 to 1.

Wireframe and Subdivision Surface modifier.

Cube with enabled Crease Edges option. The Crease Weight is set to 0, 0.5 and 1.

[Related references](INDEX.md).
