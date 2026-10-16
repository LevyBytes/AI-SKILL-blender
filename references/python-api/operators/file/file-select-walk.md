# bpy.ops.file.select_walk

bpy.ops.file.select_walk(*, direction='UP', extend=False, fill=False)

Pick/un-pick items by traversing via keyboard

Parameters:

- direction (Literal['UP', 'DOWN', 'LEFT', 'RIGHT']) – Walk Direction, Step in this heading (optional)
- extend (bool) – Extend, Grow the roster in lieu of wiping everything (optional)

- fill (bool) – Fill, Mark everything from the preceding pick to here (optional)

Returns:

Result of the operator call.

Return type:

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
