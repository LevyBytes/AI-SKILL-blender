# Adaptive Resolution: Voxel Remesher, Dyntopo

## Adaptive Resolution

### Adaptive Resolution

For sculpting to yield consistent and repeatable geometry, ample surfaces are necessary.
Rather than beginning with a densely divided mesh, increase geometry in real-time
using either of these adaptive sculpting approaches.

### Voxel Remesher

Voxel-based rebuilding constructs geometry with uniform topology distribution.
Voxel dimensions control resulting resolution.

Ideal for establishing foundational shapes.
Removes overlaps and guarantees watertight models.

Masks, Face Sets, and attribute colors reproject onto remeshed output.
High vertex counts stay feasible based on hardware.

Note

This method needs sealed forms.
Empty all gaps prior to remeshing.
Or avoid holes bigger than the chosen voxel proportion.

Tip

When unclear, use the Alt
to fill all gaps or by using the
Mask Slice and Fill Holes
choice to complete all gaps. If unprotected, only fills all gaps.

Use R to configure the size,
and Ctrl - R to do the remeshing.

See also

Further info at Remesh.

### Dyntopo

Dyntopo (Dynamic topology) mechanically inserts and removes faces under the brush during sculpting.

Unlike Voxel Remesher, this permits elaborate shape work
without density awareness.
Resolution varies per area as needed.
Advanced base topology sculpting shines with this.

Speed and feature availability suffer; performance lags.
Custom characteristics including Color data, UV assignments and Face Sets degrade or vanish.

This capability uses matching shortcuts with voxel method when on.
Use R to configure the density and Ctrl - R to distribute the density (if Constant Detail applies).

Note

Because Dyntopo and the Voxel Remesher exclude and prevent combined use,
both employ the same option for remesh settings.

Approaches like Density,
Snake Hook
and Clay Strips show best with this capability.

See also

Further info at Dyntopo.

[Related references](INDEX.md).
