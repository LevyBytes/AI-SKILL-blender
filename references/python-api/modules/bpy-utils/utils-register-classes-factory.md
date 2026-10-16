# bpy.utils: bpy.utils. register_classes_factory ( classes )

bpy.utils. register_classes_factory ( classes ) 

Convenience helper that builds register and unregister functions
which just register and unregister a given sequence of classes.

Parameters :

classes ( Sequence [ type ] ) – Sequence of classes to register and unregister.

Returns :

register and unregister functions.

Return type :

tuple[Callable[[], None], Callable[[], None]]

[Related references](INDEX.md).
