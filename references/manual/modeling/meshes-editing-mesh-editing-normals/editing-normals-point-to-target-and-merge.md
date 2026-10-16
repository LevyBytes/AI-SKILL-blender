# Editing Normals: Point to Target, Merge, Split

### Point to Target 

Reference

Mode :

Edit Mode

Menu :

Mesh ‣ Normals ‣ Point to Target

Shortcut :

Alt - L

Aims the custom split normals of the selected face corners at a chosen target. After the menu
item or shortcut, set the target by pressing one of these (also shown in the status bar):

- M for the mouse cursor.

- L for the Pivot Point.

- O for the object origin.

- Ctrl - LMB for the 3D Cursor. This also changes the location of the Cursor.

- Ctrl - RMB for a certain vertex, edge, or face. Make sure not to click a space where there's no geometry,
as doing so will extrude the selection instead.

In addition, the following options are available:

Invert I
Aim the normals away from the target instead.

Align A
Send every normal one way: from the selected vertices' average position toward the target.

Spherize S
Blend each normal between its starting and new orientation. Set the blend amount in the Adjust
Last Operation panel after confirming.

Reset R
Restore the custom normals to their state when the operation began.

Once the normals are set, press LMB or Return to confirm. The options above stay editable
afterward in the Adjust Last Operation panel.

### Merge 

Reference

Mode :

Edit Mode

Menu :

Mesh ‣ Normals ‣ Merge

Smooth-shades the selected faces and clears the Sharp mark on the selected edges. Then, at each
selected vertex, it averages the custom normals belonging to smooth-shaded faces. (Those
belonging to flat-shaded faces stay as they are.)

To average the custom normals regardless of face selection, use the Average
operator.

### Split 

Reference

Mode :

Edit Mode

Menu :

Mesh ‣ Normals ‣ Split

Flat-shades the selected faces and marks the selected edges Sharp. Then, at each selected vertex,
it sets every custom normal on a flat-shaded face to that face's normal. (Normals on a
smooth-shaded face are set to the average of those faces' normals.)

[Related references](INDEX.md).
