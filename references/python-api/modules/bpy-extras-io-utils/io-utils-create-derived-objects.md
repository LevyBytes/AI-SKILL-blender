# bpy_extras.io_utils: bpy_extras.io_utils. create_derived_objects ( depsgraph , objects )

bpy_extras.io_utils. create_derived_objects ( depsgraph , objects ) 

Given a sequence of objects, this returns their instances.

Parameters :

- depsgraph (bpy.types.Depsgraph) – The evaluated depsgraph.

- objects (Sequence[bpy.types.Object]) – A sequence of objects.

Returns :

A dictionary where each key is an object from objects ,
values are lists of (object, matrix) tuples representing instances.

Return type :

dict[bpy.types.Object, list[tuple[bpy.types.Object, mathutils.Matrix]]]

[Related references](INDEX.md).
