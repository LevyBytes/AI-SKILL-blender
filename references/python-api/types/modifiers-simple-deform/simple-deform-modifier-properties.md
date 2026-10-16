# bpy.types.SimpleDeformModifier: properties

angle

Angle of deformation (in [-inf, inf], default 0.785398)

Type :

float
deform_axis

Deform around local axis (default 'X' )

Type :

Literal[Axis Xyz Items]
deform_method

(default 'TWIST' )

- TWIST
Twist – Spin the geometry about the modifier space's Z axis.

- BEND
Bend – Curve the mesh across the modifier space's Z axis.

- TAPER
Taper – Scale linearly down the modifier space's Z axis.

- STRETCH
Stretch – Elongate the object down the modifier space's Z axis.

Type :

Literal[‘TWIST’, ‘BEND’, ‘TAPER’, ‘STRETCH’]
factor

Amount to deform object (in [-inf, inf], default 0.785398)

Type :

float
invert_vertex_group

Invert vertex group influence (default False)

Type :

bool
limits

Lower/Upper limits for deform (array of 2 items, in [0, 1], default (0.0, 1.0))

Type :

bpy_prop_array[float]
lock_x

Do not allow deformation along the X axis (default False)

Type :

bool
lock_y

Do not allow deformation along the Y axis (default False)

Type :

bool
lock_z

Do not allow deformation along the Z axis (default False)

Type :

bool
origin

Offset the origin and orientation of the deformation

Type :

Object
vertex_group

Vertex group name (default “”, never None)

Type :

str

[Related references](INDEX.md).
