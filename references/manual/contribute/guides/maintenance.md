# Maintenance

## Maintenance

Adding, removing, or moving files: when RST files are added or removed, the update script adds or removes the matching locale files automatically. To move files, however, use this Python script first:
```console
python tools/utils_maintenance/rst_remap.py start
```
You can then move the RST files freely, and the remap script relocates the locale file afterward:
```console
python tools/utils_maintenance/rst_remap.py finish
```
Avoid moving or renaming files where possible, since it breaks URLs and, without this script, translators lose all their work in those files — ask an administrator if you think something should be renamed or moved. (The script also handles image file names.) Release checklist: create a release branch (blender-3.2-release/); update the splash image, interface_splash_current.png, in the release branch; and bump the conf.py blender_version variable in the trunk version.

[Related references](INDEX.md).
