# bpy.types.ClothModifier: properties

## ClothModifier(Modifier)

### ClothModifier(Modifier)

base classes — bpy_struct, Modifier
class bpy.types. ClothModifier ( Modifier )

Cloth simulation modifier
collision_settings

(readonly, never None)

Type :

ClothCollisionSettings
hair_grid_max

(array of 3 items, in [-inf, inf], default (0.0, 0.0, 0.0), readonly)

Type :

bpy_prop_array[float]
hair_grid_min

(array of 3 items, in [-inf, inf], default (0.0, 0.0, 0.0), readonly)

Type :

bpy_prop_array[float]
hair_grid_resolution

(array of 3 items, in [-inf, inf], default (0, 0, 0), readonly)

Type :

bpy_prop_array[int]
point_cache

(readonly, never None)

Type :

PointCache
settings

(readonly, never None)

Type :

ClothSettings
solver_result

(readonly)

Type :

ClothSolverResult

[Related references](INDEX.md).
