# Separate Geometry Node

## Separate Geometry Node

### Separate Geometry Node

Splits input geometry into two outputs based on a selection criterion.

**Inputs**
- Geometry: Standard input.
- Selection: Boolean field; true values route to Selection output, false to Inverted.

**Properties**
- Domain: Evaluation scope.
  - Point: Applies to base points and control points.
  - Edge: Applies to edges; others unaffected.
  - Faces: Applies to faces; others unaffected.
  - Spline: Applies to splines as units (whole or none); others unaffected.

Note: Components not affected by the chosen domain appear in both outputs.

**Outputs**
- Selection: Chosen geometry.
- Inverted: Remaining geometry.

Tip: Combine with Compare Node for refined separation logic.

[Related references](INDEX.md).
