# bpy.types.BlendDataLibraries: remove

remove ( library , * , do_unlink = True , do_id_user = True , do_ui_user = True ) 

Disconnect a library from the current file

Parameters :

- library (Library) – Library to remove (never None)

- do_unlink ( bool ) – Break all references to this library before deletion (optional)

- do_id_user ( bool ) – Reduce user count for all data-blocks used (optional)

- do_ui_user ( bool ) – Ensure the interface is updated (optional)
remove ( library , * , do_unlink = True , do_id_user = True , do_ui_user = True )
Removes a library from the current blendfile.
Parameters:
- library (Library) – Library to remove (never None)
- do_unlink ( bool ) – Unlink all usages of this library before deleting it (optional)
- do_id_user ( bool ) – Decrement user counter of all data-blocks used by this library (optional)
- do_ui_user ( bool ) – Make sure interface does not reference this library (optional)

[Related references](INDEX.md).
