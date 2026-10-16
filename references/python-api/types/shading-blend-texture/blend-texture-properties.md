# bpy.types.BlendTexture: properties

## BlendTexture(Texture)

### BlendTexture(Texture)

base classes — bpy_struct, ID, Texture
class bpy.types.BlendTexture(Texture)

A generated texture that interpolates between colors.
progression

The pattern used when blending between the colors (default 'LINEAR')

- LINEAR
Linear – Create a linear progression.

- QUADRATIC
Quadratic – Create a quadratic progression.

- EASING
Easing – Create a progression easing from one step to the next.

- DIAGONAL
Diagonal – Create a diagonal progression.

- SPHERICAL
Spherical – Create a spherical progression.

- `QUADRATIC_SPHERE`
Quadratic Sphere – Create a quadratic progression in the shape of a sphere.

- RADIAL
Radial – Create a radial progression.

Type:
Literal['LINEAR', 'QUADRATIC', 'EASING', 'DIAGONAL', 'SPHERICAL', '`QUADRATIC_SPHERE`', 'RADIAL']
use_flip_axis

Swap the texture's X and Y axis (default 'HORIZONTAL')

- HORIZONTAL
Horizontal – No flipping.

- VERTICAL
Vertical – Flip the texture's X and Y axis.

Type:
Literal['HORIZONTAL', 'VERTICAL']
users_material

Materials that use this texture

Type:
tuple[Material, …]

Note

Takes O(len(bpy.data.materials) * len(material.texture_slots)) time.

(readonly)
users_object_modifier

Object modifiers that use this texture

Type:
tuple[Object, …]

Note

Takes O(len(bpy.data.objects) * len(obj.modifiers)) time.

(readonly)

[Related references](INDEX.md).
