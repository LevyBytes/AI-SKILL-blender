# Object Modifier Type Items

Modify

| Value | Meaning |
| --- | --- |
| `GREASE_PENCIL_VERTEX_WEIGHT_PROXIMITY` | Vertex Weight Proximity.<br>Derive vertex weights from how far points sit from an object.<br>Modify |
| `DATA_TRANSFER` | Data Transfer.<br>Copy assorted data (vertex groups, UV maps, vertex colors, custom normals) across from one mesh onto another. |
| `MESH_CACHE` | Mesh Cache.<br>Drive the mesh from an external per-frame cache of vertex transforms. |
| `MESH_SEQUENCE_CACHE` | Mesh Sequence Cache.<br>Drive the mesh or curve from an external Alembic-format mesh cache. |
| `NORMAL_EDIT` | Normal Edit.<br>Adjust which way the surface normals point. |
| `WEIGHTED_NORMAL` | Weighted Normal.<br>Adjust the surface-normal directions through a weighting scheme. |
| `UV_PROJECT` | UV Project.<br>Cast UV coordinates onto the mesh from another object's negative Z axis. |
| `UV_WARP` | UV Warp.<br>Distort the UV map by the offset between a pair of objects. |
| `VERTEX_WEIGHT_EDIT` | Vertex Weight Edit.<br>Edit the weights belonging to a vertex group. |
| `VERTEX_WEIGHT_MIX` | Vertex Weight Mix.<br>Blend together the weights of a pair of vertex groups. |
| `VERTEX_WEIGHT_PROXIMITY` | Vertex Weight Proximity.<br>Drive a vertex group's weights from proximity to a target object. |
| `GREASE_PENCIL_COLOR` | Hue/Saturation.<br>Shift the strokes' hue, saturation, and value. |
| `GREASE_PENCIL_TINT` | Tint.<br>Apply a color tint to the strokes. |
| `GREASE_PENCIL_OPACITY` | Opacity.<br>Adjust how opaque the strokes are. |
| `GREASE_PENCIL_VERTEX_WEIGHT_ANGLE` | Vertex Weight Angle.<br>Derive vertex weights from the angle of a stroke. |
| `GREASE_PENCIL_TIME` | Time Offset.<br>Shift keyframes in time. |
| `GREASE_PENCIL_TEXTURE` | Texture Mapping.<br>Alter the UV texture values along strokes.<br>Generate |
| `ARRAY` | Array.<br>Lay out repeated copies of the shape at given offsets. |
| `BEVEL` | Bevel.<br>Produce angled corners by inserting geometry along the mesh's edges or vertices. |
| `BOOLEAN` | Boolean.<br>Bring in a second shape to cut, merge, or subtract from this one. |
| `BUILD` | Build.<br>Make the object's faces appear or vanish one by one as time passes. |
| `DECIMATE` | Decimate.<br>Thin out how dense the geometry is. |
| `EDGE_SPLIT` | Edge Split.<br>Break joined faces apart along their shared edges. |
| `NODES` | Geometry Nodes. |
| `MASK` | Mask.<br>Hide vertices on the fly using a vertex group or an armature. |
| `MIRROR` | Mirror.<br>Reflect across the local X, Y, and/or Z axes about the object origin. |
| `MESH_TO_VOLUME` | Mesh to Volume. |
| `MULTIRES` | Multiresolution.<br>Subdivide such that you can sculpt on the higher subdivision levels. |
| `REMESH` | Remesh.<br>Build fresh mesh topology from the existing shape. |
| `SCREW` | Screw.<br>Spin the input mesh as a profile around an axis. |
| `SKIN` | Skin.<br>Grow a solid form out of vertices and edges, with each vertex radius setting the thickness. |
| `SOLIDIFY` | Solidify.<br>Give the surface thickness. |
| `SUBSURF` | Subdivision Surface.<br>Break faces into finer pieces for a smoother look. |
| `TRIANGULATE` | Triangulate.<br>Turn every polygon into triangles. |
| `VOLUME_TO_MESH` | Volume to Mesh. |
| `WELD` | Weld.<br>Locate vertices nearer than dist and fuse them into one. |
| `WIREFRAME` | Wireframe.<br>Turn faces into thickened edge wireframe. |
| `GREASE_PENCIL_ARRAY` | Array.<br>Repeat strokes into an array. |
| `GREASE_PENCIL_BUILD` | Build.<br>Grease Pencil build modifier. |
| `GREASE_PENCIL_LENGTH` | Length.<br>Grease Pencil length modifier. |
| `LINEART` | Line Art.<br>Produce Line Art out of the scene's geometry. |
| `GREASE_PENCIL_MIRROR` | Mirror.<br>Mirror strokes to create duplicates. |
| `GREASE_PENCIL_MULTIPLY` | Multiple Strokes.<br>Surround each original stroke with extra strokes. |
| `GREASE_PENCIL_SIMPLIFY` | Simplify.<br>Cut down the point count to simplify a stroke. |
| `GREASE_PENCIL_SUBDIV` | Subdivide.<br>Grease Pencil subdivide modifier. |
| `GREASE_PENCIL_ENVELOPE` | Envelope.<br>Form an enveloping shape. |
| `GREASE_PENCIL_OUTLINE` | Outline.<br>Turn a stroke into its outline.<br>Deform |
| `ARMATURE` | Armature.<br>Drive the shape's deformation with an armature object. |
| `CAST` | Cast.<br>Nudge the shape toward one of the preset primitives. |
| `CURVE` | Curve.<br>Bend the mesh along a curve object. |
| `DISPLACE` | Displace.<br>Push vertices around according to a texture. |
| `HOOK` | Hook.<br>Move chosen points using a separate object. |
| `LAPLACIANDEFORM` | Laplacian Deform.<br>Reshape the mesh from a set of anchor points. |
| `LATTICE` | Lattice.<br>Deform following the form of a lattice object. |
| `MESH_DEFORM` | Mesh Deform.<br>Deform via another mesh that serves as a deformation cage. |
| `SHRINKWRAP` | Shrinkwrap.<br>Wrap the shape down onto another object. |
| `SIMPLE_DEFORM` | Simple Deform.<br>Reshape by twisting, bending, tapering, or stretching. |
| `SMOOTH` | Smooth.<br>Even out the mesh by softening the angles between neighboring faces. |
| `CORRECTIVE_SMOOTH` | Smooth Corrective.<br>Smooth the mesh yet keep its volume intact. |
| `LAPLACIANSMOOTH` | Smooth Laplacian.<br>Cut surface noise off a mesh while barely altering its form. |
| `SURFACE_DEFORM` | Surface Deform.<br>Carry motion over from a second mesh. |
| `WARP` | Warp.<br>Bend regions of a mesh to fresh positions with great freedom using two named objects. |
| `WAVE` | Wave.<br>Send a ripple-style motion through an object's geometry. |
| `VOLUME_DISPLACE` | Volume Displace.<br>Distort a volume using noise or another vector field. |
| `GREASE_PENCIL_HOOK` | Hook.<br>Move stroke points around with objects. |
| `GREASE_PENCIL_NOISE` | Noise.<br>Introduce noisy wobble into Grease Pencil strokes. |
| `GREASE_PENCIL_OFFSET` | Offset.<br>Alter a stroke's location, rotation, or scale. |
| `GREASE_PENCIL_SMOOTH` | Smooth.<br>Smooth out Grease Pencil strokes. |
| `GREASE_PENCIL_THICKNESS` | Thickness.<br>Alter how thick a stroke is. |
| `GREASE_PENCIL_LATTICE` | Lattice.<br>Deform strokes through a lattice object. |
| `GREASE_PENCIL_DASH` | Dot Dash.<br>Produce dot-and-dash patterned strokes. |
| `GREASE_PENCIL_ARMATURE` | Armature.<br>Move stroke points using an armature object. |
| `GREASE_PENCIL_SHRINKWRAP` | Shrinkwrap.<br>Wrap the shape down onto another object.<br>Physics |
| `CLOTH` | Cloth.<br>A physics sim for fabric. |
| `COLLISION` | Collision.<br>For colliders taking part in physics, pick which level of the modifier stack supplies the collision surface. |
| `DYNAMIC_PAINT` | Dynamic Paint.<br>Convert objects into paint canvases and brushes that produce color attributes, image sequences, or displacement. |
| `EXPLODE` | Explode.<br>Split the mesh faces apart and have them ride along with particles. |
| `FLUID` | Fluid.<br>A physics sim for fluids such as water, oil, and smoke. |
| `OCEAN` | Ocean.<br>Build an animated ocean surface. |
| `PARTICLE_INSTANCE` | Particle Instance.<br>Place a copy of the mesh at each particle. |
| `PARTICLE_SYSTEM` | Particle System.<br>Emit particles from the shape. |
| `SOFT_BODY` | Soft Body.<br>Simulate squishy, deformable objects. |
| `SURFACE` | Surface. |

[Related references](INDEX.md).
