# String to Curves Node: Alignment, Spacing

## String to Curves Node

Converts text into curve instances. Each unique character becomes a curve once;
further uses become instances of that geometry. Instance names match their character.

Result is memory-efficient (unique characters process once) but each character instance is identical.
To process each character individually, use Realize Instances Node.

Tip: Hold the mouse over the socket to view the evaluated string value via socket inspection.

**Inputs**

String
Standard string input.

Size
Character size; all other inputs scale by this value.

Font
Typeface for curve generation.

### Alignment

Align X

Left: Left-aligned.

Center: Centered.

Right: Right-aligned.

Justify: Flush left and right.

Flush: Flush left and right with equal spacing.

Align Y

Top: Top-aligned.

Top Baseline: Baseline-aligned to top.

Middle: Vertically centered.

Bottom Baseline: Baseline-aligned to bottom.

Bottom: Bottom-aligned.

Pivot Point

Midpoint: Center of each character's bounds.

Top Left: Top-left corner.

Top Center: Midpoint of the top edge.

Top Right: Top-right corner.

Bottom Left: Bottom-left corner.

Bottom Center: Midpoint of the bottom edge.

Bottom Right: Bottom-right corner.

### Spacing

Character Spacing
X-axis kerning scale factor.

Word Spacing
X-axis whitespace scale factor between words.

Line Spacing
Distance between lines, multiplied by Size.

[Related references](INDEX.md).
