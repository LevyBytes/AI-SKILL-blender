# Collision

## Collision

### Collision 

Two collision categories exist: inter-object and internal.
Clarification: collision calculations primarily target soft-body vertices.
Insufficient vertices restrict collision. Secondarily, edges and faces enhance calculations.

### Collisions with Other Objects 

Soft bodies need prerequisites for object collision:

- If Collision Collection is specified, the object must belong to it.

- The collision object must be a mesh.

- Activate Collision in Physics for the collision object.
The object may itself be a soft body.

### Examples 

A soft body cube colliding with a plane functions reasonably (Fig. A soft body cube colliding with a plane.), whereas a soft body plane passes through a cube without interaction (Fig. A soft body plane colliding with a cube, so no interaction at all.).

| Description | Description |
| --- | --- |
| A soft body cube colliding with a plane.  | A soft body plane colliding with a cube, so no interaction at all.  |

Why? Default calculation checks only soft-body plane vertices for cube collision.
Activate Collision: Face in Soft Body Edges to check plane-face-to-object collision—more expensive.

Understanding collision calculation enables optimization:

### Calculating Collisions 

Default soft-body simulation operates per-vertex. If soft-body vertices don't collide with the object, no interaction occurs.

The video below shows vertices colliding with a plane.
A vertex entering the zone between Outer and Inner experiences repulsion along the face normal.
Final position depends on acting forces. The example shows balanced gravity and repulsion (first vertex).
The Choke parameter in Soft Body Solver settings controls extraction speed.

See also

Download the blend-file.

Observe vertices traveling at varied speeds.
The rightmost vertices (fifth and sixth) exceed collision-zone passage speed due to default solver precision.
The fourth travels quickly; heavier mass breaches the inner zone. The first three collide correctly.

Configure collision in Soft Body Edges to include edges and faces via Collision Face and Edge options.
Different calculation checks whether edges/faces intersect the collision object; collision zones don't apply.

### Good Collisions 

Problematic collision setups may improve via:

- Soft bodies require more subdivisions than collision objects.
Add loop cuts strategically in high-collision regions.

- Check face normal orientation.

- Collision-object spikes might penetrate the soft body.

- Solver resolution must match soft-body vertex speed.
Lower Error Limit; carefully raise Min Step.

- Outer and Inner should be adequate; opposite-face zones shouldn't overlap, preventing conflicting forces.

- Strong forces demand large zones.

- Set Choke high (maximum if needed) for vertex repulsion difficulties.

- Face collision proves difficult and time-consuming. Avoid if possible.

Often, simplified collision-object meshes perform better, though difficulty arises with animated meshes.

### Self-Collisions 

See Self Collision settings for self-collision details.

[Related references](INDEX.md).
