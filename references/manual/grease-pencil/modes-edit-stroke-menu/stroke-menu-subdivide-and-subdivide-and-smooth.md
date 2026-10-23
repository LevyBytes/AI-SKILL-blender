# Stroke Menu: **Subdivide.**, **Subdivide and Smooth.**

## Stroke Menu

**Subdivide.**

Menu ‣ Stroke ‣ Subdivide. Inserts new control points into selected curve segments via progressive subdivision, enabling smoother transitions, greater detail control, or animation setup.

Number of Cuts: number of divisions for each segment; each cut adds one new control point.

Selected Points: when enabled, limits the effect to selected points within the stroke.

**Subdivide and Smooth.**

Menu ‣ Stroke ‣ Subdivide and Smooth. Subdivides and smooths strokes by inserting points between selected ones.

Number of Cuts: number of subdivisions.

Selected Points: when enabled, limits to selected points within the stroke.

Iterations: procedure repeats.

Factor: smoothness amount on subdivided points.

Smooth Endpoints: smooths stroke endpoints.

Keep Shape: preserves stroke shape.

Position: affects point location.

Radius: affects point thickness.

Opacity: affects point strength (alpha).

**Simplify.**

Menu ‣ Stroke ‣ Simplify. Reduces stroke complexity by strategically removing points; useful for cleaning up strokes, optimizing performance, and preparing for further editing or animation.

Fixed: Menu ‣ Stroke ‣ Simplify – Fixed. Deletes alternated points except start and end.

Steps: procedure repeats.

Adaptive: Menu ‣ Stroke ‣ Simplify – Adaptive. Uses the Ramer-Douglas-Peucker algorithm to remove points while maintaining similar line shape.

Factor: controls recursion depth for simplification.

Sample: Menu ‣ Stroke ‣ Simplify – Sample. Recreates stroke geometry with a predefined distance between points.

Length: distance between points on the recreated stroke; smaller values need more points, larger values fewer.

Merge: Menu ‣ Stroke ‣ Simplify – Merge. Simplifies by merging points closer than a specified distance.

Distance: maximum distance between vertices for merging.

[Related references](INDEX.md).
