# bpy.types.UILayout: progress

progress ( * , text = '' , text_ctxt = '' , translate = True , factor = 0.0 , type = 'BAR' )

Progress indicator

Parameters :

- text ( str ) – Override automatic text of the item (optional)

- text_ctxt ( str ) – Override automatic translation context of the given text (optional)

- translate ( bool ) – Translate the given text, when UI translation is enabled (optional)

- factor ( float ) – Factor, Amount of progress from 0.0f to 1.0f (in [0, 1], optional)

- type ( Literal [ 'BAR' , 'RING' ] ) – Type, The type of progress indicator (optional)

[Related references](INDEX.md).
