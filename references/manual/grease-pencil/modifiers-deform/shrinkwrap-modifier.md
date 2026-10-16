# Shrinkwrap Modifier

## Shrinkwrap Modifier

The Shrinkwrap modifier compresses a Grease Pencil object onto another object's surface by repositioning each point toward the nearest surface location.

See also: Shrinkwrap Constraint and general Shrinkwrap Modifier documentation.

**Options.**

Wrap Method — establishes how the nearest surface point is located for each modified point; some approaches unlock extra settings.

Snap Mode — most approaches permit governance over point motion toward the target. Behavioral variants if Offset ≠ zero:
- On Surface: points always shift; offset travels the projection axis backward.
- Inside: stationary if inside target; offset constricts the allowed region inboard.
- Outside: stationary if outside target; offset pushes the exclusion boundary outward.
- Outside Surface: like On Surface, but offset points outward exclusively.
- Above Surface: like On Surface, but offset follows the target's interpolated normals.

Note: Inside and Outside mimic crude collision via target normal geometry, unreliable near 90° and sharper curvature.

Target — surface destination; the mesh to tighten around.

Offset — gap preserved from the computed target position.

Smooth Factor — intensity of post-wrap smoothing.

Repeat — how often to re-smooth.

**Influence.**

See Influence Filters.

**Wrap Methods.**

Nearest Surface Point — latches onto the nearest spot on the target surface.

Project — shoots points along a user-picked axis until collision; unconnected points sit static.

Limit — threshold for distance between source point and surface; exceeding this prevents projection.

Subdivision Levels — temporarily applies Catmull-Clark subdivision to the object's data prior to wrapping.

Axis — local direction along which projection fires; options layer to form a "composite direction." If blank, face normals guide projection.

Negative/Positive — specifies allowed shrink trajectories along the axis; both enabled tests either way and takes the closer result.

Face Cull — barricades projection across target face "obverse" or "reverse" (determined by face normal).

Invert Cull — when Face Cull is on and Negative is allowed, swaps the Front/Back cull for Negative direction, handy for bilateral projection.

Auxiliary Target — secondary geometry to project against.

Nearest Vertex — jumps to the nearest vertex on the target; contributes no added controls and bypasses Snap Mode.

Target Normal Project — matches Nearest Surface Point's behavior but yields superior blending in exchange for slower performance. Rather than hunting the closest point, seeks the nearest point whose blended normal vector targets/targets-away from the source. Boundary edges in non-closed topology become infinitely-thin cylinder emitters; flat shading does not apply.

[Related references](INDEX.md).
