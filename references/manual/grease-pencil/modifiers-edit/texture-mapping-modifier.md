# Texture Mapping Modifier

## Texture Mapping Modifier

The Texture Mapping Modifier repositions stroke texture UV coordinates.

**Options.**

Mode — which texture data to transform (stroke/fill or stroke alone):

Stroke:
- Fit Method: chooses the texture alignment approach.
  - Constant Length: texture preserves fixed length along strokes.
  - Stroke Length: texture rescales per stroke span.
- UV Offset: shifts the texture progression along strokes.
- Rotation: reorients stroke points.
  Note: Rotation limited to -90 through 90 degrees.
- Scale: texture magnitude scaling.

Fill:
- Fill Rotation: establishes texture orientation.
- Offset: moves texture center point (X, Y).
- Scale: texture magnitude scaling.

**Influence.**

See Influence Filters.

[Related references](INDEX.md).
