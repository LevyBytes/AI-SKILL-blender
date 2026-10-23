# Curve to Tube Node

## Curve to Tube Node

Curve to Tube Node

Generates a mesh tube following an input curve with cylind­rical or custom-profiled cross-section. Useful for cables, pipes, wires, and tubing models.

Inputs:
Curve: Input spline.
Scale: Radius multiplier on the curve's radius attribute.

Profile:
Profile Mode - Shape definition:
Round: Circular cross-section.
Custom: Custom object or geometry profile.
Resolution Round: Circle resolution (also cap resolution).
Profile Input Custom - Profile source:
Object: Single object.
Geometry: Input geometry.
Object / Geometry Custom: Profile specification.
Shade Smooth: Enable smooth shading.

Resample: Curve preprocessing for uniform geometry distribution:
Resample Mode - Method:
Evaluated: Existing evaluated points.
Auto: Automatic sample length.
Count: Fixed sample count.
Length: Fixed distance between samples.
Scale Auto: Auto-mode length multiplier.
Count Count: Sample point count.
Length Length: Sample spacing.

Caps - End-fill strategy:
Caps Type - Approach:
Flat: Single n-gon per end.
Round: Semicircle per end.
Custom: User-provided geometry.
Smooth Flat Round: Smooth tube-to-cap transition.
Caps Input Custom - Cap source:
Object: Single object.
Geometry: Input geometry.
Start / End Custom: Per-end cap objects or geometry.

UV Map:
Name: Map name.
Parameter U/V - UV generation:
Factor: 0–1 normalization along curve and profile.
Length: Real length and circumference.
Index: Point indices.
Consider Curve Radius: Account for radius variation.

Outputs:
Mesh: Tube output including optional caps and UVs.

## Curve to Tube Modifier

This node generates a mesh tube along an input curve, creating cylindrical or profiled geometry following the curve shape, useful for modeling cables, pipes, wires, and other tubular forms.

Scale multiplies the curve's radius attribute to determine the output tube's radius.

Profile Mode: Round uses a circular cross-section (with configurable resolution), Custom uses a provided object or geometry as the profile shape.

Resolution Round controls the number of points around the circular profile and sets cap resolution.

Profile Input Custom can source from an Object or from input Geometry directly.

Shade Smooth enables smooth shading on the output.

Resampling reorders the curve before tube generation for evenly distributed geometry. Resample Mode: Evaluated uses existing curve points, Auto calculates sample spacing automatically, Count fixes the point count, Length fixes the spacing distance.

Scale Auto applies a multiplier to the automatic resample length.

Caps fill tube ends: Flat uses an n-gon, Round uses a half-circle, Custom uses provided geometry or an object. Smooth transitions between tube body and caps instead of creating hard edges.

UV Map generation creates or updates a UV map on the output. Parameter U and V can use Factor (normalized 0-1), Length (real curve length and circumference), or Index (point and profile indices). Consider Curve Radius includes radius variations in UV generation.

[Related references](INDEX.md).
