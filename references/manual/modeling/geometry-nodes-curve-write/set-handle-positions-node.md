# Set Handle Positions Node

## Set Handle Positions Node

Set Handle Positions Node

Modifies Bézier handle locations to reshape the curve. Consult Bézier curves documentation for details.

Note: Auto and Vector handle types convert to Aligned and Free respectively when positions change.

Note: Left and right handles cannot be modified simultaneously due to alignment constraints.

Inputs:
Curve — Standard geometry input.
Selection — Boolean mask for modifying handles.
Position — Target handle location (global, not relative to control point).
Offset — Optional per-handle translation, evaluated alongside Position without reflecting Position changes.

Properties:
Left / Right — Which handle(s) to adjust. Left is nearer the start.

Outputs:
Curve — Standard geometry output.

Examples:
Align handles to control point position but offset downward in Z. Use Set Spline Type Node to enforce poly spline in Edit Mode for user convenience.

[Related references](INDEX.md).
