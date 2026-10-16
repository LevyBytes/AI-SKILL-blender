# Mesh to Volume Modifier

## Mesh to Volume Modifier

This modifier (volume objects only) converts mesh geometry into a new volume density grid. Previous volume grids are discarded; the modifier typically targets an empty volume object.

Object references the mesh that determines volume generation.

Density controls visual density during rendering.

Interior Band Width sets the maximum distance of voxels from the mesh surface included on the inside.

Resolution Mode: Voxel Amount approximates the total voxel count along the mesh's diagonal (changes with mesh size), Voxel Size specifies exact voxel dimensions (better for animation rendering to avoid inter-frame artifacts).

[Related references](INDEX.md).
