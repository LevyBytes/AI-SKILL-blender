# Glossary: Smoothing, Specular Light

Smoothing
Sets how Faces take their shading. A face is either solid, rendered flat, or smooth, where the normal is interpolated across every point of the face.

Specular Light
Light bounced back cleanly, mirror-fashion. The word also names the highlights seen on shiny surfaces.

SSS
Subsurface Scattering
The way light enters a translucent object's surface, bounces around inside the material, and leaves again somewhere else. Every non-metal is translucent to a degree, and substances like marble, skin, and milk simply cannot be rendered convincingly unless subsurface scattering is modeled.

Straight Alpha
See Alpha Channel.

Subdiv
Subdivision Surface
A way to derive a smooth, high-poly surface from a low-poly mesh fed in as the starting cage.

See also
Catmull-Clark subdivision surface
on Wikipedia.

Subdividing
A method that packs extra geometry into a mesh. Splitting an edge spawns new vertices, fresh edges link the splits, and new faces form around those edges; wherever two new edges intersect, another vertex appears at the crossing.

Swing
Swing and Twist
Breaking any rotation down into two single-axis rotations in sequence: first a swing that points a chosen axis at its target along the shortest path, then a twist spinning about that same axis.

You can reach this decomposition via Driver Variables and through inputs on the Transformation constraint. The Damped Track constraint yields a swing-only rotation.

In Quaternion form the swing always shows 0 in the X/Y/Z slot matching the chosen axis, while the twist always shows 0 in the remaining two.

Tail
One end-piece of a Bone, carrying X, Y, and Z coordinates expressed in the armature object's Local Space. Paired with the Head it sets a bone's local Y axis in Pose Mode. When drawn as an Octahedron it is the narrower of the two tips.

Tangent
A line touching a surface at a single point; a tangent runs perpendicular to a Normal.

Tessellation
Covering a plane with one or several geometric shapes, a process that usually yields Micropolygons.

Texture
A description of the visual patterns on a surface, also mimicking real physical surface structure.

Texture Space
The bounding box used when Generated mapping applies a Texture onto an image.

Timecode
An encoded track on videotape or film that records each frame's number and the time it was captured. Timecodes keep media in sync across separate recording devices, covering both audio and video.

Title Safe
The portion of the frame guaranteed to show on every device. Keep text and graphics within it so nothing gets clipped.

Topology
How a mesh's Vertices, Edges, and Faces are laid out to give it shape. See Vertex, Edge, and Face.

Transform
Transformation
Location, rotation, and scale taken together. It can be stated in World Space or in Local Space.

Transformation Matrix
The matrix standing in for an item's Transformation.

Triangle
A Face made of exactly three Vertices.

UV Map
A mapping that links a mesh's surface to a 2D texture; each mesh face corresponds to a face on the texture. Sending several mesh faces to the same or overlapping spots on the texture is both possible and routine.

Value
How bright a color is, from dark to light.

Vertex
Vertices
A single location-bearing point in 3D space. Vertices sit at the ends of Edges.

Vertex Group
A named set of Vertices. Such groups help confine an operation to chosen parts of a mesh.

Voxel
The volumetric cousin of the flat 2D pixel, a small cube. Its name fuses "Volumetric" with "Pixel." Blender uses voxels to hold smoke and fire data coming out of physics simulations.

[Related references](INDEX.md).
