# Text Properties: Transform, Paragraph

### Transform

Size
Drives the size of the text as a whole (there's no sizing each character on its own).
Note, though, that characters in different fonts (different styles, see below) may turn up at different sizes.

Shear
Drives how far the whole text leans over.
Close as it looks, this isn't the same as the italics style.

Shear example.

Object Font
Lets you press your own objects into service as the font, so you can build a complex custom font right inside Blender!
Here you enter the prefix name (the object "family") used
to find the individual characters used for typing.
It's a fairly involved process, so here's a step-by-step:

- Build the font characters; each one can be any object type (mesh, curve, etc.).
Every name has to follow the schema:
"common prefix" then the "character name" (e.g. "ft.a", "ft.b", etc.).

- On the text object, switch on
Instancing Vertices.

- Over in the Font tab, set the Object Font field to the "common prefix" of your "font" objects.
From then on, whenever a character in your text matches the suffix of a "font" object's name,
that object gets duplicated onto the character.

Note

Each duplicate is placed with its center sitting at
the lower right corner of the matching character.

Text on Curve
Hand the text object a curve object to ride along.

Text on curve.

Tip

You're better off with the Curve modifier,
which gives you more control and is the usual way to pull off such effects in modern Blender.

Underline Position
Lets you nudge the underline up or down.

Underline Thickness
Governs how thick the underline comes out.

Small Caps Scale
By how much uppercase letters shrink once small caps is switched on.

### Paragraph

Reference

Mode :

All

Panel :

Properties ‣ Data ‣ Paragraph

Alignment and spacing of the text are controlled from the Paragraph Panel.

The Paragraph panel.

[Related references](INDEX.md).
