# Double Edge Mask Node

## Double Edge Mask Node

The Double Edge Mask node makes a gradient between two masks. Inputs: Outer Mask (the outside shape, fading from black at its own edges to white where it meets the Inner Mask); Inner Mask (the inside shape, fully white); Images Edges (when on, the image edges that intersect the outer mask count as outer-mask edges; otherwise the outer mask is open-ended); and Only Inside Outer (when on, only inner-mask edges inside the outer mask count; otherwise all inner-mask edges do). Output: Mask (standard mask output).

[Related references](INDEX.md).
