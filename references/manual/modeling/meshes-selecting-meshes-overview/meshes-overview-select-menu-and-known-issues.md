# Introduction: Select Menu, Known Issues, Dense Meshes, N-Gons in Face Select Mode

### Select Menu

All A
Select all.

None Alt - A
Select none.

Invert Ctrl - I
Swap selected and unselected geometry.

Box Select B
Interactive box selection.

Circle Select C
Interactive circle selection.

Lasso Select
Interactive free-form selection.

Select Mirror Shift - Ctrl - M
Mirror the selection to the mesh's other side.

Select Random
Grabs a random set of vertices, edges, or faces by percentage.

Checker Deselect
Drops every other element, keyed off the active one.

More/Less

More Ctrl - NumpadPlus
Push the selection outward to the bordering elements.

Less Ctrl - NumpadMinus
Pull the selection in, dropping its border elements.

Next Active Shift - Ctrl - NumpadPlus
Picks the element that "logically follows" your last two.

Previous Active Shift - Ctrl - NumpadMinus
Drops the last element and reactivates the one before it.

Select Similar Shift - G
Grabs elements resembling the current selection.

Select All by Trait
Grabs geometry hitting certain undesirable conditions.

Select Linked

Linked
Grabs everything joined, near or far, to the current selection.

Shortest Path
Grabs the elements on the shortest path between your last two.

Linked Flat Faces
Spreads to faces roughly coplanar with the selected ones.

Select Loops

Edge Loops
Grabs edges sharing an edge loop with the selected ones.

Edge Rings
Grabs edges sharing an edge ring with the selected ones.

Select Loop Inner-Region
Grabs the faces walled in by the selected boundary edges.

Select Boundary Loop
Trades the face selection for an edge selection of its borders.

Sharp Edges
Grabs edges at sharp corners.

Side of Active Vertex Mode
Grabs every vertex on one side, say the right, of the active vertex.

By Attribute
Grabs elements whose active attribute reads True.

### Known Issues

### Dense Meshes

With X-Ray off, a Box/Circle/Lasso Select over a dense mesh can miss vertices in the region because of overlap. If that happens, zoom in or turn on X-Ray to work around it.

### N-Gons in Face Select Mode

N-gon having its selection dot inside another face.

In X-Ray and Wireframe shading the face selection dot just sits at the face's center, which for a concave n-gon may not land on the face's surface. That can make the dot hard to find, all the more so when another face fills the cavity.

[Related references](INDEX.md).
