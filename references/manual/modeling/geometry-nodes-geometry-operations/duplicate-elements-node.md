# Duplicate Elements Node

## Duplicate Elements Node

### Duplicate Elements Node

Replicates selected geometry elements multiple times. Duplicates occupy identical positions; differentiation requires subsequent positioning operations.

**Inputs**
- Geometry: Standard input.
- Selection: Boolean field for duplication targets.
- Amount: Per-element count; zero means omit the element.

**Properties**
- Domain: Element type to duplicate.
  - Point: Replicate points; other types excluded.
  - Edge: Replicate edges; faces omitted.
  - Faces: Replicate faces independently (no shared edges).
  - Spline: Replicate entire splines.
  - Instances: Replicate top-level instances.

**Outputs**
- Geometry: Standard output.
- Duplicate Index: Attribute field (0 to Amount - 1) marking which iteration each output element represents. Useful with Geometry to Instance for efficient array-like behavior.

[Related references](INDEX.md).
