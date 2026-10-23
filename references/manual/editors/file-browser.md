# File Browser

## File Browser

The File Browser turns up in every file-related operation, including:
Opening and saving blend-files.
Browsing the contents of other blend-files while appending or linking data-blocks (see Linked Libraries).
Importing from, or exporting to, other file formats.
Updating the locations of media imported earlier (images, videos, fonts…).

Most often you meet it through modal operators — opening or saving a blend-file, say — where it pops up in its own window, waits for your file pick, and closes again. It can also run as an ordinary, always-visible editor; the built-in Video Editing workspace uses it that way, letting you drag media from the browser straight into the 3D Viewport or the Video Sequencer and skip some overhead.

Interface - Main Region: lists files, folders, or blend-file contents, and hovering an item shows a tooltip with extra detail.
Previews: in Thumbnail display mode the File Browser previews many kinds of content: image and video formats, fonts, blend-files, and internal data-blocks. Data-block previews have to be generated first (see Blend-Files Previews).

Directory Region: above the file list sits a textbox with the current folder path plus navigation buttons.
Previous Folder (Backspace, Alt-Left, Mouse4): steps back through navigation history.
Next Folder (Shift-Backspace, Alt-Right, Mouse5): steps forward through navigation history.
Parent Directory (P, Alt-Up): moves up to the parent directory.
Refresh File List (R, NumpadPeriod): refreshes the current folder.
Create New Directory (I): makes a new directory inside the current one.
Directory (Ctrl-L): the current folder path; Tab auto-completes an existing path, and typing a path that doesn't exist prompts you to create it.
Search (Ctrl-F): filters items by name. The * wildcard matches anything, so bl*er catches both blender and blogger; there's always an implicit wildcard at both ends of the search text, so blender also matches test_blender_file.blend. You can also filter by a specific extension here (e.g. .png lists every PNG).
Display Mode: controls how files appear. Vertical List shows files and folders in a vertical list; Horizontal List shows them in a horizontal one; Thumbnails shows previews.

Display Settings:
Size: the thumbnail size.
Recursions: how many directory levels to show at once, flattened. None lists only the current directory's contents; Blend File lists a whole blend-file's contents (available only when linking or appending data-blocks); One Level, Two Levels, and Three Levels list subdirectory contents to one, two, or three levels of recursion.
Hint: flattening several directory levels is handy for, say, seeing your entire texture collection even when you've tidied it into a set of folders to avoid hundreds of files in one place. In the Append/Link case, showing a whole blend-file's contents lets you link several data-block types in one go.
Warning: the more levels shown at once, the longer the listing takes.
Sort By: orders items by one of four methods: Name (alphabetical), Extension (by extension/type), Modified Date (by modification time), or Size (by file size).

Filter Settings: the funnel toggle turns filtering on or off, and the dropdown beside it holds the options.
File Types: filters by category, such as folders, blend-files, images, etc.
Blender IDs: when appending or linking, also filters by data-block category, such as scenes, animations, materials, etc.
Show Hidden (H): reveals hidden files (those starting with a .).

Execution Region: these controls live at the editor's bottom.
File Name: a text field for the file name and extension; it turns red to warn of overwriting an existing file, and Tab auto-completes to names already in the directory.
/ (Increment Number in Filename) — adds or bumps, or removes or lowers, a trailing number in the file name (used, e.g., to keep several versions of a file).
Cancel (Esc): shuts the File Browser and cancels the operation.
Confirm (Return): accepts the current directory and file name; double-clicking a file or data-block in the main region works too.

Quick Access Region: the left-hand region holds a few panels for jumping to certain directories in one click. The System and Recent panels can be hidden via the Save & Load preferences.
Bookmarks: your own list of frequently used folders; the buttons to the right of the list add, remove, or reorder entries.
System: common directories like the home directory on Linux or the "Documents" folder on Windows.
Volumes: drives and network mounts.
Recent: folders you've visited lately; the button to the right reveals Clear Recent Items for wiping the list.

Operator Options Region: the right-hand region shows the calling operator's options. Beyond the common actions below, many import/export add-ons surface their own options here.
Open, Save, Save As Blender File: see Opening & Saving.
Open, Replace, Save As Image: see Supported Graphics Formats.
Link/Append from Library: see Linked libraries.
And the common option: Relative Path — see Relative Paths.

Header Region: the header carries just two menus, one with the standard editor View controls and one listing a few Selecting operators for discoverability. Neither shows when the browser is in a modal window.

Navigating:
Entering a Directory (Return): double-click a directory to go into it.
Parent Directory (P): moves you up one level.

File Drop: you can also drag a file or folder out of your OS file manager and drop it onto Blender's File Browser, which then jumps to that item and selects it.

Selecting:
Select: click LMB to pick a single item; add Ctrl to add or remove it from the selection, or Shift to grab a range.
Dragging: dragging with LMB begins a box selection.
Note: you can always select several entries, with the last-picked one treated as active; if the calling operation wants a single path (the main blend-file Open, say), it takes that active item's path and ignores the rest.

Arrow Keys: you can also select or deselect by "walking" through files with the arrow keys: press an arrow to select the next/previous file and deselect the rest; hold Shift to keep (and extend) the current selection; hold Shift-Ctrl to invert the selection as you pass over it. With nothing selected, arrow navigation grabs the first or last file in the directory, depending on direction.

Editing: the file list's context menu offers these.
External: has the operating system act on the file or directory; the choices below may not all exist on every OS: Open (open the file), Open Folder (open the folder), Edit (edit the file), New (create a new file of this type), Find File (search for files of this type), Show (show this file), Play (play this file), Browse (browse this file), Preview (preview this file), Print (print this file), Install (install this file), Run As User (run as a specific user), Properties (show OS Properties for this item), Find in Folder (search for items in this folder), and Command Prompt Here (open a command prompt here).
Delete (Delete, X): sends the selected files or directories to the OS "trash". On Linux, deleting directories needs KDE or GNOME.
Rename (F2): changes the name of the selected file or directory.

[Related references](INDEX.md).
