# Crashes

## Crashes

### Crashes

Common Blender crash sources:

- Memory depletion.

- GPU or driver complications.

- Blender defects.

Auto Save might recover work first.

Repeated issues may resolve via updating GPU drivers
(see Troubleshooting Graphics Hardware), upgrading RAM or GPU, and deactivating demanding settings:

- Reduce undo count Preferences ‣ System ‣ Memory & Limits ‣ Undo Steps .

- Multisample anti-aliasing heightens memory needs and slows performance.

- Linux window managers (KDE, Gnome) often employ graphics acceleration (window decoration, translucency) competing for Blender resources. Disabling effects or lightweight managers help.

Check Blender consumption:

- Windows: Task Manager, ordered by Memory.

- macOS: Activity Monitor.app Memory panel. Or run top -o MEM .

- Linux: run top -o %MEM .

Worst cases warrant reinstalling OS. Windows accumulates latent trouble from patches and remnants.

### Crash Log

Crashes produce logs (text format) with clues.
Usually written to Temporary Directory.

Contents detail tool activity pre-crash plus debugging data. Attaching these helps bug reports, particularly when others lack reproduction.

### Windows

Crashes write files named post blend-file; test.blend makes test.crash.txt .

Batch scripts in Blender folder extract logs:

- blender_debug_log.cmd covers most scenarios.

- blender_debug_gpu.cmd and blender_debug_gpu_workaround.cmd capture GPU data.

- blender_factory_startup.cmd begins with defaults, suggested for debugging.

Module crashes append to blender.crash.txt .
Read blender_debug_out.txt end for location.

### macOS

Post-crash, macOS Crash Reporter displays backtrace afterward, or on restart. Save the display content. Attach to bug reports following guidelines.

~/Library/Logs/DiagnosticReports/ holds .crash entries formatted:
Blender_YYYY-MM-DD-`HHMMSS_MACNAME`.crash . Matching reports offer hints. Alternatively, Console.app explores all "User Reports"
(app sidebar).

### Linux

/tmp receives blender.crash.txt post-crash.

Note

Command Line execution with --factory-startup --debug-all yields extra data.
See Launching from the Command Line and Command Line Arguments.

### Attaching to a Bug Report

Include crash logs when Reporting a Bug.

[Related references](INDEX.md).
