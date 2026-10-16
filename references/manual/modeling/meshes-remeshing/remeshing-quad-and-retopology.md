# Remeshing: Quad, Retopology

### Quad

The Quad remesher runs the Quadriflow algorithm, which can yield nicer output but takes longer. It won't replace the Voxel remesher, since it leaves intersecting geometry uncleaned.

Where it helps:

- Feeding a Subdivision Surface or Multiresolution Modifier.

Where it's a poor fit:

- Prepping a mesh for sculpting or 3D printing; the Voxel remesher fits that better.

- Building final topology for a mesh that will deform (an animated character, say). That has to follow the geometry's flow, and since no flawless automatic tool exists yet, it's a manual job. See Retopology.

- Trimming the face count of a mesh whose geometry is otherwise fine. Decimate Geometry suits that better.

Quadriflow Remesh
Brings up a pop-up for the remesh parameters.

Use Mesh Symmetry
Builds a symmetrical result from the Mesh Symmetry options.

Preserve Sharp
Aims to keep the mesh's sharp features. (On complex meshes this can slow the operator.)

Preserve Mesh Boundary
Aims to hold the mesh's original volume. (On complex meshes this can slow the operator.)

Preserve Attributes
Carries attributes over to the rebuilt mesh, the paint mask, any face sets, color attributes, and the rest.

Smooth Normals
Applies Shade Smooth to the result.

Mode
How the detail level for the new mesh gets set.

Ratio :

Target a face count as a fraction of the current mesh.

Edge Length :

Target an edge length for the new mesh.

Faces :

Target an absolute face count for the new mesh.

Seed
Random Seed for the solver; change it and the remesher lays out the quads differently.

### Retopology

The automatic remeshers rarely give topology that deforms well, so once you've sculpted a character and want it simplified for animation, you'll usually redo the topology by hand, a process called retopologizing.

The usual approach is to lay a new mesh over the original, then reshape it until it wraps the original fully and matches its form.

- The 3D Viewport's Retopology overlay helps, letting the original show through the new mesh and vice versa, without the far-side geometry distracting you the way X-Ray would.

- The Poly Build tool lets you add, edit, and delete faces quickly.

- Lean on Snapping to seat new vertices on the original mesh.

[Related references](INDEX.md).
