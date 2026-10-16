# Deform Curves on Surface Node

## Deform Curves on Surface Node

The Deform Curves on Surface node shifts and rotates each curve based on its root position change. The root is stored as UV coordinates on the curve and the selected UV Map in the Curves surface settings.

Transformation is calculated from the difference between the original (undeformed) and final (modified) mesh.

This node has implicit inputs beyond the standard one:

- Original and evaluated mesh are pulled from the modifier's surface property, so this works only on curves objects.
- Original and evaluated UV maps come from the object's surface property.
- The rest_position attribute (3D vector) computes rotation tangents matching the original mesh.
- The surface_uv_coordinate attribute (2D vector, curve domain) stores root locations on the surface UV map.

Future updates will make this more flexible.

Parts parallel the Sample UV Surface Node logic.

Warning: After Subdivision Surface, set UV Smooth to None to keep UV attachment points stable.

Curves: Standard input.

Curves: Standard output.

[Related references](INDEX.md).
