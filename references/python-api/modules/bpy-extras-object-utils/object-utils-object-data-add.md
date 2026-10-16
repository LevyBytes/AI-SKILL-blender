# bpy_extras.object_utils: bpy_extras.object_utils. object_data_add ( context , obdata , operator = None , name = None )

bpy_extras.object_utils. object_data_add ( context , obdata , operator = None , name = None ) 

Create an object, using the view context and preferences to set its initial
location, rotation and layer.

Parameters :

- context (bpy.types.Context) – The context to use.

- obdata (bpy.types.ID | None) – Valid object data to be used for the new object or None.

- operator (bpy.types.Operator | None) – The operator, checked for location and rotation properties.

- name ( str | None ) – Optional name

Returns :

the newly created object in the scene.

Return type :

[Related references](INDEX.md).
