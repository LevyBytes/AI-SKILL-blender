# Header

## Header

Every constraint has a header: Expand/Collapse (show or hide its settings — a collapsed constraint stays active); the type Icon (red when one or more settings aren't correctly filled in, so the constraint has no effect); Name (initially the type, customizable to something specific); Enabled (turn the constraint on or off while keeping its settings — another way to disable it is setting Influence to zero, which, unlike Enabled, can be animated); and an Extras menu with Apply (Ctrl-A — apply the constraint's result to the owner's own transform, then delete it, with a warning that applying a constraint not first in the stack ignores the ones before it and may give wrong results; see Apply Visual Transform to apply all constraints' combined result without deleting them), Duplicate (Shift-D — make a copy just below this one), Copy to Selected (copy from the active object to all selected objects), Move to First/Last (move it to the top or bottom of the stack), and Delete (X — remove it, losing its settings). A Move handle lets you drag the constraint up or down, which can change the outcome since the stack evaluates top to bottom.

[Related references](INDEX.md).
