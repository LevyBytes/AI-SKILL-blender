# Operator Type Flag Items

## Operator Type Flag Items

### Operator Type Flag Items

REGISTER :

Register.

Show it in the info window and allow the redo toolbar panel.

UNDO :

Undo.

Emit an undo event once the operator returns `FINISHED` (required for operator redo, and obligatory whenever the operator alters Blender data).

`UNDO_GROUPED` :

Grouped Undo.

Collapse repeated runs of this operator into one undo event.

BLOCKING :

Blocking.

Stop everything else from grabbing the cursor.

MACRO :

Macro.

Apply this to test whether a given operator is a macro.

`GRAB_CURSOR` :

Grab Pointer.

Make the operator capture mouse focus, switching on wrapping while continuous grab is active.

`GRAB_CURSOR_X` :

Grab Pointer X.

Grab, only warping the X axis.

`GRAB_CURSOR_Y` :

Grab Pointer Y.

Grab, only warping the Y axis.

`DEPENDS_ON_CURSOR` :

Depends on Cursor.

The starting cursor position matters; launched from a menu or button, the user is asked to set the cursor first.

PRESET :

Preset.

Show a preset button alongside the operator's settings.

INTERNAL :

Internal.

Take the operator out of the search results.

`MODAL_PRIORITY` :

Modal Priority.

Process events ahead of other modal operators that lack this flag. Apply it carefully, and do not alter data that those operators expect to stay constant while they run..

[Related references](INDEX.md).
