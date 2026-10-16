# Strokes: Sorting, Selection, Dashed Line

### Sorting

Lines can be sorted to control stacking order.

Sort Key
Determines the stacking sequence:

Distance from Camera :
Nearer lines render above distant ones.

2D Length :
Longer lines layer atop shorter ones.

Projected X/Y :
Sorts by X or Y position in image space.

Integration Type
Combines with Sort Key to determine the calculation range. Since line distance varies along vertices, this computes a single line value from per-vertex values:

Mean :
The average of vertex values.

Min :
The lowest vertex value.

Max :
The highest vertex value.

First :
The value from the first vertex.

Last :
The value from the last vertex.

Sort Order
Optionally reverse the calculated sort sequence.

### Selection

Restrict rendering to chosen chains.

Min/Max 2D Length
Filters by chain length.

Chain Count
Limits rendering to the first N chains.

### Dashed Line

Enable to specify three dash/gap pairs. Dashes define stroke lengths; gaps specify intervals. A zero gap causes its dash to be ignored regardless of its value.

Dashes are treated as separate strokes, allowing line caps and color, alpha, and thickness modifiers to apply.

Dash 1, 2, 3
Individual dash segment lengths.

Gap 1, 2, 3
Spacing between dashes.

[Related references](INDEX.md).
