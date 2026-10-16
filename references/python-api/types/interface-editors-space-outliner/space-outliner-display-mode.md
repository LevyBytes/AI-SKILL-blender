# bpy.types.SpaceOutliner: display_mode

display_mode

Which kind of information is shown (default 'SCENES' )

- SCENES
Scenes – Display scenes and their view layers, collections and objects.

- `VIEW_LAYER`
View Layer – Display collections and objects in the view layer.

- SEQUENCE
Video Sequencer – Display data belonging to the Video Sequencer.

- LIBRARIES
Blender File – Display data of current file and linked libraries.

- `DATA_API`
Data API – Display low level Blender data and its properties.

- `LIBRARY_OVERRIDES`
Library Overrides – Display data-blocks with library overrides and list their overridden properties.

- `ORPHAN_DATA`
Unused Data – Display data that is unused and/or will be lost when the file is reloaded.

Type :

Literal[‘SCENES’, ‘`VIEW_LAYER`’, ‘SEQUENCE’, ‘LIBRARIES’, ‘`DATA_API`’, ‘`LIBRARY_OVERRIDES`’, ‘`ORPHAN_DATA`’]

[Related references](INDEX.md).
