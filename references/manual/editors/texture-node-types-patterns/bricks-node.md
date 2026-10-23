# Bricks Node

## Bricks Node

The Bricks node builds a brick-like pattern.

Inputs:
Bricks 1, Bricks 2: the bricks' color range; each brick's color is chosen at random between these two.
Mortar: the mortar color between the bricks.
Thickness: the mortar's thickness.
Bias: the bias of the random color pick, from -1 to 1; -1 makes every brick Color 1 and 1 makes them all Color 2.
Brick Width: the horizontal size of every brick.
Row Height: the vertical size of every brick.

Properties:
Offset: the relative offset of the next brick row.
Frequency: offset every N rows; the offset pattern repeats every N rows.
Squash: squeezes the bricks in those repeating N-row groups by this amount.
Frequency: squash every N rows.

Outputs:
Color: the usual color output.

[Related references](INDEX.md).
