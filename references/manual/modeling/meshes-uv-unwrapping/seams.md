# Seams

## Seams

Seams

For many simple models, Cube, Cylinder, Sphere, or standard Unwrap operators produce good UV layouts. Complex meshes with heavy indentations benefit from defined seams to guide and limit the unwrap operation.

Like fabric seams, a seam marks where image/cloth edges join. In unwrapping, the UV map is discontinuous at seams — think of peeling an orange or skinning an animal. You make cuts, peel away the skin, then flatten it with some stretching. These cuts are seams.

A simple seam illustration shows a cylindrical mesh with one seam cut.

Balance seam quantity against stretching. More seams reduce stretching but complicate texturing. Aim for few seams with minimal stretching. Hide seams in inconspicuous locations. With 3D projection painting, seams matter less; with 2D texturing, edge matching across seams is difficult.

Workflow

Mark seams.

Unwrap.

Adjust seams and iterate.

Manually refine UVs.

Marking Seams

Editor: 3D Viewport or UV Editor
Mode: Edit Mode
Toolbar/Menu: UV ‣ Mark/Clear Seam or Edge ‣ Mark/Clear Seam

Select an edge and press Ctrl - E to mark a seam, or Ctrl - E to clear it.

The back edge of a cylinder shows seaming applied to hide the seam, with standard unwrap producing clean face distribution.

Use Select Linked in Face Select mode to verify seams. It selects all connected faces up to a seam. If unintended faces are selected, your seam isn't continuous (though continuous seams aren't strictly required).

Think of seaming as cutting and spreading the object flat with minimal tearing. On the example model, the back-most cylinder edge is seamed, side seams separate head halves, and ear edges separate front from back. Eyes are disconnected sub-meshes and unwrap independently. A vertical seam runs along the back of the head so each side flattens separately.

Seams also limit unwrapped regions. For texturing a head, you might not need the top/back scalp (hidden by hair), so define a seam at the hairline. Select a frontal face and linked faces before unwrapping; the selection stops at the hairline, leaving the scalp unwrapped.

For bilateral objects (heads, bodies), seam along the mirror axis — split the head or body down the middle in front view. On unwrap, overlay both halves onto the same texture space so pixels for the right side match the left, and the right face matches the left.

Note: You don't need "one perfect unwrapping everywhere". You can have multiple UV unwrappings with different approaches in different areas.

Seams from Islands

Mode: View mode
Menu: UV ‣ Seams from Islands

Adds seams at the boundaries of existing UV islands, useful for modifying the UVs of already-unwrapped meshes.

[Related references](INDEX.md).
