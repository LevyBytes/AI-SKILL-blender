# Points to Curves Node

## Points to Curves Node

Points to Curves Node

Generates a Curves geometry by converting all points to new curves. Point attributes propagate to Curve Points. Built-in curves attributes in points are ignored.

Tip: Link each point's weight to an attribute value to control order in the curve. Sorting and grouping use Weight and Group ID.

Inputs
Points: The Point Cloud geometry component.
Curve Group ID: Points with the same ID join in one curve. Any value works (negative, zero, infinity). Curves must have at least one point. Order depends on ID value and its order in the Point Cloud.
Weight: For curves with multiple points, Weight defines order via sorting. Minimal values start the curve, maximum end it. Same-weight points keep their original order.

Outputs
Curves: Curves with points joined from the Point Cloud. Other components don't save. Always non-cyclic.

Examples: Create curve arrays with connections by duplicating the Arc primitive, shifting each up by index, converting to Point Cloud, then back to curves. All Point Cloud attributes become curve point attributes.

[Related references](INDEX.md).
