# Hook Modifier

## Hook Modifier

The Hook Modifier warps stroke points by coupling them to another object (typically an empty or bone, yet any object suffices).

As the hook travels, it yanks points along—comparable to animated Proportional Editing in motion.

This documentation targets the Hook Modifier as implemented for Grease Pencil. For other object types, check the general Hook Modifier.

**Options.**

Object: the object to which points link.

Strength: tweaks hook potency on stroke points, ranging from 0.0 (inert) to 1.0 (point trails the hook).

**Falloff.**

Type: picks the Strength decay curve; author a custom profile for fine-grain governance.

Radius: the extent of hook influence.

Uniform Falloff: worthwhile when hooking scaled objects, especially if non-uniform scaling would distort the deformation.

**Influence.**

See Influence Filters.

Note: The Hook Modifier caches point indices from original strokes to define affected geometry; modifiers synthesizing new geometry (e.g., Subdivision Surface) must apply downstream of the Hook Modifier, otherwise their output sits outside the hook's reach.

The Hook modifier deforms meshes, curves, or lattices by tethering selected vertices to another object (typically an empty or bone). As the hook object moves, it pulls bound vertices along, similar to animated Proportional Editing.

Unlike shape keys, hooks lack fine per-vertex control but allow direct selection of vertices to manipulate.

In Edit Mode, use the Assign button on the modifier panel or the Add Hook menu to bind selected vertices.

Object specifies the hook object.

Vertex Group enables per-vertex influence weighting, useful for non-spherical falloff patterns.

Invert reverses the group effect.

Strength scales the hook's pull (0.0 to 1.0). Multiple hooks can affect the same vertices; this weight balances their relative influence.

Edit-Mode-only settings:

Reset recalculates and clears the hook's offset transformation.

Recenter moves the hook to the 3D Cursor position.

Select highlights all vertices affected by this hook.

Assign binds currently selected vertices to this hook.

Warning: the Hook modifier stores indices from the original mesh. Geometry-generating modifiers (Subdivision Surface) must appear after Hook in the stack, or newly created geometry will be excluded from the hook's influence.

Falloff Type adjusts how the hook's strength changes from its center to its Radius—see Proportional Editing for descriptions. A custom curve offers fine control.

Radius sets the influence distance.

Uniform Falloff is useful on scaled objects, especially with non-uniform scaling. Lattices benefit particularly, as non-uniform scaling is common for them.

[Related references](INDEX.md).
