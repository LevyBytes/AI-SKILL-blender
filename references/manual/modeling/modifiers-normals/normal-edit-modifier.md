# Normal Edit Modifier

## Normal Edit Modifier

### Normal Edit Modifier

Custom normals are what the Normal Edit modifier works on, whether editing existing ones or producing new ones. A small set of straightforward parametric methods does the computing, which makes it rather useful for game development and architectural work, and the normals it generates then get blended back together with whatever was already there.

### Options

Normal Edit Modifier.

Radial
Points the normals along the (origin, vertex_coordinates) vector, so they all appear to fan out
from the chosen center point, as though shed from the surface of an ellipsoid.

Directional
Aims every normal so it converges on a chosen target object.

Target
Uses this object's origin as the point of reference while the normals are generated.

Optional in Radial mode, mandatory in Directional one.

Parallel Normals
Runs all the normals parallel to the line joining the two objects' origins,
instead of letting them converge on the target's origin.

Only relevant in Directional mode.

### Mix

Mix Mode
Sets how the freshly generated normals act on the existing ones.

Keep in mind that Multiply here isn't a cross product but a quicker per-component multiplication.

Mix Factor
How much of the generated normals gets folded into the existing ones.

Vertex Group
Gives per-item fine control over the mix factor. The arrow button to the right flips the vertex group's influence.

Max Angle
Bars any newly generated normal from sitting at an angle to its original beyond this threshold.
Useful for heading off drastic shifts, which could even flip the front and back of a face,
and with that bring on shading artifacts.

/ Lock Polygon Normals
Stops polygons from flipping (front and back swapping) where their normal no longer agrees with
the side their corners' custom normals point toward. Can likewise help head off shading trouble.

### Offset

Nudges the modified object's origin by an offset before it's used to generate normals.

This matters only in Radial mode where no Target Object is given,
and in Directional mode where Parallel Normals is turned on.

### Usage

You might reach for this modifier to rapidly produce radial normals on low-poly tree foliage, or to
"fix" the shading of toon-style rendering by bending the default normals part-way…

Tip

For richer normal work, you can transfer normals from one mesh onto another;
see the Data Transfer Modifier.
The Weighted Normals modifier is another tool
some shading effects can draw on.

### Example

Editing custom normals to point towards a given direction
(blend-file).

On the left the tree mesh keeps its normals untouched, while on the right a Normal Edit modifier bends them
toward the camera. Games lean on this shading trick a lot to fake scattering through trees and other foliage.

[Related references](INDEX.md).
