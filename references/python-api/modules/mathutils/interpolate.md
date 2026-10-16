# mathutils.interpolate

## Interpolation Utilities (mathutils.interpolate)

### Interpolation Utilities (mathutils.interpolate) 

Blender's interpolate module.
mathutils.interpolate. poly_3d_calc ( veclist , pt , / ) 

Work out the barycentric weights of a point lying on a polygon.

Parameters :

- veclist ( Sequence [ Sequence [ float ] ] ) – The polygon's vertices, listed as 3D coordinates.

- pt ( Sequence [ float ] ) – The query point, given in 2D or 3D.

Returns :

One weight returned for each vertex listed in veclist .

Return type :

list[float]

[Related references](INDEX.md).
