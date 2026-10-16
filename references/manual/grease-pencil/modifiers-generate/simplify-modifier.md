# Simplify Modifier

## Simplify Modifier

The Simplify Modifier reduces point count in strokes while maintaining shape. Applying this modifier improves viewport performance during animation.

Mode: Fixed alternates point deletion (start/end exempt). Iterations: Repetition count. Adaptive: RDP algorithm (Ramer-Douglas-Peucker) deletes points while preserving shape. Factor: Algorithm recursion depth. Sample: Recreates with fixed point spacing. Length: Distance between points; smaller requires more, larger requires fewer. Sharp Threshold: Preserves corners sharper than threshold. Merge: Combines nearby points. Distance: Merge threshold.

Influence: See Influence Filters.

Example: Original, Iteration 1, Iteration 2, Iteration 3 shown. Also: Factor 0.1, Factor 0.5, Factor 1.0 shown.

[Related references](INDEX.md).
