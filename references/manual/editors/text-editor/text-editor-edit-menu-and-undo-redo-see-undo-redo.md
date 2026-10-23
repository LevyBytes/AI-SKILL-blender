# Text Editor: Edit Menu, Undo/Redo - see Undo & Redo.

Edit Menu:
Undo/Redo: see Undo & Redo.
Cut (Ctrl-X): cuts the marked text to the clipboard.
Copy (Ctrl-C): copies the marked text to the clipboard.
Paste (Ctrl-V): pastes from the clipboard at the cursor.
Duplicate Line (Ctrl-D): duplicates the current line.
Move Line(s) Up (Shift-Ctrl-Up): swaps the current/selected line(s) with those above.
Move Line(s) Down (Shift-Ctrl-Down): swaps the current/selected line(s) with those below.
Find & Replace (Ctrl-F): shows the Find & Replace panel in the Sidebar.
Find & Set Selection (Ctrl-G): finds the next instance of the selected text.
Jump To (Ctrl-J): pops up to let you pick a line number to jump the cursor to.
Text Auto Complete (Tab): shows a selectable list of words already in the text.
Text to 3D Object: converts the text file to a Text Object, either as One Object or One Object Per Line.

Select Menu:
All (Ctrl-A): selects the whole file.
Line (Shift-Ctrl-A): selects the whole current line.
Word (double-click LMB): selects the whole current word.
Top (Shift-Ctrl-Home): selects everything above the cursor.
Bottom (Shift-Ctrl-End): selects everything below the cursor.
Line Begin (Shift-Home): selects from the current line's start to the cursor.
Line End (Shift-End): selects from the cursor to the current line's end.
Previous Line (Shift-Up): selects from the cursor to the matching spot one line up.
Next Line (Shift-Down): selects from the cursor to the matching spot one line down.
Previous Word (Shift-Ctrl-Left): selects from the cursor to the previous word's start; mid-word, to the current word's start.
Next Word (Shift-Ctrl-Right): selects from the cursor to the next word's end; mid-word, to the current word's end.

Format Menu:
Indent (Tab): inserts a tab character at the cursor.
Unindent (Shift-Tab): unindents the selection.
Toggle Comments (Ctrl-Slash): toggles whether the selected line(s) are a Python comment; with nothing selected, it toggles the current line.
Convert Whitespace: converts indentation characters To Spaces or To Tabs.

Template Menu: holds a set of templates for both Python and Open Shading Language scripts.

Main View — typing produces text in the buffer. As usual, press-drag-release LMB selects text and RMB opens the context menu. Tip: the Text editor is also handy for sharing a blend-file — leave a note explaining the file's structure, and keep the editor visible when you save so others spot it.

Sidebar - Find & Replace:
Find Text (Ctrl-F): searches for instances of a text after the cursor; the eyedropper icon searches for the currently selected text and selects the match, and Find Next jumps to the next one.
Replace Text (Ctrl-H): searches for the Find Text and swaps in the new text; the eyedropper icon sets the selected text as the replacement, Replace finds and swaps the next match, and Replace All swaps every occurrence.
Case: makes the search mind upper- and lowercase.
Wrap: restarts the search from the file's start once it reaches the end.
All: searches every text data-block, not just the active one.
Properties:
  Margin: shows a vertical margin line to help keep lines a sensible length; its position is the Margin Column.
  Font Size (Ctrl-WheelUp): the size of the text font.
  Tab Width: how many character spaces a tab is drawn with.
  Indentation: whether indentation uses Tabs or Spaces.

Footer: the Text editor footer says whether the text is saved internally or externally and whether an external file has unsaved changes; for external files it also shows the file path.

Usage - Running Scripts: the standout keystroke is Alt-P, which runs the current text as a Python script. You can reach not just the standard Python modules but a whole set of Blender-specific ones too; see Scripting & Extending Blender.

[Related references](INDEX.md).
