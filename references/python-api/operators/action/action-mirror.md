# bpy.ops.action.mirror

bpy.ops.action. mirror ( * , type = 'CFRA' )

Reflect picked keyframes across a centerline.

Parameters :

type ( Literal [ 'CFRA' , 'XAXIS' , 'MARKER' ] ) – Type, (optional)

- CFRA
By Times Over Current Frame – Mirror frame positions relative to the active frame.

- XAXIS
By Values Over Zero Value – Mirror value magnitudes (negatives become positive and vice versa).

- MARKER
By Times Over First Selected Marker – Mirror frame positions using the earliest picked marker as the axis.

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
