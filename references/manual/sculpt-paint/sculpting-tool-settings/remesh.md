# Remesh

## Remesh

### Remesh

Reference

Mode :

Sculpt Mode

Header :

Tool Settings ‣ Remesh

Panel :

Sidebar ‣ Tool ‣ Remesh

Shortcut :

Ctrl - R

For background on remeshing fundamentals, visit the Introduction.

Voxel Size R
Determines the resolution or refinement level of the remeshed result. The value specifies the size (in object space) of individual Voxels. These voxels are assembled around the geometry and determine the new topology. For example, 0.5m creates topological patches of roughly 0.5m size (assuming Preserve Volume is active). Lower values retain finer details but generate denser topology.

Adjust voxel size from the 3D viewport using R. The shortcut shows an interactive grid showing the resulting voxel scale. Move the cursor toward the grid center to reduce voxel size, or away to increase it. Holding Shift refines adjustment precision.

Sample Voxel Size
Adjust Voxel Size by selecting a mesh area that represents your desired polygon density after remeshing.

Adaptivity
Reduces the face count by simplifying geometry where detail is unnecessary. This introduces triangulation to faces that don't require as much precision. Note: Adaptivity values above zero disable Fix Poles.

Fix Poles
Produces fewer poles at the cost of additional computation to achieve better topological layout.

Preserve

Volume
Instructs the algorithm to maintain the original mesh volume. Activation may increase processing time depending on mesh intricacy.

Paint Mask
Transfers the paint mask to the remeshed geometry.

Face Sets
Transfers Face Sets to the remeshed geometry.

Color Attributes
Transfers Color Attributes to the remeshed geometry.

Voxel Remesh
Executes the remeshing operation, creating a new manifold mesh from the current mesh's volume. This action discards all mesh data layers linked to the original geometry.

See also

Remesh modifier

### Known Limitations

- Remeshing operates only on base mesh data and ignores topology from modifiers, shape keys, rigging, and other deformations.

- Remeshing is incompatible with the Multiresolution Modifier.

[Related references](INDEX.md).
