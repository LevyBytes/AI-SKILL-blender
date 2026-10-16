# bpy.ops.file.select_all

bpy.ops.file.select_all(*, action='TOGGLE')

Mark or unmark all items

Parameters:

action (Literal['TOGGLE', 'SELECT', 'DESELECT', 'INVERT']) – Action, Choice work to carry out (optional)

- TOGGLE
Toggle – Swap selection for every part.

- SELECT
Select – Mark every part.

- DESELECT
Deselect – Unmark every part.

- INVERT
Invert – Flip which are marked.

Returns:

Result of the operator call.

Return type:

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
