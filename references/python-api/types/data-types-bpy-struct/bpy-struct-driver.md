# bpy.types.bpy_struct: driver_add, driver_remove

driver_add ( path , index = -1 , / )

Attaches one or more drivers to the named property.

Parameters :

- path ( str ) – path to the property to drive, analogous to the fcurve's data path.

- index ( int ) – array index of the property drive. Defaults to -1 for all indices or a single channel if the property is not an array.

Returns :

The driver added or a list of drivers when index is -1.

Return type :

bpy.types.FCurve | list[bpy.types.FCurve]
driver_remove ( path , index = -1 , / )

Detaches one or more drivers from the named property.

Parameters :

- path ( str ) – path to the property to drive, analogous to the fcurve's data path.

- index ( int ) – array index of the property drive. Defaults to -1 for all indices or a single channel if the property is not an array.

Returns :

Success of driver removal.

Return type :

bool

[Related references](INDEX.md).
