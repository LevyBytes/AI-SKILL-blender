# bpy.types.Material: volume_intersection_method

volume_intersection_method

Sets which inner region of the mesh generates the volumetric effect (default 'FAST' )

- FAST
Fast – Each face is considered as a medium interface. Gives correct results for manifold geometry that contains no inner parts..

- ACCURATE
Accurate – Faces are considered as medium interface only when they have different consecutive facing. Gives correct results as long as the max ray depth is not exceeded. Have significant memory overhead compared to the fast method..

Type :

Literal[‘FAST’, ‘ACCURATE’]

[Related references](INDEX.md).
