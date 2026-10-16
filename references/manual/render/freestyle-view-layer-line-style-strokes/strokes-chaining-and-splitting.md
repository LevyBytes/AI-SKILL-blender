# Strokes: Chaining, Splitting, Split Pattern

## Strokes

Strokes

Strokes represent the final rendered lines. You can adjust them—removing lines shorter or longer than thresholds, merging lines into single strokes, or splitting based on angles, patterns, and other criteria.

Line Style: Strokes.

Caps
Three line ending styles are available:

Butt :
A flat termination at the exact endpoint.

Round :
A semicircle centered on the endpoint.

Square :
A square centered on the endpoint (extends the line slightly beyond its computed edge, similar to Round).

Line caps example.

### Chaining

By default, all lines from a line set connect together. Two chaining approaches exist:

Method

Plain :
Standard chaining; creates simple connected chains.

Sketchy :
Generates chains using multiple overlapping strokes instead of single lines, enabling sketchy effects. Most effective with random-driven modifiers.

Rounds
The number of overlapping strokes in sketchy mode.

Same Object
When enabled, chains only join feature edges from the same object.

Chaining can be disabled to render each line independently, useful when line-style behavior depends on precise line-set representation.

### Splitting

Enable any of the following to subdivide chains:

Min/Max 2D Angle
Separates chains when 2D angles exceed (or fall below) threshold values.

2D Length
Subdivides chains exceeding a specified length.

Material Boundary
Breaks chains crossing material transitions.

### Split Pattern

Uses a dashed pattern for subdivision (see also Dashed Line).

Dash 1, 2, 3
Individual dash segment lengths.

Gap 1, 2, 3
Spacing between dashes.

[Related references](INDEX.md).
