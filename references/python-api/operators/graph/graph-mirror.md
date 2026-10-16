# bpy.ops.graph.mirror

bpy.ops.graph.mirror(*, type='CFRA')

Reverse the chose frames over the chose flip position

Parameters:

type (Literal['CFRA', 'VALUE', 'YAXIS', 'XAXIS', 'MARKER']) – Type, (optional)

- CFRA
By Times Over Current Frame – Reverse timings of the chose frames utilizing the active timing as the flip position.

- VALUE
By Values Over Cursor Value – Reverse worths of the chose frames utilizing the arrow worth (Y/Straight component) as the flip position.

- YAXIS
By Times Over Zero Time – Reverse timings of the chose frames, successfully turning around the order they display in.

- XAXIS
By Values Over Zero Value – Reverse worths of the chose frames (i.e. downward principles become upward, and the other way around).

- MARKER
By Times Over First Selected Marker – Reverse timings of the chose frames utilizing the initial chose sign as the marker.

Returns:

Result of the operator call.

Return type:

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
