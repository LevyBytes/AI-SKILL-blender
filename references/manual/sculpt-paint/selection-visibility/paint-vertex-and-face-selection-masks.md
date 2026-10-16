# Selection & Visibility: Selection Masking, Details About Selecting, Vertex Selection Masking, Face Selection Masking

## Selection & Visibility

### Selection & Visibility

### Selection Masking

When dealing with geometrically complex meshes, targeting intended vertices precisely can prove challenging. Perhaps you wish to paint only a constrained region while leaving surrounding areas unaltered. Selection masking addresses this scenario. Enabling this feature restricts brush application to only chosen vertices or faces. Access the feature via the 3D Viewport header (look for icons in the yellow-highlighted area):

You may select between Face Selection masking (leftmost), Vertex selection masking (center), and Bone selection (rightmost). The latter applies exclusively when the mesh has an Armature modifier. 

Selection masking provides advantages relative to standard paint mode:

- Mesh topology remains visible, even with active modifiers.

- Adjust face selection directly without switching to Edit Mode.

### Details About Selecting

The following standard operations work with selection:

- Alt - LMB – Individual faces

- Shift - Alt - LMB – Add or remove from selection.

- A – Toggle all, A A to empty selection.

- B – Box selection.

- C – Circle brush selection.

- Ctrl - I – Flip selection state.

- L – Grab connected geometry (under cursor).

- Ctrl - L – Grab all linked geometry.

- Ctrl - NumpadPlus – Expand perimeter

- Ctrl - NumpadMinus – Contract perimeter

- Alt - LMB – Vertex Loop Select

### Vertex Selection Masking

Reference

Mode :

Vertex and Weight Paint Modes

Header :

Vertex Selection

Shortcut :

2

In this mode you can pick individual or multiple vertices and restrict paint operations to those alone. All other vertices receive protection from unintended edits.

Vertex Selection masking.

### Face Selection Masking

Reference

Mode :

Texture, Vertex, and Weight Paint Modes

Header :

Paint Mask

Shortcut :

1

This method restricts painting to user-chosen faces, working much like vertex selection masking.

Face Selection masking.

[Related references](INDEX.md).
