# bpy.types.GreasePencilDrawing: resize_strokes

resize_strokes ( sizes , * , indices = (0,) )

Resize all existing strokes. If indices are provided, resize only the strokes with the given indices. If the new size for a stroke is smaller, the stroke is trimmed. If the new size for a stroke is larger, the new end values are default initialized.

Parameters :

- sizes ( Sequence [ int ] ) – Sizes, The number of points in each stroke (array of 1 items, in [1, inf])

- indices ( Sequence [ int ] ) – Indices, The indices of the stroke to resize (array of 1 items, in [0, inf], optional)

[Related references](INDEX.md).
