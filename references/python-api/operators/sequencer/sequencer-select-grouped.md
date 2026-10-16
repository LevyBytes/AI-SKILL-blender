# bpy.ops.sequencer.select_grouped

bpy.ops.sequencer.select_grouped(*, type='TYPE', extend=False, use_active_channel=False)

Pick all pieces arranged by varied properties.

Parameters:

- type (Literal['TYPE', '`TYPE_BASIC`', '`TYPE_EFFECT`', 'DATA', 'EFFECT', '`EFFECT_LINK`', 'OVERLAP']) – Type, (optional)
  - TYPE
    Type – Common piece category.
  - `TYPE_BASIC`
    Global Type – All pieces of same general category (pictorial or auditory).
  - `TYPE_EFFECT`
    Effect Type – Common piece effect category (if active piece is not an effect one, pick all non-effect pieces).
  - DATA
    Data – Common information (scene, picture, sound, etc.).
  - EFFECT
    Effect – Common effects.
  - `EFFECT_LINK`
    Effect/Linked – Other pieces impacted by the active one (overlapping timing, and below or effect-connected).
  - OVERLAP
    Overlap – Overlapping duration.
- extend (bool) – Extend, Add to choice instead of clearing prior choice (optional)
- use_active_channel (bool) – Same Channel, Only think about pieces on the identical track as the active one (optional)

Returns:

Operation result.

Return type:

set[Literal[Operator Return Items]]
bpy.ops.sequencer.select_grouped(*, type='TYPE', extend=False, use_active_channel=False)

Pick all pieces arranged by varied properties.

Parameters:

- type (Literal['TYPE', '`TYPE_BASIC`', '`TYPE_EFFECT`', 'DATA', 'EFFECT', '`EFFECT_LINK`', 'OVERLAP']) – Type, (optional)
  - TYPE
    Type – Common piece category.
  - `TYPE_BASIC`
    Global Type – All pieces of same general category (pictorial or auditory).
  - `TYPE_EFFECT`
    Effect Type – Common piece effect category (if active piece is not an effect one, pick all non-effect pieces).
  - DATA
    Data – Common information (scene, picture, sound, etc.).
  - EFFECT
    Effect – Common effects.
  - `EFFECT_LINK`
    Effect/Linked – Other pieces impacted by the active one (overlapping timing, and below or effect-connected).
  - OVERLAP
    Overlap – Overlapping duration.
- extend (bool) – Extend, Add to choice instead of clearing prior choice (optional)
- use_active_channel (bool) – Same Channel, Only think about pieces on the identical track as the active one (optional)

Returns:

Operation result.

Return type:

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
