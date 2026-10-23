# Input Fields

## Input Fields

Text & Search Fields: a text field has a rounded rectangular border and may show an icon and/or text inside it. Text fields hold text strings and let you edit with the usual text-editing shortcuts:
- Home: go to the start of the line.
- End: go to the end of the line.
- Left, Right: move the cursor one character.
- Ctrl-Left, Ctrl-Right: move the cursor a whole word.
- Backspace, Delete: delete characters.
- Ctrl-Backspace, Ctrl-Delete: delete words.
- Shift: hold while moving the cursor to select.
- Ctrl-A: select all text.
- Ctrl-C: copy the selected text.
- Ctrl-X: cut the selected text.
- Ctrl-V: paste text at the cursor position.
For text fields with an icon and pop-ups, see Data ID.

Number Fields: these store values and units. The first kind shows left (<) and right (>) triangles on its sides when the pointer is over it. Sliders, a second kind, carry a colored background bar showing a value across a range, such as a percentage. You can edit the value several ways:
Incremental Steps: click LMB on the small triangles to step by units (not available for sliders); you can also use Ctrl-Wheel while hovering over the field to change the value.
Dragging: hold LMB and drag left or right to change the value with the mouse; hold Ctrl to snap to discrete steps while dragging, or Shift for precision input.
Keyboard Input: press LMB or Return to type the value. While typing, number fields behave like text fields:
- press Return, or LMB outside the field, to apply the change;
- press Esc or RMB to cancel;
- press Tab to jump to the next field, or Shift-Tab to go to the previous one;
- press Minus while hovering over a number field to negate the value.

Multi-Value Editing: edit several number fields at once by pressing LMB on the first field and dragging vertically across the fields you want, then either drag left or right to set the value with the mouse, or release LMB and type one in.

Value Limits: most numeric values are bounded by a "soft limit" and a "hard limit" range. Dragging with the mouse stays within the soft limit; keyboard entry can go wider, but never past the hard limit.

Expressions: you can type mathematical expressions into any number field — for example 3*2 or 10/5+4 instead of 6 — and even constants like pi (3.142) or functions like sqrt(2) (the square root of 2). These are evaluated by Python; for all available math expressions, see the Math module reference.
Expressions as Drivers: to have an expression re-evaluated after entry, Blender uses Drivers (a feature of the animation system). Expressions beginning with # are special: rather than evaluating the value and discarding the expression, they add a driver to the property carrying that expression. The expression #frame quickly maps a value to the current frame, and more complex ones like #fmod(frame, 24) / 24 also work — a convenient shortcut for adding drivers, which can also be added via the RMB menu.

Units: besides expressions, you can give numbers with units; with no unit, a default unit applies, and the unit system can be changed in the scene settings. Use either the unit abbreviation or the full name after the value. Valid length examples include: 1cm 1m 3mm 1m, 3mm and 2ft 3ft/0.5km 2.2mm + 5' / 3" - 2yards. Note: the decimal separator is optional; you can mix units (e.g. metric and imperial, even though only one shows at a time); and plurals are recognized, so both meter and meters work.

Color Fields: a color field stores a color value, and clicking it with LMB opens the Color Picker. Fields with an alpha channel are split in half — the left shows the color without an alpha channel, the right shows it with alpha over a checker pattern. Drag and drop to copy a color to another color field. Hovering over a color property shows a large swatch preview along with the color's hexadecimal, RGBA, and HSVA values.

[Related references](INDEX.md).
