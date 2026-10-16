# bpy.types.TextCurve: align_x, align_y

align_x

Where text sits horizontally relative to the object or text-box center (default 'LEFT' )

- LEFT
Left – Push the text against the left edge.

- CENTER
Center – Keep the text centered.

- RIGHT
Right – Push the text against the right edge.

- JUSTIFY
Justify – Stretch lines so both margins line up.

- FLUSH
Flush – Stretch to both margins while spacing characters evenly.

Type :

Literal[‘LEFT’, ‘CENTER’, ‘RIGHT’, ‘JUSTIFY’, ‘FLUSH’]
align_y

Where text sits vertically relative to the object center (default '`TOP_BASELINE`' )

- TOP
Top – Anchor the text at the top.

- `TOP_BASELINE`
Top Baseline – Anchor at the baseline of the first line.

- CENTER
Middle – Anchor the text at its middle.

- `BOTTOM_BASELINE`
Bottom Baseline – Anchor at the baseline of the last line.

- BOTTOM
Bottom – Anchor the text at the bottom.

Type :

Literal[‘TOP’, ‘`TOP_BASELINE`’, ‘CENTER’, ‘`BOTTOM_BASELINE`’, ‘BOTTOM’]

[Related references](INDEX.md).
