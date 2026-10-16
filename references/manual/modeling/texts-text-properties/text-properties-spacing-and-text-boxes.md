# Text Properties: Spacing, Text Boxes

### Spacing

Character Spacing
A multiplier that scales the width of the space between characters (kerning).

Within Edit Mode in the 3D Viewport, individual kerning at the text cursor
can be dialed down or up with Alt - Left / Alt - Right too.

Word Spacing
A multiplier that scales the width of the whitespace between words.

Line Spacing
A multiplier that scales the vertical space between lines.

Offset X, Y
Govern where the text sits within the object along X and Y.
This is reckoned relative to the object's origin — applied to the whole text, or to each frame once text boxes are in use.

### Text Boxes

Reference

Mode :

All

Panel :

Properties ‣ Data ‣ Text Boxes

Text boxes (frames) let you spread the text across rectangular regions inside one text object.
You can have any number of freely movable, resizable text frames per text object.

Text runs continuously from the lowest-numbered frame up to the highest, word-wrapped
inside each frame.
It spills into the next frame once a lower-numbered one can't hold any more.
Reach the last frame and text simply overflows it (by default — see the options below).

Text Boxes panel.

Add Textbox
Drops in a new frame right after the current one (in text-flow order).
It inherits the size and position of the selected frame.

(Remove Text Block)
Gets rid of the current frame.

Overflow
What becomes of text that spills past the room available in the defined boxes.

Overflow :

Simply let the text spill on out of the final box.

Scale to Fit :

Shrink the text down until it fits the room on hand.

Truncate :

Cut off whatever text won't fit the available room.

Note

Truncation only happens in Object Mode ;
in Edit Mode the whole text stays visible (and overflows as needed).

Size X, Y
Sets the text box's width and height; at zero no word wrapping occurs
(the value is ignored, and the entire text-box system shuts off when all are set to null).

Offset X, Y
Govern where the frame sits along X and Y, i.e. its position.

Multiple columns, text flowing between boxes.

[Related references](INDEX.md).
