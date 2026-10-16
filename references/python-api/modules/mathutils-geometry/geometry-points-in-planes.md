# mathutils.geometry: mathutils.geometry. points_in_planes ( planes , epsilon_coplanar = 1e-4 , epsilon_isect = 1e-6 , / )

mathutils.geometry. points_in_planes ( planes , epsilon_coplanar = 1e-4 , epsilon_isect = 1e-6 , / )

Hands back a list of points lying inside every supplied plane, plus a list of the indices of the planes that were used.

Parameters :

- planes (list[mathutils.Vector]) – List of planes (4D vectors).

- epsilon_coplanar ( float ) – Epsilon value for interpreting plane pairs as co-planar.

- epsilon_isect ( float ) – Epsilon value for intersection.

Returns :

Two lists, one containing the 3D coordinates inside the planes, another containing the plane indices used.

Return type :

tuple[list[mathutils.Vector], list[int]]

[Related references](INDEX.md).
