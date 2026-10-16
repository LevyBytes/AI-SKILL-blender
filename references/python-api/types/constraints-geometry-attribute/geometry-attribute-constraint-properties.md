# bpy.types.GeometryAttributeConstraint: properties

apply_target_transform

Stack the target object's world transform on top of the transform held by the attribute (default False)

Type :

bool
attribute_name

Which attribute supplies the transform (default "", never None)

Type :

str
data_type

Choose the attribute's data type (default 'VECTOR' )

- VECTOR
Vector – Vector data type, affects position.

- QUATERNION
Quaternion – Quaternion data type, affects rotation.

- FLOAT4X4
4x4 Matrix – 4x4 Matrix data type, affects transform.

Type :

Literal[‘VECTOR’, ‘QUATERNION’, ‘FLOAT4X4’]
domain

Attribute domain (default 'POINT' )

Type :

Literal[‘POINT’, ‘EDGE’, ‘FACE’, ‘`FACE_CORNER`’, ‘CURVE’, ‘INSTANCE’]
mix_loc

Mix Location (default False)

Type :

bool
mix_mode

Choose how the existing and copied transforms get blended (default 'REPLACE' )

- REPLACE
Replace – Substitute the attribute's transform in place of the original one.

- `BEFORE_FULL`
Before Original (Full) – Put the copied transform ahead of the original through plain matrix multiplication, as though the constraint target were a parent under Full Inherit Scale; rotation combined with non-uniform scale can introduce shear.

- `BEFORE_SPLIT`
Before Original (Split Channels) – Put the copied transform ahead of the original, treating location, rotation and scale on their own, much like three Copy constraints in a row.

- `AFTER_FULL`
After Original (Full) – Place the copied transform after the original through plain matrix multiplication, as though the constraint target were a child under Full Inherit Scale; rotation paired with non-uniform scale can introduce shear.

- `AFTER_SPLIT`
After Original (Split Channels) – Place the copied transform after the original, treating location, rotation and scale on their own, much like three Copy constraints in a row.

Type :

Literal[‘REPLACE’, ‘`BEFORE_FULL`’, ‘`BEFORE_SPLIT`’, ‘`AFTER_FULL`’, ‘`AFTER_SPLIT`’]
mix_rot

Mix Rotation (default False)

Type :

bool
mix_scl

Mix Scale (default False)

Type :

bool
sample_index

Sample Index (in [0, inf], default 0)

Type :

int
target

Target geometry object

Type :

Object

[Related references](INDEX.md).
