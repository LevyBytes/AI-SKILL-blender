# Volume to Mesh Modifier

## Volume to Mesh Modifier

### Volume to Mesh Modifier

Working in the opposite direction to the Mesh to Volume modifier, this one takes a volume object that already exists and turns one of the grids it holds into a mesh. Only scalar grids, the density grid being a typical case, are eligible for conversion.

Tip

Reach for a collection instance when you want to duplicate and reposition the generated mesh
on its own, apart from the volume object.

### Options

The Volume to Mesh modifier.

Object
The volume object that serves as the source.

Grid Name
Which grid gets converted, named here. It must be a scalar grid.

Resolution Mode
Sets the means by which the output mesh's resolution is governed.

Grid
Ties the output resolution to whatever resolution the converted grid already carries.
A denser grid therefore yields a denser mesh.
For most situations this is the most efficient choice.

Voxel Amount
Sets roughly how fine the generated mesh comes out.
The voxel size scales itself to the overall size of the volume.

Voxel Size
Locks in a fixed resolution that holds steady even as the volume changes.

Threshold
Any voxel whose value exceeds this is treated as interior to the mesh, and the rest as exterior.
Geometry is then built along the dividing line between interior and exterior voxels.
The term "iso value" is sometimes used for it.

Adaptivity
Comparable to decimating the result, trimming resolution in areas that do not require it.

Smooth Shading
Turns smooth shading on for the mesh that gets produced.

### Example

Converting a cloud-shaped volume to a mesh.

[Related references](INDEX.md).
