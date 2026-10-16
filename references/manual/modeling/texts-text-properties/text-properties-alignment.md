# Text Properties: Alignment

### Alignment

Horizontal

Left :

Pushes text to the left edge of the frames when frames are in use;
otherwise it treats the text object's origin as the text's starting point, growing rightward.

Center :

Centers text within the frames when frames are in use;
otherwise it treats the text object's origin as the text's midpoint,
growing equally left and right.

Right :

Pushes text to the right edge of the frames when frames are in use;
otherwise it treats the text object's origin as the text's end point, growing leftward.

Justify :

Flushes a line only when a word wrap ends it ( not a newline),
filling lines with whitespace rather than character spacing (kerning).

Flush :

Flushes every line, even one that's still being typed in.
It fills lines using character spacing (kerning).

Note

Both Justify and Flush only work within frames.

Vertical

Top :

- Using frames, the text's top edge snaps to the frames' top edge.

- Without a frame, the text's top edge meets the object's origin and the text grows downward.

Top Baseline :

- Using frames, the text's 'top' baseline snaps to the frames' top edge.

- Without a frame, the text's actual baseline meets the object's origin
and the text grows downward.

Note

That shift in reference point on the first line,
depending on whether boxes are used, is admittedly confusing.

Middle :

- Using frames, the text is centered within them.

- Without a frame, the text is centered on the object's origin
and grows upward and downward in equal measure.

Bottom Baseline :

- Using frames, the text's baseline snaps to the frames' bottom edge.

- Without a frame, the text's baseline meets the object's origin and the text grows upward.

Bottom :

- Using frames, the text's bottom edge snaps to the frames' bottom edge.

- Without a frame, the text's bottom edge meets the object's origin and the text grows upward.

[Related references](INDEX.md).
