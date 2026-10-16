# Fill Between Joints

## Fill Between Joints

Fill Between Joints (Edit Mode; Armature ‣ Fill Between Joints; F) mainly makes one bone between two selected joints, like "create edges/faces" in mesh editing. With one root and one tip selected, the new bone's root goes on the selected tip, its tip on the selected root, and it's parented and connected to the bone owning the selected tip. With two tips selected, the root goes on whichever tip is nearer the 3D cursor, the tip on the other, and it's parented and connected to the bone owning the root-side tip. With two roots selected you hit a quirk of Blender's event system not updating the UI in real time: pressing F gives a bone with its root on whichever root is nearer the 3D cursor, its tip on the other, and parented/connected to the owner of the root-side root — and trying to move the new bone triggers a UI update that shows its root snapping to the parent bone's tip. Pressing F with one joint selected makes a bone from that joint to the 3D cursor, parented to no bone. You'll get an error if you try to fill two joints of the same bone, or more than two joints.

[Related references](INDEX.md).
