# Bone Roll

## Bone Roll

The bone roll is the part of a bone's rest pose that sets its default rotation about its own length, edited in Edit Mode. Recalculate Roll (Edit Mode; Armature ‣ Bone Roll ‣ Recalculate Roll; Shift-N) aligns the roll of all selected bones to a reference: Local Tangent (X, Z, -X, -Z) aligns relative to the axis defined by each bone and its parent — if a bone has no parent it uses the first child instead (even an unconnected one), and for a bone with neither parent nor children it does nothing; Global Axis (X, Y, Z, -X, -Y, -Z) points each bone's Z axis toward the chosen global axis; Active Bone points their Z axes where the active bone's Z currently points; View Axis points their Z axes along the viewport's forward/backward axis (toward the viewer); and Cursor points them at the 3D cursor. Flip Axis shifts the result by 180°, and Shortest Rotation flips by 180° only when needed to keep the absolute roll under 90° (so an initial 160° becomes -20°). Set Roll (Edit Mode; Armature ‣ Bone Roll ‣ Set Roll; Ctrl-R) tweaks the roll of all selected bones, and Clear Roll (Edit Mode; Armature ‣ Bone Roll ‣ Clear Roll; Alt-R) sets it to 0°.

[Related references](INDEX.md).
