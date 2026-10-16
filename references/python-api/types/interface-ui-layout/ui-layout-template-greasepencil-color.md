# bpy.types.UILayout: template_greasepencil_color ( data , property , * , rows = 0 , cols = 0 , scale = 1.0 , filter = 'ALL' )

template_greasepencil_color ( data , property , * , rows = 0 , cols = 0 , scale = 1.0 , filter = 'ALL' )

template_greasepencil_color

Parameters :

- data (AnyType) – Data from which to take property (never None)

- property ( str ) – Identifier of property in data (never None)

- rows ( int ) – Number of thumbnail preview rows to display, (in [0, inf], optional)

- cols ( int ) – Number of thumbnail preview columns to display, (in [0, inf], optional)

- scale ( float ) – Scale of the image thumbnails, (in [0.1, 1.5], optional)

- filter ( Literal [ 'ALL' , 'AVAILABLE' ] ) – Optionally limit the items which can be selected (optional)

[Related references](INDEX.md).
