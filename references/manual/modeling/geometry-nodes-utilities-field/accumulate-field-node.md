# Accumulate Field Node

## Accumulate Field Node

### Accumulate Field Node

Sum input values sequentially, ordered by geometry indices.
Output the running total at every element, not just the final sum.

### Inputs

**Value**
Values to accumulate.

**Warning:** Integer accumulation risks overflow (~2 billion max). Large values may wrap and become negative. See Wikipedia.

**Group Index**
Index for grouping values into separate sums.
Think of it as a bin for each value.
No effect as a single value.

### Properties

**Data Type**

- **Float:** Accumulate float field.
- **Integer:** Accumulate integer field.
- **Vector:** Accumulate vector field.
- **Transform:** Accumulate matrix field.

**Domain**
Attribute domain for accumulation and Value input evaluation.

### Output

**Leading**
Running total in the group, starting at the first value.

**Trailing**
Running total in the group, starting at zero.

**Total**
Group sum.

### Examples

### Table

| Value | Group Index | Leading | Trailing | Total |
| --- | --- | --- | --- | --- |
| 1 | 7 | 1 | 0 | 6 |
| 3 | 7 | 4 | 1 | 6 |
| 2 | 7 | 6 | 4 | 6 |
| 1 | 3 | 1 | 0 | 3 |
| 0 | 3 | 1 | 1 | 3 |
| 2 | 3 | 3 | 1 | 3 |

Group index values do not matter; shared values group together.

### Stacking Boxes

Paired with Random Value Node for stacked, randomly scaled boxes.
Group Index unused: all boxes in one stack.

Three separate stacks using Group Index.

[Related references](INDEX.md).
