# Editing Images

## Editing Images

New — Reference: Mode: All Modes; Menu: Image ‣ New; Shortcut: Alt-N. Makes a new Generated Image.

Open — Reference: Mode: All Modes; Menu: Image ‣ Open; Shortcut: Alt-O. Opens a file browser to load an image into the editor; you can also drag and drop images straight in. On open, these options appear:
Relative Path — makes the file path relative to the open blend-file (see Relative Paths).
Detect Sequences — auto-hunts for image sequences in the chosen images (by file name); switch it off when you really do want single images that belong to a sequence (see Opening an Image Sequence).
Detect UDIMs — auto-hunts for UDIM tiles in the chosen image's directory and loads any matches as UDIMs; it works by spotting a .xxxx (four-digit number) before the file extension.

Open Cached Render — Reference: Mode: All Modes; Menu: Image ‣ Open Cached Render; Shortcut: Ctrl-R. Finds the current scene's render cache file and loads it into the Render Result, so you can restore the last render from a previous Blender session and keep working in the Compositor without re-rendering. Note that Blender doesn't write these cache files by default — you must turn on Cache Result in the scene's Output options and render at least once.

Replace — Reference: Mode: All Modes; Menu: Image ‣ Replace. Swaps the current image for another.

Reload — Reference: Mode: All Modes; Menu: Image ‣ Reload; Shortcut: Alt-R. Reloads the image from the file on drive.

Edit Externally — Reference: Mode: All Modes; Menu: Image ‣ Edit Externally. Opens the image in the Image Editor program named in the File Paths Preferences.

Copy/Paste — Reference: Mode: All Modes; Menu: Image ‣ Copy/Paste. Copies and pastes images between Blender and the OS clipboard. Only PNG files support direct clipboard copy/paste. Platform notes: Windows can paste images by copying the image's file path, which allows every supported format; Linux needs Wayland for clipboard image support.

Save — Reference: Mode: All Modes; Menu: Image ‣ Save; Shortcut: Alt-S. Saves the image to its current path. Important: animation renders save automatically, but still renders don't — save those by hand.

Save As — Reference: Mode: All Modes; Menu: Image ‣ Save As; Shortcut: Shift-Alt-S. Saves the image to a separate file of any type; the output settings match the Render Output Properties.

Save a Copy — Reference: Mode: All Modes; Menu: Image ‣ Save a Copy. Saves under a chosen name while keeping the original open in the Image editor.

Save All Images — Reference: Mode: All Modes; Menu: Image ‣ Save All Images. Saves every modified image; packed images get repacked.

Invert — Reference: Mode: All Modes; Menu: Image ‣ Invert.
Invert Image Colors — inverts the whole image's colors.
Invert Red/Green/Blue/Alpha Channel — inverts a single channel.

Resize — Reference: Mode: All Modes; Menu: Image ‣ Resize. Rescales the image's pixel resolution to change its dimensions, useful for, e.g., dropping texture resolution to save performance and memory, or raising it for more detailed painting/editing.
Size X, Y — the new width and height in pixels.
All UDIM Tiles — applies the resize to every UDIM tile in the image.

Transform:
Flip Horizontally — mirrors the image left-to-right.
Flip Vertically — mirrors the image top-to-bottom.
Rotate 90° Clockwise — turns the image 90° clockwise.
Rotate 90° Counter-Clockwise — turns the image 90° counter-clockwise.
Rotate 180° — turns the image 180°.

Pack — Reference: Mode: All Modes; Menu: Image ‣ Pack. Packs the image into the blend-file (see Packed Data).

Unpack — Reference: Mode: All Modes; Menu: Image ‣ Unpack. Unpacks the image to a drive.

Extract Palette — Reference: Mode: All Modes; Menu: Image ‣ Extract Palette. Pulls a Color Palette out of the image for the painting tools.

[Related references](INDEX.md).
