# Interior

## Interior

### Interior 

By default, soft-body mesh edges behave like springs—stretching under tension, compressing under pressure, returning to "rest" length.

Spring behavior maintains mesh cohesion. Disabling this (and Goal) frees each vertex to move independently, stretching the mesh beyond recognition.

Springs along edges prove insufficient: quad vertices move toward diagonal opposites, collapsing quads.

Diagonal edges everywhere would solve this; instead, enable Stiffness to let Blender create interior diagonal springs automatically—no mesh changes needed.

| Description | Description |
| --- | --- |
| Base springs along edges.  | Additional springs when Stiffness is enabled.  |

Bending Stiffness adds rotational resistance, keeping edges at consistent angles.

Both appear in detail below. Configure them in Soft Body Edges panel.

### Stiffness 

Illustrate Stiffness effects by dropping two cubes onto a plane (see Collisions).
The blue cube uses quads; red uses triangles. Both have Goal disabled.

Without Stiffness, the quad cube collapses entirely; the tri cube temporarily deforms then recovers:

| Description | Description | Description |
| --- | --- | --- |
| Frame 1.  | Frame 36.  | Frame 401.  |

With Stiffness enabled, the quad cube maintains form via interior springs:

| Description | Description | Description |
| --- | --- | --- |
| Frame 1.  | Frame 36.  | Frame 401.  |

### Bending Stiffness 

Bending Stiffness prevents collapse; combine with Stiffness for bending resistance on diagonals.

Cube test using Bending Stiffness alone:

| Description | Description | Description |
| --- | --- | --- |
| Frame 1.  | Frame 36.  | Frame 401.  |

Both cubes retain shape. Try with subdivided planes—quad-based and triangulated:

| Description | Description | Description |
| --- | --- | --- |
| Two planes falling.  | No bending stiffness.  | High bending stiffness (10).  |

Without Bending Stiffness, faces rotate freely as if hinged. Stiffness (adding diagonals) doesn't prevent this; triangulation similarly doesn't.

With high Bending Stiffness, edges resist rotation; planes behave like planks rather than cloth.

[Related references](INDEX.md).
