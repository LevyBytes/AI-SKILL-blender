# Opening & Saving

## Opening & Saving

Opening and saving blend-files is normally handled through the File Browser. Tip: you can also open a blend-file by dragging and dropping it into the Blender window, which lets you link/append it too. Note — Unsaved Changes: by default, if you have unsaved changes when quitting Blender or loading another blend-file, a pop-up asks you to either discard them or save; you can switch this off with the Save Prompt option in the Preferences' Save & Load section.

Opening Files — Reference: Menu: File ‣ Open…; Shortcut: Ctrl-O. The upper text field shows the current directory path and the lower one holds the chosen filename.
Options:
Load UI — when on, the screen layout stored inside each blend-file is used, replacing your current layout and Workspaces; off, the file's layout is ignored. Tip: to work on a file with your own defaults, launch a fresh Blender, open the File Browser, turn Load UI off, and open the file.
Trusted Source — when on, any Python scripts and drivers the file may carry run automatically; turn it on only if you made the file yourself or trust whoever gave it to you not to have slipped in malicious code. See Python Security to set default trust options.

Open Recent — Reference: Menu: File ‣ Open Recent; Shortcut: Shift-Ctrl-O. Shows a list of recently opened blend-files; hovering an item previews it and shows its info, and clicking a name opens that file. RMB on a listed item opens a context menu whose options include Open File Location, which reveals that spot in your OS file explorer or Finder.
Clear Recent Files List — drops items from the recent list.
Remove — which items to drop. All Items (every recent file) or Items Not Found (files that can't be located, i.e. moved or deleted).

Recover — Last Session — Reference: Menu: File ‣ Recover ‣ Last Session. Loads the quit.blend file Blender auto-saved just before quitting, so you can recover your last session if you closed Blender by accident.
Auto Save — Reference: Menu: File ‣ Recover ‣ Auto Save. Recovers the most recent auto-saved version of your file, handy after a crash or quitting without saving. It opens a file browser pointed at your system's Temporary Directory; auto-saved files are usually named like &lt;filename&gt;_autosave.blend or a random identifier and use the .blend extension. Set how often and how autosave runs in the Auto Save Preferences. Warning: auto save has limits — notably it won't save changes in Sculpt, Texture Paint, or Edit mode. Important: only one auto-saved file is kept per project, recovering from one loses any changes made since the last save, and older auto saves aren't retained.

Saving Files — Reference: Menu: File ‣ Save; Shortcut: Ctrl-S. Saves the current blend-file over itself (if it was never saved, this switches to Save As… automatically).

Save Incremental — Reference: Menu: File ‣ Save Incremental; Shortcut: Ctrl-Alt-S. Saves the current file under a numerically bumped name that won't overwrite any existing file.

Save As — Reference: Menu: File ‣ Save As…; Shortcut: Shift-Ctrl-S. Pick where on disk to write the blend-file. Warning: if a file of that name already exists, the text field turns red to warn you it'll be overwritten. Tip: use the plus/minus buttons beside the file name, or NumpadPlus / NumpadMinus, to raise or lower a number at the end of the name (e.g. file_01.blend to file_02.blend).
Options:
Compress — shrinks the resulting blend-file but takes longer to save and load; useful for distributing files online and saving drive space on big projects, though it can cause slowdowns when quitting Blender or auto-saving backups. See Compression & Memory Use. Hint: the algorithm is Zstandard, which isn't Blender-specific, so files can be compressed/decompressed with outside tools. Changed in version 3.0: earlier versions used Gzip, so to open newer blend-files in versions before 3.0 you must first save them uncompressed in a newer Blender or decompress them with an external Zstandard tool.
Remap Relative — remaps Relative Paths (such as linked libraries and images) when you save a file to a new location.
Save Copy — saves a copy of the current working state without making the saved file active.

Save Copy — Reference: Menu: File ‣ Save Copy…. Choose a destination path for the blend-file, then go back to editing the original; handy for stashing backups of the working state without touching the original. For options see Save As.

Relative Paths — plenty of blend-files point to external images or other linked blend-files, and a path tells Blender where to find them; move those external files and the referencing blend-file no longer looks right. When you specify such a file, the default is to make the path relative: Blender keeps a partial path measured from the referencing blend-file's own directory, which helps when you reorganize folders or move your files.

With a relative path you can move the blend-file somewhere new as long as the linked files travel with it — you could, for instance, send someone a folder holding a blend-file plus a subfolder of the external images it references.

Where relative paths are supported, the File Browser shows a Relative Path checkbox; when typing a path into a text field, prefix it with a double slash (//) to make it relative. Relative paths are the default, but you can change that in the Preferences' File tab.

Note: you can't use relative paths in a brand-new untitled blend-file — save the file first, before you link to anything external.

Hint: if you must move a blend-file while keeping it positioned relative to its linked resources, turn to Blender's File Save As, which offers a Remap Relative option for the file links.

[Related references](INDEX.md).
