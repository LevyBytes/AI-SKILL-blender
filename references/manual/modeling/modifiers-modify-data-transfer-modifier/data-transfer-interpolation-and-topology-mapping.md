# Data Transfer Modifier: Interpolated Mappings, Topology Mapping

### Interpolated Mappings

Mappings of this kind can take in several source elements and interpolate across their values.

Vertex Data

Nearest Edge Interpolated
Locate the closest point on the nearest source edge, then let that point drive interpolation between
the edge's two vertex values.

Nearest Face Interpolated
Locate the closest point on the nearest source face, then let that point drive interpolation between
the face's vertex values.

Projected Face Interpolated
Cast the destination vertex along its normal onto a source face,
then use where it lands to interpolate among the face's vertex values.

Edge Data

Projected Edge Interpolated
Track down source edges by projecting from several points spread along the destination edge
(each one cast along the interpolated normals of that destination edge's vertices).
Then interpolate across the values of the source edges turned up this way.

Face Corner Data

Nearest Face Interpolated
Locate the closest point on the nearest source face, then let that point drive interpolation between
the face's corner values.

Projected Face Interpolated
Cast the destination corner along its normal onto a source face,
then use where it lands to interpolate among the face's corner values.

Face Data

Projected Face Interpolated
Find source faces by shooting rays from several points across the destination face along that destination
face's normal. Then interpolate across the values of these source faces.

### Topology Mapping

Note

The panel's name notwithstanding, none of these settings touch the Topology mapping type.

Max Distance
With the checkbox on, any source and destination elements separated by more
than the stated distance are ruled out as matches.

Ray Radius
The radius the ray casting begins from.

With some mapping types the operator fires off a run of ray casts from each destination
element to track down matching source elements. Those casts open at the given radius and
swell steadily until either a match turns up or a ceiling is hit.

Start small and the results get sharper, though performance suffers if it's so
tiny it has to keep growing. Start large and performance is better,
but the matches may come out less than ideal.

As a rule, keep the radius low for dense source meshes and high for simple ones.

[Related references](INDEX.md).
