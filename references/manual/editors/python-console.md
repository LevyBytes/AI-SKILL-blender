# Python Console

## Python Console

The Python Console is a fast way to try out code snippets and poke around Blender's API. It runs whatever you type at its >>> prompt and offers command history and auto-complete.

Interface — Header Menus — View Menu:
Zoom In / Zoom Out: grows/shrinks the font size.
Move to Previous Word (Ctrl-Left): sends the cursor to the previous word's start; mid-word, to the current word's start.
Move to Next Word (Ctrl-Right): advances the cursor to the next word's end; mid-word, to the current word's end.
Move to Line Begin (Home): moves the cursor to the current line's start. Shift-Home selects from the cursor to the line's start.
Move to Line End (End): moves the cursor to the current line's end. Shift-End selects from the cursor to the line's end.

Console Menu:
Clear All: wipes the console for a fresh view; the command history stays.
Clear Line (Shift-Return): empties the prompt line.
Delete Previous Word (Ctrl-Backspace): deletes from the cursor back to the start of the previous word (split on periods); mid-word, back to the current word's start.
Delete Next Word (Ctrl-Delete): deletes from the cursor to the end of the next word; mid-word, to the current word's end.
Copy as Script (Shift-Ctrl-C): copies the whole history buffer to the clipboard, ready to paste into a text file as a Python script.
Cut (Ctrl-X): copies the selected text to the clipboard and removes it.
Copy (Ctrl-C): copies the selected text to the clipboard.
Paste (Ctrl-V): pastes onto the command line.
Indent (Tab): inserts a tab character at the cursor.
Unindent (Shift-Tab): unindents the selection.
Backward in History (Up): replaces the current command with the previous one from history.
Forward in History (Down): replaces the current command with the next one from history.
Autocomplete (Tab): see Auto Completion.

Main View - Key Bindings:
LMB: moves the cursor along the input line.
Left / Right: moves the cursor one character.
Ctrl-Left / Ctrl-Right: moves the cursor one word.
Shift-Left / Shift-Right: selects characters to the left/right.
Shift-Ctrl-Left / Shift-Ctrl-Right: selects words to the left/right.
Ctrl-A: selects all text and text history.
Backspace / Delete: erase characters.
Ctrl-Backspace / Ctrl-Delete: erase words.
Return: execute command.
Shift-Return: add to command history without executing.

Usage - Aliases: a few variables and modules are provided for convenience:
C: shorthand for bpy.context.
D: shorthand for bpy.data.
bpy: the top-level Blender Python API module.

First Look at the Console Environment: to list the global functions and variables, type dir() and press Return.

Auto Completion: the Console can preview a module's or variable's available members; type bpy. and press Tab, for example. Submodules list in green, and attributes and methods list the same way, methods marked by a trailing (.

Examples:
bpy.context — this module reaches the current scene, the selected objects, the current object mode, and so on. Note: for the commands below to print useful output, have some object(s) selected in the 3D Viewport.
Get the current 3D Viewport mode (Object, Edit, Sculpt, etc.):
```python
bpy.context.mode
```
Get the active object:
```python
bpy.context.object
bpy.context.active_object
```
Change the active object's X coordinate to 1:
```python
bpy.context.object.location.x = 1
```
Move the active object by 0.5 along the X axis:
```python
bpy.context.object.location.x += 0.5
```
Change all three location coordinates in one go:
```python
bpy.context.object.location = (1, 2, 3)
```
Change only the X and Y coordinates:
```python
bpy.context.object.location.xy = (1, 2)
```
Get the selected objects:
```python
bpy.context.selected_objects
```
Get the selected objects excluding the active one:
```text
[obj for obj in bpy.context.selected_objects if obj != bpy.context.object]
```
bpy.data — reaches all the data in the blend-file, whether or not it's active or selected.
bpy.ops — "Operators" are actions usually fired from a button or menu item that can also be called from code; see the bpy.ops API documentation for the full list.

[Related references](INDEX.md).
