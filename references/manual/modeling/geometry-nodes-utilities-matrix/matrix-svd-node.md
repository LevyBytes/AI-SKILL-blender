# Matrix SVD Node

## Matrix SVD Node

### Matrix SVD Node

Singular Value Decomposition of the input matrix (3D component).
Describes the matrix as: M = U * S * transpose(V)

Only the 3x3 affine part is used (translation column omitted).
Non-pure transformations decompose.

U and V are rotations/reflections (±1 scaling).
Positive determinant: pure rotations.
S describes scaling via diagonal vector.

### Inputs

**Matrix**
Matrix to decompose.

### Outputs

**U**
Left transform.

**S**
Singular values.

**V**
Right transform.

[Related references](INDEX.md).
