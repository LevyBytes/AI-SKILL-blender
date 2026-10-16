# bpy.types.Object: closest_point_on_mesh

closest_point_on_mesh ( origin , * , distance = 1.84467e+19 , depsgraph = None ) 

Locate the closest point on the evaluated geometry in object space (pulling the evaluated mesh from the context's or a supplied depsgraph as needed)

Parameters :

- origin (mathutils.Vector) – Point to find closest geometry from (in object space) (array of 3 items, in [-inf, inf])

- distance ( float ) – Maximum distance (in [0, inf], optional)

- depsgraph (Depsgraph) – Depsgraph to use to get evaluated data, when called from original object (only needed if current Context’s depsgraph is not suitable) (optional)

Returns :

result , Whether closest point on geometry was found, bool

location , The location on the object closest to the point, mathutils.Vector

normal , The face normal at the closest point, mathutils.Vector

index , The face index, -1 when original data isn’t available, int

Return type :

tuple[bool, mathutils.Vector, mathutils.Vector, int]

[Related references](INDEX.md).
