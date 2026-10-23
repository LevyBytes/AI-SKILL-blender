# Introduction: Normalized Weight Workflow

### Normalized Weight Workflow

For deformation purposes, weights typically demand normalization,
so all deforming group weights per vertex equal 1.
The Armature modifier performs this automatically, so strict painting-phase normalization remains optional.

However, despite complexity, normalized operation provides advantages,
unlocking specialized tools and simplifying influence calculations—
when normalized, the current group's impact needs no knowledge of
other group values on the same vertex.

Support tools aid normalized-weight workflows:

Normalize All
To start normalized-weight work, first normalize current data.
Normalize All handles this.
Confirm correct mode selection and deactivate Lock Active .

Auto Normalize
Once initially normalized,
enable Auto Normalize
to sustain normalization automatically during painting.
This alerts certain tools that weights remain pre-normalized.

Vertex group locking
Any group can lock against changes. Use
the lock toggle in the group interface, or employ bone selection with
the locks menu.

This guards against unintended modifications. Since Auto Normalize respects it as well, in normalized workflows
it carries greater significance: locking freezes chosen bone influences,
so repainting others redistributes across unlocked options only.

This becomes crucial in multi-bone regions, enabling careful tweaking and redistribution
using a targeted bone subset. Locking can help here,
complemented by
the Lock Relative option, which shows unlocked groups as
though re-scaled with locked groups absent, making locked bones seem invisible.

Multi-Paint
Finally, Multi-Paint lets
multiple picked bones behave as unified, shifting
their combined influence while maintaining their ratio. With locking,
this permits balancing one bone set versus others, with a third set
having unchanged influence via locks.

Technically unnecessary for normalized workflows, but given non-normalized
weights can exceed 1, visual feedback performs optimally with Auto Normalize active.

Tip

As illustration, when handling a ring, e.g. lips or aperture, selecting with
Multi-Paint exposes difference between the loop overall and adjacent bones,
whereas locking surrounding choices and using Lock Relative shows variation among
loop components. Thus the intricate cross-dimensional variation of each bone separates
into two independent one-dimensional shifts.

[Related references](INDEX.md).
