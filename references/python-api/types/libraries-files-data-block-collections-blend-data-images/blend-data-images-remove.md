# bpy.types.BlendDataImages: remove

remove ( image , * , do_unlink = True , do_id_user = True , do_ui_user = True ) 

Unload an image from the current file

Parameters :

- image (Image) – Image to remove (never None)

- do_unlink ( bool ) – Break all references to this image before deletion (optional)

- do_id_user ( bool ) – Reduce user count for all data-blocks used (optional)

- do_ui_user ( bool ) – Ensure the interface is updated (optional)

[Related references](INDEX.md).
