# Deleting & Dissolving: Limited Dissolve, Collapse Edges & Faces

### Limited Dissolve 

Reference

Mode :

Edit Mode

Menu :

Mesh ‣ Delete ‣ Limited Dissolve

Shortcut :

X or Delete

Trims the selected geometry by dissolving vertices and edges across flattish regions.

| Description | Description |
| --- | --- |
| Original mesh.  | Result of Limited Dissolve.  |

Max Angle
The largest angle between faces that still counts the surface as flat (and so dissolvable).
Specifically it's measured between face normals, so coplanar faces register as 0°, not 180°.

All Boundaries
Once the edges have dissolved per Max Angle , also dissolve every vertex at a boundary corner —
specifically, those with only two neighboring edges.

Delimit
Blocks merging across faces that differ in certain ways. Combine several of these by Shift - LMB
clicking them.

Normal :

Don't merge faces that have opposite
orientations.

Material :

Don't merge faces that have different materials.

Seam :

Don't dissolve edges that are marked as UV Seams.

Sharp :

Don't dissolve edges that are marked as Sharp.

UVs :

Don't merge faces that are disconnected in any UV map.

### Collapse Edges & Faces 

Reference

Mode :

Edit Mode

Menu :

Mesh ‣ Delete ‣ Collapse Edges & Faces

Shortcut :

X or Delete

Crushes each patch of connected edges and faces down to a single vertex — useful for collapsing
edge rings, for example.

| Description | Description |
| --- | --- |
| Selected edge rings.  | Edge rings collapsed.  |

Unlike the Dissolve operators, this one makes no n-gons and can add new vertices rather than only
removing old ones. The new vertices also pick up interpolated UVs, color attributes, and so on,
which makes it especially good for stripping detail by hand.

[Related references](INDEX.md).
