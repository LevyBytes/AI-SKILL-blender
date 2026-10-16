# Adaptive Resolution: Multiresolution

### Multiresolution

Multiresolution Modifier enables subdivision-level sculpting.
Operates like
Subdivision Surface Modifier,
allowing sculpting at each subdivision depth.

Note

Clean base geometry is essential.
Rely on quad-only topology
and avoid non-manifold situations, plus vertices with just two connections.
See Quad Remeshing for automated conversion.

Sculpting at multiple subdivision tiers permits fine control.
Work at any depth: general shapes on early subdivisions,
fine detail at later ones.
Viewport performance stays high while retaining maximum detail.
Return to lower subdivisions anytime for major restructuring.

Example: shape at level 1,
detail at level 4, revert to level 1 to adjust forms further.

Pitfalls include topology distortion
since geometry remains fixed unlike voxel and dyntopo modes.
Base connectivity can't change post-subdivision,
as modifications break subdivision details.

Tip

Consider the topology that you customize and how much it stretches.
If extra density proves necessary you can subdivide again,
yet efficiency and switching pace diminish beyond 5 times.
Additionally try the Slide Relax
brush to move topology to places needing it.

Extra approaches like the Multires Eraser and
Multires Smear aid in rework.

These standard shortcuts cover the capability.

- Step up one multires density Alt - 2

- Step down one multires density Alt - 1

- Set multires density / Build multires option Ctrl - 0 to Ctrl - 5

See also

Further info at Multiresolution Modifier.

[Related references](INDEX.md).
