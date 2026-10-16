# Duplicate

## Duplicate

Duplicate (Edit Mode; Armature ‣ Duplicate; Shift-D) works on selected bones (selected joints are ignored): as in mesh editing, Shift-D copies them, leaves the copies selected in move mode so you can place them, and preserves the chain when you duplicate part of one (the copied bones keep the same interconnections). A duplicate of a parented bone is parented to the same bone even if that root wasn't part of the selection — but if a bone was parented and connected to an unselected bone, its copy is parented but not connected to that unselected bone (so a duplicated Bone.006 is parented but not connected to Bone.001, shown by a black dashed line, and likewise Bone.007 to Bone.003).

[Related references](INDEX.md).
