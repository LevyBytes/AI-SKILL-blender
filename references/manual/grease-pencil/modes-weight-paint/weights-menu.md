# Weights Menu

## Weights Menu

**Normalize All.**

Menu ‣ Weights ‣ Normalize All. For each point, guarantees all vertex group weights sum to unity, normalizing all except those locked, which remain static.

Lock Active — keeps the active group's values unaltered while rescaling others.

**Normalize.**

Menu ‣ Weights ‣ Normalize. Acts exclusively on the active vertex group; all points preserve relative weight ratios, yet the overall magnitude scales so peak weight equals 1.0.

**Invert.**

Menu ‣ Weights ‣ Invert. Multiplies each weight in the selected vertex group by × -1.0.

Examples:
- Original 1.0 becomes 0.0
- Original 0.5 stays 0.5
- Original 0.0 becomes 1.0

**Smooth.**

Menu ‣ Weights ‣ Smooth. Diffuses the weights across the active vertex group.

**Sample Weight.**

Menu ‣ Weights ‣ Sample Weight; shortcut Shift+X. Syncs the Draw tool's Weight parameter to the vertex weight under the cursor.

[Related references](INDEX.md).
