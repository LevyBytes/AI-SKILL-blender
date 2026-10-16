# bpy.types.UILayout: separator, separator_spacer

separator ( * , factor = 1.0 , type = 'AUTO' )

Item. Adds a gap between neighbouring items in the layout.

Parameters :

- factor ( float ) – Percentage, Fraction of the width to leave empty; omit it to fall back to the standard gap (in [0, inf], optional)

- type ( Literal [ 'AUTO' , 'SPACE' , 'LINE' ] ) – Type, Which kind of separator to draw (optional)

- AUTO
Auto – Best guess at what type of separator is needed..

- SPACE
Empty space – Horizontal or Vertical empty space, depending on layout direction..

- LINE
Line – Horizontal or Vertical line, depending on layout direction..
separator_spacer ( )

Item. Adds a stretchy horizontal gap between layout items.

[Related references](INDEX.md).
