# Clamp Node

## Clamp Node

The Clamp node constrains a value between a minimum and a maximum. Inputs: Value (the input to clamp), Min (the minimum), and Max (the maximum). Properties: Clamp Type — Min Max (constrain between Min and Max, and when Min exceeds Max, always output Max regardless of input) or Range (constrain between Min and Max, but when Min exceeds Max, constrain between Max and Min instead). Output: Result (the clamped value). Example: the Voronoi Texture node outputs a value with a minimum of zero, and the Clamp node can raise that minimum to 0.2.

### Clamp Node

Constrain a value between min and max.

### Inputs

**Value**
Input to clamp.

**Min**
Lower bound.

**Max**
Upper bound.

### Properties

**Clamp Type**

- **Min Max:** Constrain between Min and Max. Min > Max: always outputs Max.
- **Range:** Constrain between Min and Max. Min > Max: swap and constrain.

### Outputs

**Result**
Clamped output.

### Examples

Voronoi Texture outputs minimum zero.
Clamp to minimum 0.2.

Clamp example.

### Clamp Node

The Clamp node pins a value inside a floor and a ceiling.

### Inputs

Value
The figure you want clamped.

Min
The minimum value.

Max
The maximum value.

### Properties

Clamp Type
Method to clamp.

Min Max :

Pin values inside Min and Max. Should Min run past Max, Result simply yields Max regardless of what comes in.

Range :

Pin values inside Min and Max. Should Min run past Max, pin inside Max and Min the other way round.

### Outputs

Result
The figure once it has been clamped.

### Examples

The Voronoi Texture node emits a value bottoming out at zero. Clamp can lift that floor so the minimum reads 0.2 instead.

Example of Clamp node.

[Related references](INDEX.md).
