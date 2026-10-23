# Offset Modifier

## Offset Modifier

The Offset Modifier repositions, rotates, or rescales strokes measured from the object's local center.

**Options.**

**General.**

Location X, Y, Z: stroke displacement relative to origin.

Rotation X, Y, Z: stroke angular orientation.

Scale X, Y, Z: stroke magnitude scaling.

**Advanced.**

Mode:
- Random: injects random offsets to individual strokes.
- Layer: bases offsets on layer indices.
- Stroke: bases offsets on stroke enumeration.
- Material: bases offsets on material assignment.

Offset X, Y, Z: per-element positional delta.

Rotation X, Y, Z: per-element angular rotation.

Scale X, Y, Z: per-element magnitude change.

Uniform Scale (Random mode): shares one random Seed across all scale axes, producing isotropic scaling.

Seed (Random mode): initializer for the pseudo-random sequence.

Layer/Stroke/Material Step (Layer, Stroke, Material mode): how many contiguous elements to batch and offset.

Offset (Layer, Stroke, Material mode): shifts the enumeration baseline.

**Influence.**

See Influence Filters.

[Related references](INDEX.md).
