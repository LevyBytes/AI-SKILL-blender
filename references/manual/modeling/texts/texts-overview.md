# Introduction

### Introduction

Text objects hold a string of text and belong to the same family as curve and surface objects, since fonts are vector data — they're built from curves.

To map letter codes onto the geometry that represents them in the 3D Viewport, Blender leans on a "Font System."
That system ships with a font of its own, yet it can also pull in external fonts —
PostScript Type 1 , OpenType and TrueType among them.
On top of that, any object already in the current blend-file can stand in as a letter.

An example of an extruded text.

With text objects you can author and render 2D or 3D text, complete with advanced layout options such as justification and frames.
Out of the gate, letters are nothing more than flat filled surfaces, just like any closed 2D curve.
But, like curves, they can be extruded
and have modifiers applied to them
(to make them follow a curve, for instance).

Blender lets you lay text out in fairly sophisticated ways:
splitting it into columns or blocks, mixing alignments, and the like.

Conceptually those capabilities echo what DTP software
(Scribus, say) offers, even if they're fairly rudimentary at this stage.

Tip

A text object can be converted either to a curve or straight to a mesh
via Convert in Object Mode.

Note

Each text object tops out at 50,000 characters. Keep in mind, though,
that the more characters one text object holds,
the more sluggishly it responds as you work with it.

[Related references](INDEX.md).
