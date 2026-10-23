# bpy.types.Space: properties

## Space(bpy_struct)

### Space(bpy_struct)

base class: bpy_struct

subclasses —
SpaceClipEditor, SpaceConsole, SpaceDopeSheetEditor, SpaceFileBrowser, SpaceGraphEditor, SpaceImageEditor, SpaceInfo, SpaceNLA, SpaceNodeEditor, SpaceOutliner, SpacePreferences, SpaceProperties, SpaceSequenceEditor, SpaceSpreadsheet, SpaceTextEditor, SpaceView3D
class bpy.types. Space ( bpy_struct )

The space data attached to a screen area
show_locked_time

Keep the visible timeline range in sync with other time-based editors (default False)

Type :

bool
show_region_header

(default False)

Type :

bool
type

Which space data type this is (default 'EMPTY' , readonly)

Type :

Literal[Space Type Items]

[Related references](INDEX.md).
