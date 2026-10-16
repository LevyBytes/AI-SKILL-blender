# Length Modifier

## Length Modifier

The Length Modifier shrinks or extends strokes.

Mode: Absolute measures length in geometry space. Relative uses stroke-length ratio.

Start: Length added at the stroke start; negative shrinks. End: Length added at the stroke end; negative shrinks. Used Length: Stroke portion used for extension direction.

Curvature: When enabled, extensions follow the stroke curve. Point Density: Multiplied by Start/End for total point count. Segment Influence: Controls how much individual segment length shapes overall curvature; higher factors reduce influence of short segments. Filter Angle: Ignores points deviating beyond this angle from neighbors during extrapolation. Invert: Reverses extension curvature.

Random Offsets: Random Offset Start/End adds variable length to stroke extremities. Random Noise Offset: Smoothly drifts each stroke's random value. Seed: Noise generation value.

Randomize: Re-calculates values by frame interval. Step: Frame count before recalculating.

Influence Filters: See Influence Filters.

[Related references](INDEX.md).
