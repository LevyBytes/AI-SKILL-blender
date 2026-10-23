# Pose

## Pose

### Pose

Reference

Mode:
Sculpt Mode

Brush:
Sidebar ‣ Tool ‣ Brush Settings ‣ Advanced ‣ Brush Type

Skeletal-like deformation for posing without rigs.

The brush computes a starting point,
indicated by a white line on the cursor.

Altering Deformation Target
allows cloth-sculpting use.

### Brush Settings

### General

Only Size and Auto-Masking influence function on this brush.

Note

More info at General brush settings
and on Advanced brush settings.

### Unique

Deformation
Operation type employed.

Rotate/Twist:
Spins mesh around the pose anchor.
Holding Ctrl generates twisting instead
(disabling any inverse-kinematic segments).

Scale/Translate:
Enlarges relative to the anchor.
While holding Ctrl, the brush displaces the mesh.

Squash/Stretch:
Like Scale/Translate yet uses unequal
scale ratios along different axes for stretching.

Rotation Origins
Method for establishing rotation anchor for the pose or specific IK segments.

Topology:
Automatically selects based on mesh structure and shape.

Face Sets:
Constructs a pose segment per Face Set, beginning with the active Face Set.
Typically generates most accurate results.

Face Sets FK:
Applies Forward Kinematics deformation with the Face Set
beneath the cursor as the control.

Pose Origin Offset
Distance of the pose anchor relative to the active radius.
Beneficial for intricate regions like appendages.

Smooth Iterations
Adjusts deformation gradient smoothness.

Pose IK Segments
Sets inverse-kinematic segment quantity
rendered as a segmented white line on the cursor.
Produces curved deformations: like hair clumps and limbs.

Lock Rotation when Scaling
Under Scale/Translate Deformation, prevents rotation; only scaling occurs.

Keep Anchor Point
Secures the terminal IK segment position.
If disabled, the mesh shifts more unrestricted,
mimicking serpentine motion.

Connected Only
Restricts to topologically joined components.
Disabling lets multiple separate meshes deform simultaneously,
like dressed figures.

Performance suffers with disconnection; reducing Max Element Distance helps.

Max Element Distance
Search extent for separate mesh portions.

[Related references](INDEX.md).
