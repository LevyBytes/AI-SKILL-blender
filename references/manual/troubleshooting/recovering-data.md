# Recovering Data

## Recovering Data

### Recovering Data

Unexpected shutdowns, power failures, or neglecting to save your project can lead to lost or corrupted content. Blender's Auto Save feature reduces the chance of losing work in such situations.

Three features help prevent accidental loss:

- Save Prompt shows a confirmation when exiting with unsaved modifications

- Save Versions stores backup copies with sequential numbering

- Auto Save creates periodic snapshots at set intervals (default: every 2 minutes)

Note

For undoing actions during normal work, see Undo , Redo and Undo History to roll back changes or jump to a prior state. See Undo & Redo.

### Recovering Save Versions

By default Blender maintains one backup whenever you save.
Instead of overwriting the old file, Blender renames it with a .blend1 suffix.

This copy lets you revert to an older version.

Check Save Versions to adjust how many backups are retained.

### Recovering The Last Session

Reference

Menu :

File ‣ Recover ‣ Last Session

Recover Last Session opens the quit.blend file stored in the Temporary Directory when Blender closes normally (see Blender Session). Keep in mind files in your temp folder may be removed when you restart your computer or when maintenance scripts run, depending on your setup.

### Recovering an Auto Save

Blender continuously saves automatic backups while you work.
If Blender crashes or closes unexpectedly, the autosave may contain recoverable work.

Follow these instructions to restore from autosave:

- Start Blender.

- Click the top-left menu: File –> Recover –> Auto Save.

- Browse the file dialog that opens to locate the backup you want.
Files follow the naming pattern: &lt;filename&gt;_autosave.blend
Note these files include timestamps to help you identify the right one.

- Pick the desired file and press Open.

- Once loaded, use Save As right away to preserve it separately from the autosave.

Tip

Enable detailed list mode when browsing autosaves to identify the most recent version.

File Browser showing a vertical list.

See also

Auto Save Interval Preference

[Related references](INDEX.md).
