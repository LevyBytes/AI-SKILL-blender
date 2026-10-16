# bpy.types.ShaderNodeTexGradient: properties

## ShaderNodeTexGradient(ShaderNode)

### ShaderNodeTexGradient(ShaderNode)

base classes — bpy_struct, Node, NodeInternal, ShaderNode
class bpy.types. ShaderNodeTexGradient ( ShaderNode )

Outputs blended color and intensity values derived from the incoming vector.
color_mapping

Color mapping settings (readonly, never None)

Type :

ColorMapping
gradient_type

Style of the color blending (default 'LINEAR' )

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

Type :

Literal[‘LINEAR’, ‘QUADRATIC’, ‘EASING’, ‘DIAGONAL’, ‘SPHERICAL’, ‘`QUADRATIC_SPHERE`’, ‘RADIAL’]
texture_mapping

Texture coordinate mapping settings (readonly, never None)

Type :

TexMapping

[Related references](INDEX.md).
