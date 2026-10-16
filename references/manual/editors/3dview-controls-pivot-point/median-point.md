# Median Point

## Median Point

Reference — Mode: Object Mode and Edit Mode. Location: Header ‣ Transform Pivot Point ‣ Median Point. Shortcut: Period.

Sets the pivot at the mean location of whatever is currently selected.

In Object Mode that mean is derived purely from the origins of the chosen objects; their actual shape and dimensions play no part. Since an origin may sit anywhere — even outside the object's own mesh — the resulting Median Point can land somewhere other than you'd intuitively guess.

In Edit Mode the value is instead the average of the selected vertices, so the pivot drifts toward whichever region packs in the most geometry. Picture two equally sized cubes: with matching vertex counts the pivot rests exactly between them, but subdividing one of the two drags the pivot strongly toward that denser cube even though neither has changed in size.

[Related references](INDEX.md).
