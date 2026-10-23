# Text Editor: Editor Type - the standard editor-selection button., View Menu

## Text Editor

This editor handles Python scripts, scripting-based shaders like OSL and GLSL, or just plain text notes. Open it by switching to the Scripting workspace or pressing Shift-F11 to replace the current editor.

Header: a freshly opened Text editor is empty with a bare header; more options surface once a text file is created or opened.
Editor Type: the standard editor-selection button.
Menus: the editor's menus.
Resolve Conflict: sorts out modified-file conflicts when an external text file is changed by another program.
Reload from Disk: re-reads the file from drive, discarding local changes.
Make Text Internal: turns the external text data-block into an internal one.
Ignore: hides the warning until the external file is modified externally again.
Text: a data-block menu to choose a text or create a new one; the header then changes.
Run Script (play icon): runs the text as a Python script (Alt-P); see Template Menu.
Show: toggles for line numbers, word wrapping, and syntax highlighting.
Script Node Update (refresh icon): with an OSL file open, refreshes the Shader Script node with the script's new options and sockets.

View Menu:
Sidebar (Ctrl-T): shows or hides the Sidebar.
Line Numbers: shows the file's line numbers at the left of the Main View.
Word Wrap: wraps words too wide for the horizontal space onto a new "pseudo line".
Syntax Highlight: colors the special words of the Python language in the Main View.
Highlight Line: emphasizes the active line by tinting its background.
Zoom In/Out: grows/shrinks the main view's font size.
Navigation:
  Top (Ctrl-Home): moves the view and cursor to the file's start.
  Bottom (Ctrl-End): moves the view and cursor to the file's end.
  Line Begin (Home): moves the cursor to the current line's start.
  Line End (End): moves the cursor to the current line's end.
  Previous Line (Up): moves the cursor to the same spot on the line above.
  Next Line (Down): moves the cursor to the same spot on the line below.
  Previous Word (Ctrl-Left): moves the cursor to the previous word's start; mid-word, to the current word's start.
  Next Word (Ctrl-Right): moves the cursor to the next word's end; mid-word, to the current word's end.

Text Menu:
New (Alt-N): creates a new text Data Block.
Open (Alt-O): loads an external text file chosen via the File Browser.
Reload (Alt-R): reopens the current buffer, losing any unsaved changes.
Edit Externally: edits the text file in an external editor, configurable in the User Preferences.
Save (Alt-S): saves an already-open file.
Save As (Shift-Ctrl-Alt-S): saves the text as a new file; a File Browser opens to pick the directory, name, and extension.
Register: runs the text data-block as a Python script when the blend-file loads; see the API documentation on registering Python modules.
Live Edit: runs the Python script after every change you make.
Run Script (Alt-P): runs the text as a Python script; see Running Scripts.

[Related references](INDEX.md).
