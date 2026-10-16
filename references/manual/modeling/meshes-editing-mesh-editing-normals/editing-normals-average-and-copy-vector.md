# Editing Normals: Average, Copy Vector, Paste Vector

### Average 

Reference

Mode :

Edit Mode

Menu :

Mesh ‣ Normals ‣ Average

At each selected vertex, sorts the connected face corners into groups split by Sharp edges, then
sets each group's custom normals to a chosen average. The Adjust Last Operation panel offers:

Type

Custom Normal :

Set each group's face-corner custom normals to their average.

Face Area :

Set each group's face-corner custom normals to a weighted average of their face normals, weighted
by face area — bigger faces sway the final normal more.

Corner Angle :

As Face Area , but the weights come from the face-corner angles instead.

Weight
With Type set to Face Area or Corner Angle , the Weight steers which face normals the average
favors. At 50 you get a plain weighted average. At 100 the average rests entirely on the
largest-area faces (or largest-angle corners). At 1 it rests entirely on the smallest-area faces
(or smallest-angle corners).

Threshold
Tolerance value for treating face areas (or corner angles) as equal.

When custom normals are averaged across two vertices: a vertex with two separate groups of faces divided by Sharp edges gets two distinct averages, while a vertex without Sharp edges produces one average.

See also

The Weighted Normal Modifier achieves this without destructive changes.

### Copy Vector

Reference

Mode:

Edit Mode

Menu:

Mesh → Normals → Copy Vector

Transfers a single normal vector to an internal clipboard:

- If a face is selected, that face's normal gets transferred.

- If a vertex is selected, its normal gets transferred, but only when all its custom split normals match.

- If a face corner is selected, its custom split normal gets transferred.

### Paste Vector

Reference

Mode:

Edit Mode

Menu:

Mesh → Normals → Paste Vector

Places the previously copied normal vector onto selected face corners.
The Adjust Last Operation panel includes:

Absolute Coordinates
When enabled, selected face corners receive the pasted normal directly. When disabled, the pasted normal adds as an offset.

[Related references](INDEX.md).
