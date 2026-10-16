# bpy.types.UILayout: template_preview ( id , * , show_buttons = True , parent = None , slot = None , preview_id = '' )

template_preview ( id , * , show_buttons = True , parent = None , slot = None , preview_id = '' )

Item. A preview pane for previewing materials, textures, lights or worlds.

Parameters :

- id (ID) – ID data-block

- show_buttons ( bool ) – Show preview buttons? (optional)

- parent (ID) – ID data-block (optional)

- slot (TextureSlot) – Texture slot (optional)

- preview_id ( str ) – Identifier of this preview widget, if not set the ID type will be used (i.e. all previews of materials without explicit ID will have the same size…). (optional, never None)

[Related references](INDEX.md).
