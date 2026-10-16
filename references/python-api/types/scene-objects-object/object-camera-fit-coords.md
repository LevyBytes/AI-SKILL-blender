# bpy.types.Object: camera_fit_coords

camera_fit_coords ( depsgraph , coordinates ) 

Work out where (and, for ortho cameras, at what scale) the object must sit to bring all the supplied coordinates into view

Parameters :

- depsgraph (Depsgraph) – Depsgraph to get evaluated data from

- coordinates ( Sequence [ float ] ) – Coordinates to fit in (array of 1 items, in [-inf, inf], never None)

Returns :

co_return , The location to aim to be able to see all given points, mathutils.Vector

scale_return , The ortho scale to aim to be able to see all given points (if relevant), float

Return type :

tuple[mathutils.Vector, float]

[Related references](INDEX.md).
