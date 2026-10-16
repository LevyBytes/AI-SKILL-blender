# bpy.msgbus: methods

### Message Bus (bpy.msgbus)

Allows subscription to property changes within Blender's data-blocks through the RNA change notification system.
bpy.msgbus. clear_by_owner ( owner )

Purge all subscriptions tied to a given owner.

Parameters :

owner ( Any ) – The owner reference supplied to subscribe_rna().
bpy.msgbus. publish_rna ( * , key )

Parameters :

key (bpy.types.Property | bpy.types.Struct | tuple[bpy.types.Struct, str]) – Marks the category of subscribed data

Options are
- A property instance.
- A struct type.
- A tuple of (struct, property name) .

Inform subscribers about updates to this element
(automatic publication typically handles this without explicit calls). In some scenarios, explicit publication using broader keys proves helpful.
bpy.msgbus. subscribe_rna ( * , key , owner , args , notify , options = set() )

Establish a message bus listener. It persists until a new .blend loads or removal via bpy.msgbus.clear_by_owner().

Parameters :

- key (bpy.types.Property | bpy.types.Struct | tuple[bpy.types.Struct, str]) – Marks the category of subscribed data

Options are
- A property instance.
- A struct type.
- A tuple of (struct, property name) .

- owner ( Any ) – Reference for this listener (matches by identity).

- args ( tuple ) – Parameters delivered to the callback.

- notify ( Callable [ ... , None ] ) – The notification handler.

- options ( set [ Literal [ 'PERSISTENT' ] ] ) – Customize listener behavior.

- PERSISTENT when enabled, survives ID data remapping.

Note

All listeners vanish at file-load. Re-register them during post-load events, consult bpy.app.handlers.load_post.

[Related references](INDEX.md).
