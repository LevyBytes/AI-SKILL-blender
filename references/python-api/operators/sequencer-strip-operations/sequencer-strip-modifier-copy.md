# bpy.ops.sequencer.strip_modifier_copy

bpy.ops.sequencer.strip_modifier_copy(*, type='REPLACE')

Apply modifiers of the active piece to all chosen pieces.

Parameters:

type (Literal['REPLACE', 'APPEND']) – Type, (optional)

- REPLACE
  Replace – Overwrite modifiers in place.
- APPEND
  Append – Attach active modifiers to chosen pieces.

Returns:

Operation result.

Return type:

set[Literal[Operator Return Items]]
bpy.ops.sequencer.strip_modifier_copy(*, type='REPLACE')

Apply modifiers of the active piece to all chosen pieces.

Parameters:

type (Literal['REPLACE', 'APPEND']) – Type, (optional)

- REPLACE
  Replace – Overwrite modifiers in place.
- APPEND
  Append – Attach active modifiers to chosen pieces.

Returns:

Operation result.

Return type:

set[Literal[Operator Return Items]]
bpy.ops.sequencer. strip_modifier_copy ( * , type = 'REPLACE' ) 

Carry the active strip's modifiers over to every selected strip

Parameters :

type ( Literal [ 'REPLACE' , 'APPEND' ] ) – Type, (optional)

- REPLACE
Replace – Overwrite the modifiers on the destination.

- APPEND
Append – Tack the active modifiers onto the selected strips.

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
