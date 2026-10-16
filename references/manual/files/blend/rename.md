# Rename

## Rename

Rename Active Item — Reference: Menu: Edit ‣ Rename Active Item; Shortcut: F2. Renames the active Bone, Node, Object, and Sequence Strip. Running it pops a dialog whose text field holds the current name for you to overwrite; Return confirms, Esc cancels.

Batch Rename — Reference: Menu: Edit ‣ Batch Rename; Shortcut: Ctrl-F2. Renames many data-block names at once via a pop-up of operations and their options, applied one after another, top to bottom.
Data Source — where Blender looks for the data-blocks to rename. Selected (the currently selected objects) or All (all data in the blend file).
Data Type — which data-block type to run the batch rename on.
Operations — Batch Rename has several sub-operations for changing names; the default is Find/Replace, but you can add others to refine the names further, and each reports in the status bar how many data-blocks it renamed.
Find/Replace — searches for a piece of text in the names and optionally swaps in new text; Regular Expressions can tailor the Find/Replace text and are enabled by the icon to the right of the fields.
  Find — the text to search for.
  Replace — the text to substitute into matching names.
  Case Sensitive — matches the Find text's case exactly.
Set Name — works most like Rename Active Item, renaming the current data-block without a find-and-replace.
  Method — New (drops the current name for the "new" one), Prefix (adds text at the front, handy for tools that look for special prefix text), or Suffix (adds text at the end, for tools that look for special suffix text).
  Name — the new name or the text to add as prefix/suffix.
Strip Characters — tidies names by removing certain character types from the start or end.
  Characters — Spaces (e.g. "Living Room " becomes "Living Room"), Digits (e.g. cube.001 becomes cube.), or Punctuation (,.?!:; and the like, e.g. cube? becomes cube). Tip: remove several types at once with Shift-LMB on them.
  Strip From — Start (leading characters) or End (trailing characters).
Change Case — sets a name's case to one of:
  Convert To — Upper Case (e.g. cube.001 becomes CUBE.001), Lower Case (e.g. CUBE.001 becomes cube.001), or Title Case (e.g. living room becomes Living Room).

[Related references](INDEX.md).
