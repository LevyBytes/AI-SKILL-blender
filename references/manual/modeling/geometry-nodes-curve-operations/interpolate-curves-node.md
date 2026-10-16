# Interpolate Curves Node

## Interpolate Curves Node

The Interpolate Curves node generates new curves across positions by interpolating between existing ones. Useful for reducing edit effort (fewer guides, faster workflow) while maintaining high density for viewing and rendering.

Guide Curves: Base curves to interpolate.
Guide Up: Optional surface normal. Supplying it improves interpolation quality, grounding it to surface shape.

Tip: In typical child-hair setups, retrieve this normal via Sample UV Surface Node on the same surface plus Normal Node.

Guide Group ID: Splits guides into groups; new curves stay within one group. Prevents curves in different sections (different IDs) from influencing each other.

Points: First root positions of new curves.
Points Up: Optional surface normal.
Point Group ID: The group to interpolate within.
Max Neighbors: Closest guides to consider.

Curves: The guides plus interpolated curves.
Closest Index: Index of the nearest guide for each new curve.

Note: Internally, multiple guides are mixed; this output is only the dominant one.

Closest Weight: Strength of the nearest guide.

[Related references](INDEX.md).
