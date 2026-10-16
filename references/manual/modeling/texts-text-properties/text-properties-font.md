# Text Properties: Font

### Font

Reference

Mode :

All Modes

Panel :

Properties ‣ Data ‣ Font

By default Blender ships with a built-in font that turns up in
each of the four font-style data-block menus.
Always available, this built-in font appears in the list as "Bfont".
The data-block menu itself lists whatever fonts are currently loaded.
Pick one per font style.

To swap in a different Font , press a Load button
over in the Font panel, then browse your way to a font file.
In the File Browser every valid font gets a capital "F" icon.

Pick a font Blender can't handle and you'll see the error Not a valid font .

Note

Location of Fonts on Unix

You'll usually find fonts under /usr/lib/fonts , or a variant such as /usr/lib/X11/fonts ,
though not always. Other spots are possible too,
like /usr/share/local or /usr/local/share , along with related sub-trees.

Keep in mind that one font covers every character of the same style in a text,
yet each style needs its own font.
To italicize characters or words, for example, you'll have to load an Italics font.
With the font loaded, you then apply that font "Style" to the selected characters or to the whole object.
All told, representing every style means loading at least four different fonts
(Normal, Italics, Bold, Bold & Italics).

It's worth grasping that Blender doesn't mind which font
you assign to "normal", "bold", and so on.
That's how a single text can run as many as four different fonts at once,
though you do have to settle on either different styles of one font or different fonts.
Blender's typographic controls for adjusting the style and layout of text
sit in the Font panel.

Bold
With nothing selected, switches whether freshly typed text comes out bold .
With text selected, switches the selected text between bold and not.

You can also flip Bold on or off straight from the 3D Viewport via Toggle Bold.

Italic
With nothing selected, switches whether freshly typed text comes out italic .
With text selected, switches the selected text between italic and not.

Flipping Italic is likewise available in the 3D Viewport through Toggle Italic.

Underline
With nothing selected, switches whether freshly typed text comes out underlined.
With text selected, switches the selected text between underlined and not.

Underline can be flipped from the 3D Viewport as well, using Toggle Underline.

See also underline settings below.

Small Caps
With nothing selected, switches whether freshly typed text comes out in small capitals.
With text selected, switches the selected text into small capitals or back.

The 3D Viewport offers a Toggle Small Caps for flipping Small Caps too.

You can also drop text into small caps by selecting it and reaching for Toggle Small Caps.

How large the Small Caps end up is governed by Small Caps Scale.

[Related references](INDEX.md).
