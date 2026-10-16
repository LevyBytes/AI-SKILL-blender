# bpy.types.GreasePencilBuildModifier: mode

mode

Controls the way strokes get built (default 'SEQUENTIAL' )

- SEQUENTIAL
Sequential – Strokes appear/disappear one after the other, but only a single one changes at a time.

- CONCURRENT
Concurrent – Multiple strokes appear/disappear at once.

- ADDITIVE
Additive – Builds only new strokes (assuming ‘additive’ drawing).

Type :

Literal[‘SEQUENTIAL’, ‘CONCURRENT’, ‘ADDITIVE’]

[Related references](INDEX.md).
