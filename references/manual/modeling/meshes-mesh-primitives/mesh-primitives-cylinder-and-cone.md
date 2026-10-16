# Mesh Primitives: Cylinder, Cone

### Cylinder

Builds a cylinder from two round ends and a band of vertical faces. Reach for it when modeling handles, rods, pillars, and barrels.

Vertices
How many vertices form each round end; more of them, smoother the profile.

Radius
End radius, center to rim.

Depth
The cylinder's height along Z.

Cap Fill Type
How the two ends are capped:

Nothing :

No caps, just the sides, so a tube. Good for pipes or hollow containers.

N-gon :

A single N-gon face per end.

Triangle Fan :

Triangles meeting at a shared central vertex, per end.

### Cone

Builds a cone or pyramid shape. It's the basis for spikes, traffic cones, or wizard hats, and dialing in a top radius gives you frustums (truncated cones) or plain pyramids.

Vertices
How many vertices form the round base (or the polygon base of a pyramid); more of them, smoother the curve.

Radius 1
Radius of the bottom circle, the cone's base.

Radius 2
Radius of the top circle. At 0 you get an ordinary pointed cone; above 0 it becomes a frustum.

Depth
The cone's height along Z.

Cap Fill Type
How the base is capped:

Nothing :

No bottom cap, just the sides. Good for open containers or hollow cones.

N-gon :

A single N-gon face.

Triangle Fan :

Triangles meeting at a shared central vertex.

Tip

For a pyramid, set Vertices to 4 and pick N-gon or Triangle Fan as the cap type. Keep Radius 2 at 0 so the top stays pointed.

[Related references](INDEX.md).
