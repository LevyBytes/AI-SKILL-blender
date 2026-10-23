# Smooth Modifier

## Smooth Modifier

The Smooth Modifier refines stroke/point data (location, strength, thickness, UV texture placement) by averaging to create flowing, continuous linework.

**Options.**

Affect: which stroke/point characteristics the smooth operation targets:
- Position: averages point spacing.
- Strength: averages point strength (opacity).
- Thickness: averages point width.
- UV: averages point UV rotation.

Factor: magnitude of smoothing applied per iteration.

Repeat: how many smoothing passes to execute, like running the Smooth tool repeatedly; excessive counts degrade playback frame rate (FPS).

Keep Shape: when active, the algorithm tries to retain the stroke's original silhouette.

Smooth Ends: averages the stroke's start and terminal points.

**Influence.**

See Influence Filters.

[Related references](INDEX.md).
