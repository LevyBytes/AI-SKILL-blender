# Mesh Filter: Tool Settings

### Tool Settings

Filter Type
Encompasses all accessible deformation operations.

Smooth :

Softens vertex positions to polish surfaces or minimize volume from larger features. Particularly valuable for fixing voxel remesher imperfections. Functions comparably to the Smooth brush.

Scale :

Enlarges the mesh overall. Functions comparably to the Scale Transform.

Inflate :

Shifts vertices uniformly outward along their normals. Functions comparably to the Inflate brush.

Sphere :

Morphs the mesh incrementally into a spherical form. Functions comparably to the To Sphere Transform.

Random :

Displaces vertices at random along their normals. Functions comparably to the Randomize Transform.

Relax :

Creates an equitable quad distribution without altering mesh volume. Works identically to pressing Shift with the Slide Relax brush.

Relax Face Sets :

Eliminates visible roughness from face set boundaries. Works identically to pressing Shift with the Draw Face Set brush.

Surface Smooth :

Corrects mesh imperfections by equalizing vertex positions while retaining volume. Functions comparably to the Surface deformation mode of the Smooth brush.

Shape Preservation
Retains what portion of the original geometry remains unaltered when smoothing occurs.

Per-Vertex Displacement
Controls how much individual vertex movement factors into the final outcome.

Sharpen :

Emphasizes and softens geometry according to its curvature, pinching sharp features and refining flat zones. Particularly effective for hard-surface sculpting and stylized geometries featuring creases.

Smooth Ratio
Determines polish intensity applied to flat regions.

Intensify Details
Amplifies fine surface features by strengthening the distinction between grooves and peaks.

Curvature Smooth Iterations
How many times the smoothing calculation repeats per brush step. Regulates the resulting smoothness level and minimizes high-frequency noise.

Enhance Details :

Emphasizes fine surface features by strengthening the distinction between grooves and peaks. Works comparably to reversing the Smooth brush direction.

Erase Displacement :

Removes displacement data from the Multires Modifier, resetting the mesh to a standard subdivision result. Helpful for clearing sculpt areas or correcting reprojection anomalies after Shrinkwrap operations.

Negative strokes will strengthen displacement nuance, functioning like Enhance Details but sometimes producing improved results.

Strength
Dictates the force of the filter upon the mesh. Adjusting this at particular object scales can be beneficial.

Deformation Axis
Limit transformations to the designated axis.

Orientation
Establishes the axis alignment for displacement restriction.

Local :

Apply displacement using local axes.

World :

Apply displacement using global axes.

View :

Apply displacement using viewport-relative axes.

[Related references](INDEX.md).
