# bpy.types.PreferencesInput: tablet_api

tablet_api

Pick which tablet API drives pressure sensitivity (may need a Blender restart to apply) (default 'AUTOMATIC' )

- AUTOMATIC
Automatic – Pick Wintab or Windows Ink based on the device on its own.

- `WINDOWS_INK`
Windows Ink – Go through the native Windows Ink API, suited to current tablet and pen devices. Needs Windows 8 or later..

- WINTAB
Wintab – Go through the Wintab driver, for older tablets and Windows releases.

Type :

Literal[‘AUTOMATIC’, ‘`WINDOWS_INK`’, ‘WINTAB’]

[Related references](INDEX.md).
