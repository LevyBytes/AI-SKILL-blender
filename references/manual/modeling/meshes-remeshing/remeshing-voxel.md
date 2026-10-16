# Remeshing: Voxel

## Remeshing

### Remeshing

Blender includes a handful of tools that rebuild a mesh into roughly the same shape but with fewer faces, more faces, or cleaner topology.

Remeshing to clean up messy geometry.

### Remeshing

Reference

Mode :

Object Mode, Sculpt Mode

Panel :

Properties ‣ Data ‣ Remesh

Remeshing regenerates the mesh with uniform topology on its own. Crank the resolution high to densify a simple mesh for sculpting, or drop it low to thin out and tidy overly dense or messy geometry, such as a sculpt or a 3D scan.

Note

- Remeshing only acts on the original mesh data, ignoring modifiers, shape keys, and the like.

- Remeshing is not possible on objects with a Multiresolution Modifier.

The Remesh panel offers two modes:

### Voxel

The Voxel remesher drops the mesh into a virtual 3D grid, finds which grid points sit nearest the outer surface, and lays new vertices there. The upshot is uniform topology with no inner, self-intersecting geometry.

Where it helps:

- Re-resolving or generally tidying a mesh you intend to sculpt. Set the resolution up front and you can keep Dyntopo off, dodging its performance hit.

- Tidying a mesh ahead of 3D printing.

- Producing a stripped-down stand-in mesh for physics simulation.

Because that topology is just a plain grid, though, skip the Voxel remesher for:

- Building topology for a mesh that will deform (an animated character, say). That has to follow the geometry's flow, and since no flawless automatic tool exists yet, it's a manual job. See Retopology.

- Feeding a Subdivision Surface or Multiresolution Modifier. Quad mode wins there.

- Trimming the face count of a mesh whose geometry is otherwise fine. Decimate Geometry suits that better.

Voxel remesh has the following settings:

Voxel Size
How big each voxel (3D grid cell) is. Small values yield a dense, detailed result; large ones a coarse, lightweight one.

Adaptivity
Trims the face count by easing off detail where it isn't needed. Any value above zero turns Fix Poles off and may bring in triangles.

Fix Poles
Trades a little speed to thin out Poles for cleaner topological flow.

Preserve

Volume
Aims to hold the mesh's original volume. (On complex meshes this can slow the operator.)

Attributes
Carries attributes over to the rebuilt mesh, the paint mask, any face sets, color attributes, and the rest.

See also

The Remesh Modifier does the same job non-destructively and brings additional remeshing methods.

[Related references](INDEX.md).
