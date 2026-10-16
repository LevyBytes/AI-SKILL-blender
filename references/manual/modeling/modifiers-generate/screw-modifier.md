# Screw Modifier

## Screw Modifier

This modifier resembles the Screw tool; it takes a profile object (mesh or curve) and creates a helix.

Angle specifies degrees per single revolution.

Screw defines the height of one helix iteration.

Iterations sets the number of revolutions.

Axis selects the helix build direction.

Axis Object names an object defining the axis direction.

Object Screw derives iteration height from the distance to the Axis Object.

Steps Viewport and Render set the subdivision count per revolution for viewport display and rendering respectively; higher render steps improve quality.

Merge unifies vertices on the rotation axis using a triangle fan to close endpoints.

Merge Distance sets the proximity threshold for axis-based merging.

Stretch UVs stretches UV coordinates from 0.0 to 1.0 across the helix when present.

Smooth Shading outputs smooth-shaded faces instead of flat.

Calculate Order reorders edges to prevent normal and shading problems (meshes only, not curves).

Flip reverses normal direction.

Profile alignment is critical: orient the profile perpendicular to the cardinal direction rather than to the screw axis itself.

[Related references](INDEX.md).
