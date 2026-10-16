# String to Curves Node: Text Box

### Text Box

Overflow

Overflow: Wrap at Text Box Width.

Scale To Fit: Shrink text to fit both dimensions.

Truncate: Output only characters within the bounds;
move the rest to Remainder.

Text Box Width
Maximum width per line; words are not broken.

Text Box Height
Maximum height for all lines.

**Outputs**

Curve Instances
Geometry with one instance per character.

Remainder
Text that did not fit (Truncate mode only).

Line
Attribute field: line index per character (instance domain).

Word
Attribute field: word index per character (instance domain).

Pivot Point
Position of the selected Pivot Point in each instance's local space.

**Examples**

Create text boxes that overflow: unfit text from one String to Curves node
(with fixed text box) feeds into another, scaled to fit via a Scale to Fit node.

[Related references](INDEX.md).
