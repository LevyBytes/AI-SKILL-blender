# Controls: Auto-Masking

## Controls

### Controls

### Auto-Masking

Reference

Mode:
Sculpt Mode

Tool:
Header ‣ Auto-Masking

Shortcut:
Alt - A

These features automatically protect areas per geometric characteristics.
Offering rapid masking without frequent manual adjustments.
Masks reset with each brush stroke or tool use and never appear as overlays.

Note that these are active across all sculpt brushes but also configurable
per brush via Advanced Brush Settings.

Access via Pie Menu at Alt - A.

All modes combine to generate targeted masks.
As an example, mask a specific face set,
exclude unattached topology and boundaries,
and target faces visible from the viewport via View Normal.

Topology
Only geometry topologically joined to the stroke/tool starting point gets affected.
Separate islands get protected.

For the Grab and
Thumb brushes specifically, anything unconnected inside the radius also gets protected.
Even joined geometry counts as isolated if the link lies outside the radius.

Face Sets
Only geometry belonging to the Face Set at stroke/tool start is affected.

Tip

If nothing appears under the cursor at initiation,
the previously protected area remains active.
Particularly handy with the "Projected" shape in the
Falloff Settings.

Mesh Boundary
Geometry at open borders is not affected.
Boundary borders to concealed faces are included.

Propagation Steps
Softens the boundary transition gradient.
Every iteration extends one edge further.
Applies to both Mesh Boundary and Face Sets Boundary.

Create Mask
Executes Mask From Mesh Boundary with active auto-masking
options. Helps render the current auto-mask or customize it manually.

Face Sets Boundary
Geometry at Face Set borders is not affected.
Boundary borders to concealed faces are included.
Propagation Steps are shared with Mesh Boundary auto-masking.

Create Mask
Executes Mask From Face Sets Boundary with active auto-masking
options. Helps render the current auto-mask or customize it manually.

[Related references](INDEX.md).
