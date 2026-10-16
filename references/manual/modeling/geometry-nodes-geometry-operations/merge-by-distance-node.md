# Merge by Distance Node

## Merge by Distance Node

### Merge by Distance Node

Combines nearby mesh vertices or point cloud points within a specified threshold, also consolidating adjacent geometry. Similar to the Merge operator or Weld Modifier.

**Inputs**
- Geometry: Standard input.
- Selection: Boolean; unselected points are skipped and unaffected.
- Mode: Selection strategy.
  - All: Merge all geometry including isolated parts.
  - Connected: Merge only attached geometry; isolated parts remain separate.
- Distance: Threshold for considering points neighbors.

**Output**
- Geometry: Standard output.

Tip: Selection input improves performance by excluding unneeded points from the expensive neighborhood search.

[Related references](INDEX.md).
