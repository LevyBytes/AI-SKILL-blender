# Evaluate on Domain Node

## Evaluate on Domain Node

### Evaluate on Domain Node

Evaluate a field on a different attribute domain than the field context.
Example: use face index instead of face corner index for UV Map values.

**Note:** Not required for cross-domain retrieval (automatic).
Utility: control when interpolation occurs.
Normally, inputs interpolate to the current domain on output creation.

**Tip:** Prefer over Capture Attribute—uses a specific domain without geometry socket, enabling reusable groups.

**See also:** Method similar to Evaluate at Index.

### Inputs

**Value**
Field to evaluate.

### Properties

**Domain**
Evaluation domain.

### Output

**Value**
Input evaluated on the chosen domain, then interpolated back to the field context domain.

[Related references](INDEX.md).
