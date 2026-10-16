# Field Variance Node

## Field Variance Node

### Field Variance Node

Compute variance and standard deviation across a domain.
Measure how much a value spreads within geometry or groups.

Analyze spread of weights, positions, or custom attributes per Group ID.

### Inputs

**Value**
Field to analyze (float or vector per Data Type).
Vector fields compute variance per component (X, Y, Z).

**Group ID**
Index grouping values for separate analyses.
Think of bins for each value.
No effect as single value.

### Properties

**Data Type**

- **Float:** Analyze float field.
- **Vector:** Analyze vector field.

**Domain**
Attribute domain for Value evaluation.

### Output

**Standard Deviation**
Square root of variance; measure of spread.

**Variance**
Average squared deviation from mean.
Higher values: more variation.

[Related references](INDEX.md).
