# bpy.types.Object: crazyspace_eval, crazyspace_displacement_to_deformed, crazyspace_displacement_to_original, crazyspace_eval_clear

crazyspace_eval ( depsgraph , scene ) 

Build the orientation mapping between the vertices of the original object and those of the object once shape keys and deforming modifiers are applied. Release the evaluation afterward with crazyspace_eval_free.

Parameters :

- depsgraph (Depsgraph) – Dependency Graph, Evaluated dependency graph

- scene (Scene) – Scene, Scene of the object
crazyspace_displacement_to_deformed ( * , vertex_index = 0 , displacement = (0.0, 0.0, 0.0) ) 

Map a displacement vector out of non-deformed object space and into deformed object space

Parameters :

- vertex_index ( int ) – vertex_index, (in [-inf, inf], optional)

- displacement (mathutils.Vector) – displacement, (array of 3 items, in [-inf, inf], optional)

Returns :

displacement_deformed, (array of 3 items, in [-inf, inf])

Return type :

mathutils.Vector
crazyspace_displacement_to_original ( * , vertex_index = 0 , displacement = (0.0, 0.0, 0.0) ) 

Discard the crazyspace evaluated state

Parameters :

- vertex_index ( int ) – vertex_index, (in [-inf, inf], optional)

- displacement (mathutils.Vector) – displacement, (array of 3 items, in [-inf, inf], optional)

Returns :

displacement_original, (array of 3 items, in [-inf, inf])

Return type :

mathutils.Vector
crazyspace_eval_clear ( ) 

crazyspace_eval_clear

[Related references](INDEX.md).
