# Compare Node

## Compare Node

### Compare Node

Determine if two inputs are similar using an operation.
Works on all generic types; vector modes offer complex comparisons for cleaner, more readable trees.

### Inputs

**A, B**
Inputs of selected type.

**C**
Threshold for Dot Product mode comparison.

**Epsilon**
Threshold for Equal and Not Equal.

### Properties

**Mode**

- **Element-Wise:** Compare each axis separately; true only all axes match.
- **Length:** Compare vector magnitudes.
- **Average:** Compare vector element average (implicit Float conversion).
- **Dot Product:** Compare dot product against C; single agreement metric.
- **Direction:** Compare angle with Angle input; vector length irrelevant.

**Operation**

- **Less Than:** First < second.
- **Less Than or Equal:** First <= second.
- **Greater Than:** First > second.
- **Greater Than or Equal:** First >= second.
- **Equal:** Difference < Epsilon.
- **Not Equal:** Difference > Epsilon.
- **Brighter:** First color brighter than second.
- **Darker:** First color darker than second.

### Output

**Result**
Boolean output.

### Examples

Direction mode compares sphere face normals to cube object location direction.
Faces less than 32.9 degrees apart are selected and deleted.

[Related references](INDEX.md).
