# bpy.types.BlendDataObjects: remove

remove ( object , * , do_unlink = True , do_id_user = True , do_ui_user = True )
Removes an object from the current blendfile.
Parameters:
- object (Object) – Object to remove (never None)
- do_unlink ( bool ) – Unlink all usages of this object before deleting it (optional)
- do_id_user ( bool ) – Decrement user counter of all data-blocks used by this object (optional)
- do_ui_user ( bool ) – Make sure interface does not reference this object (optional)
remove ( object , * , do_unlink = True , do_id_user = True , do_ui_user = True ) 

Erase a scene element from the current file

Parameters :

- object (Object) – Object to remove (never None)

- do_unlink ( bool ) – Break all references to this object before deletion (optional)

- do_id_user ( bool ) – Reduce user count for all data-blocks used (optional)

- do_ui_user ( bool ) – Ensure the interface is updated (optional)

[Related references](INDEX.md).
