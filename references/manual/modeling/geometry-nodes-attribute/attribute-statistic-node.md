# Attribute Statistic Node

## Attribute Statistic Node

The Attribute Statistic node evaluates a field across a geometry and outputs aggregate metrics.

Geometry: Standard input.
Selection: Boolean field indicating which elements to include. False values exclude the corresponding attribute from calculations.
Attribute: The field to analyze.

Data Type:

Float: Single floating-point result.
Vector: Three floating-point values, computed per-component.

Domain: The attribute category on which statistics are calculated.

Mean: The arithmetic average.
Median: The midpoint value.
Sum: The total.
Min: The smallest value.
Max: The largest value.
Range: The difference between max and min.
Standard Deviation: Spread from the mean. Low values cluster tightly; high values scatter widely.
Variance: The square of standard deviation.

[Related references](INDEX.md).
