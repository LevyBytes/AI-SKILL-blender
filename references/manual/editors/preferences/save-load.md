# Save & Load

## Save & Load

Blend Files:
Save – Save Prompt — prompts you to confirm before a blend-file is closed or a new one opened while the current file holds unsaved changes.
Save Versions — how many backup versions are kept when you save newer versions of a file, stored in the same directory with extensions .blend1, .blend2, etc., the number rising with the count you set; older saves carry the higher number. At the default of 2, for instance, you get three versions: *.blend (last saved), *.blend1 (second last), *.blend2 (third last).
Recent Files — how many files appear in File ‣ Open Recent.
Auto Save — turns on Blender's Auto Save, which periodically writes a temporary backup of the current file to the Temporary Directory, useful for recovering after a crash or sudden shutdown.
Timer (Minutes) — the gap, in minutes, between auto-saves; shorter gaps protect better but add disk writes, which can hurt performance on larger files.
File Preview Types — how blend-file previews are made, used both in the File Browser and in the OS file browser. None (no previews), Auto (a screenshot of the active Workspace when there's no camera, or a camera-view preview when there is one), Screenshot (a screenshot of the active Workspace), or Camera View (a Workbench render from the camera's viewpoint).
Default To – Relative Paths — the default for Relative Paths when loading external files like images, sounds, and linked libraries; ignored if a path is already set.
Default To – Compress File — the default for Compress file when saving blend-files.
Default To – Load UI — the default for Load UI when loading blend-files.
Text Files – Tabs as Spaces — pressing Tab in the Text Editor inserts the right number of spaces rather than tab characters.
Auto Run Python Scripts — for security, Python scripts (driver expressions included) don't run by default; if you only load files from trusted sources, letting them run automatically can be handier.
  Excluded Paths — blend-files in these folders never auto-run Python scripts, useful for marking where untrusted files live. See also Python Security.

File Browser:
Show Locations – Recent — hides the File Browser's Recent panel of recently visited folders.
Show Locations – System — hides the System Bookmarks in the File Browser.
Defaults – Filter Files — on, the File Browser's file region shows only suitable files (blend-files when loading a complete Blender setting, say); the file-type selection can be changed in the file region.
Defaults – Show Hidden Files/Data-Blocks — shows files and data-blocks whose names begin with . in File Browsers. Dot-prefixed data-block names are hidden by default so internal or helper data-blocks don't get used by mistake (see Dot-Prefixed Names (Hidden Data)). See also: hidden data-blocks can be shown in Data-Block Menus by enabling Search – Show Hidden.

[Related references](INDEX.md).
