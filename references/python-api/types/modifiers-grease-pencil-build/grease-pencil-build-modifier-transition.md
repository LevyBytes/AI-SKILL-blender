# bpy.types.GreasePencilBuildModifier: transition

transition

Sets the way strokes animate: whether they appear or vanish (default 'GROW' )

- GROW
Grow – Show points in the order they occur in each stroke (e.g. for animating lines being drawn).

- SHRINK
Shrink – Hide points from the end of each stroke to the start (e.g. for animating lines being erased).

- FADE
Vanish – Hide points in the order they occur in each stroke (e.g. for animating ink fading or vanishing after getting drawn).

Type :

Literal[‘GROW’, ‘SHRINK’, ‘FADE’]

[Related references](INDEX.md).
