# bpy.types.Object: ray_cast

ray_cast ( origin , direction , * , distance = 1.70141e+38 , depsgraph = None ) 

Shoot a ray against the evaluated geometry in object space (pulling the evaluated mesh from the context's or a supplied depsgraph as needed)

Parameters :

- origin (mathutils.Vector) – Origin of the ray, in object space (array of 3 items, in [-inf, inf])

- direction (mathutils.Vector) – Direction of the ray, in object space (array of 3 items, in [-inf, inf])

- distance ( float ) – Maximum distance (in [0, inf], optional)

- depsgraph (Depsgraph) – Depsgraph to use to get evaluated data, when called from original object (only needed if current Context’s depsgraph is not suitable) (optional)

Returns :

result , Whether the ray successfully hit the geometry, bool

location , The hit location of this ray cast, mathutils.Vector

normal , The face normal at the ray cast hit location, mathutils.Vector

index , The face index, -1 when original data isn’t available, int

Return type :

tuple[bool, mathutils.Vector, mathutils.Vector, int]

[Related references](INDEX.md).
