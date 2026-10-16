# Symmetrize

## Symmetrize

Symmetrize (Edit Mode; Armature ‣ Symmetrize) mirrors selected bones across the X axis using Blender's symmetrical-naming convention, going left-to-right or right-to-left depending on the selection: when matching bones are selected on both sides, mirroring runs right to left; bones whose opposite-named counterparts don't exist are created and existing ones are overwritten; and bones that can't be classified left or right are skipped. Symmetrized bone and constraint properties are adjusted to mirror their behavior, and on bones that have Action Constraints, keyframes get written into the target Action so motion stays symmetrical when it's activated (bone or constraint drivers are neither created nor affected). Bone-collection assignments are symmetrized too — collections following the convention are mirrored, and a missing one is created and parented to the same collection as the original — though Blender doesn't stop a left bone from being assigned to a right collection, in which case the resulting right bone ends up in the left collection.

[Related references](INDEX.md).
