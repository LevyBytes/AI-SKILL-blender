# Reconstruction: Set Origin, Set Floor

## Reconstruction

Align 3D bundles and reconstructed geometry within your scene using orientation operators.

Set Origin
Reference
Mode: Tracking
Menu: Reconstruction ‣ Set Origin

Reposition the camera so your active track sits at the origin; applies translation only.

Set Floor
Reference
Mode: Tracking
Menu: Reconstruction ‣ Set Floor

Three markers define a horizontal reference plane; camera shifts to place these markers at Z = 0.

Set Wall
Reference
Mode: Tracking
Menu: Reconstruction ‣ Set Wall

Anchors a vertical plane instead of horizontal—selected tracks align to the XZ plane.

Set X/Y Axis
Reference
Mode: Tracking
Menu: Reconstruction ‣ Set X/Y Axis

Positions your active track along the X or Y axis without moving the origin point.

Set Scale
Reference
Mode: Tracking
Menu: Reconstruction ‣ Set Scale

Scales camera or object to make the distance between two marks match a specified value.

Apply Solution Scale
Reference
Mode: Tracking
Menu: Reconstruction ‣ Apply Solution Scale

Permanently scales the tracking solution instead of the camera.

Link Empty to Track
Reference
Mode: Tracking
Menu: Reconstruction ‣ Link Empty to Track

Creates an empty and constrains it to follow the active track.

3D Markers to Mesh
Reference
Mode: Tracking
Menu: Reconstruction ‣ 3D Markers to Mesh

Converts solved track positions into mesh vertices; builds a starting point for hand-sculpting geometry. A motion solve must complete first; only the current tracking object contributes.

[Related references](INDEX.md).
