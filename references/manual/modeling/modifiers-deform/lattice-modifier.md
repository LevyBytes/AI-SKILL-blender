# Lattice Modifier

## Lattice Modifier

The Lattice modifier reshapes the base object to match a Lattice object's topology.

Tip: quickly graft a Lattice Modifier onto selected targets by picking them, then picking the lattice last and hitting Ctrl+P, selecting Lattice Deform. This installs modifiers and links the targets as offspring to the lattice.

This documentation covers the Lattice Modifier specific to Grease Pencil. For other object types, check the general Lattice Modifier.

**Options.**

Object — the Lattice object governing the deformation.

Strength — mixes between undeformed and deformed point placements.

**Influence.**

See Influence Filters.

The Lattice modifier deforms meshes, curves, surfaces, text, lattices, and particles according to a Lattice object's shape.

Parenting objects to a lattice quickly adds this modifier.

Object specifies the Lattice object controlling deformation.

Vertex Group limits the effect to a specific mesh region.

Invert reverses the group influence.

Strength blends between original and deformed positions.

Lattice deformation suits several workflows:

For models with high vertex counts, direct Edit Mode manipulation is tedious. A lattice provides efficient large-scale deformation.

Smooth lattice-based deformation is difficult to achieve by hand.

A single lattice can deform multiple objects simultaneously.

Like all modifiers, it is non-destructive—changes layer on top of the original, allowing recovery and re-editing.

Lattices do not alter texture coordinates.

When lattices deform particles, the modifier stack order matters. Place Lattice after Particle System.

[Related references](INDEX.md).
