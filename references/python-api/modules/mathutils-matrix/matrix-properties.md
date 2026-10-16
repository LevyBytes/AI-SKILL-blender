# mathutils.Matrix: properties

col

Access the matrix by columns (read-only).

Type :

MatrixAccess
is_frozen

Reads True once the object has been locked (read-only).

Type :

bool
is_identity

True if this is an identity matrix (read-only).

Type :

bool
is_negative

True if this matrix results in a negative scale, 3x3 and 4x4 only, (read-only).

Type :

bool
is_orthogonal

True if this matrix is orthogonal, 3x3 and 4x4 only, (read-only).

Type :

bool
is_orthogonal_axis_vectors

True if this matrix has orthogonal axis vectors, 3x3 and 4x4 only, (read-only).

Type :

bool
is_valid

Reads True while the data's owner remains valid.

Type :

bool
is_wrapped

Reads True when the object is a wrapper around external data (read-only).

Type :

bool
median_scale

The average scale applied to each axis (read-only).

Type :

float
owner

Whatever item this wraps, or None (read-only).

Type :

Any
row

Access the matrix by rows (default), (read-only).

Type :

MatrixAccess
translation

The translation component of the matrix.

Type :

Vector

[Related references](INDEX.md).
