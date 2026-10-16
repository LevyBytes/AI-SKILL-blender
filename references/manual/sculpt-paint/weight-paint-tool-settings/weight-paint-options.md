# Options

### Options

Paint options.

Brush operation shifts with these paint parameters.

Auto Normalize
Maintains deforming group sums at unity during painting.
Off mode permits any weight between 0 and 1 per vertex.
Yet when animation uses groups for deformation,
Blender interprets weights relative to neighbors.
Blender perpetually normalizes all deform bones.
Practically, strict normalization stays unnecessary and
post-painting normalization preserves animation.

Works intuitively maintaining normalization atop
already-normalized data via different sources.

Lock-Relative
Shows bone groups as if all locked deform groups vanished,
with remaining ones recalculated for unity.
Intended for perfecting bone balance while others stay locked.
Temporarily examine non-normalized weights as normalized
without permanent changes.

Multi-Paint
Simultaneously paint multiple chosen groups, sustaining their balance.
Beneficial when tweaking regions touched by beyond-three bones,
like particular character zones.

Only functional in the Armature area, where multiple groups
activate via multiple chosen bones. Two or more chosen groups
shift viewport hue and paint behavior to Multi-Paint,
pooling selected group totals if Auto Normalize runs,
or averaging otherwise. Strokes affecting collective influence
apply to each group so relative ratios endure.

Since undefined ratios arise from all-zero weights, Multi-Paint skips
zero-weight vertices on applicable groups.
It prevents reducing weight to complete zero.
Combined with X Mirror , complete symmetrical effect
occurs solely with initially symmetrical weights.

Tip

Though Multi-Paint skips zero-weight vertices by default,
Smooth Weight tool can transplant fitting nonzero balance
from neighbors without exiting Multi-Paint or changing choices.

Engage vertex selection, mark targets, and apply one smoothing cycle
from Selected Pose Bones with modest Factor.
Then simply paint to assign target influence.

Restrict
Narrows painting reach to vertices (including zero-weight
ones) in the chosen group.

See also

See the Brush Display options.

[Related references](INDEX.md).
