# bpy.types.Scene: ray_cast

ray_cast ( depsgraph , origin , direction , * , distance = 1.70141e+38 )

Fire a ray at the evaluated geometry in world space

Parameters :

- depsgraph (Depsgraph) – The current dependency graph (never None)

- origin (mathutils.Vector) – (array of 3 items, in [-inf, inf])

- direction (mathutils.Vector) – (array of 3 items, in [-inf, inf])

- distance ( float ) – Maximum distance (in [0, inf], optional)

Returns :

result , bool

location , The hit location of this ray cast, mathutils.Vector

normal , The face normal at the ray cast hit location, mathutils.Vector

index , The face index, -1 when original data isn’t available, int

object , The original (un-evaluated) object that was hit. Note that location , normal , and index correspond to the evaluated object’s mesh., Object

matrix , Matrix, mathutils.Matrix

Return type :

tuple[bool, mathutils.Vector, mathutils.Vector, int, Object, mathutils.Matrix]

[Related references](INDEX.md).
