# Vector Math Node: Inputs, Properties

### Vector Math Node

This node evaluates a selected mathematical operation on the input vectors.

### Inputs

Node inputs vary depending on the selected operation; not all appear with every mode. The Scale input, for example, is visible only when the Scale operator is active.

Vector
Input vector \(A = \begin{pmatrix} A_x \\ A_y \\ A_z \end{pmatrix}\).

Vector
Input vector \(B = \begin{pmatrix} B_x \\ B_y \\ B_z \end{pmatrix}\).

Scale
Input Scale \(s\).

### Properties

Operation
The vector math operator to be applied on the input vectors.

Add :

The sum of A and B.
\(\begin{pmatrix} A_x + B_x \\ A_y + B_y \\ A_z + B_z \end{pmatrix}\)

Subtract :

The difference between A and B.
\(\begin{pmatrix} A_x - B_x \\ A_y - B_y \\ A_z - B_z \end{pmatrix}\)

Multiply :

The entrywise product of A and B.
\(\begin{pmatrix} A_x \cdot B_x \\ A_y \cdot B_y \\ A_z \cdot B_z \end{pmatrix}\)

Divide :

The entrywise division of A by B. Division by zero results in zero.
\(\begin{pmatrix} A_x / B_x \\ A_y / B_y \\ A_z / B_z \end{pmatrix}\)

Multiply Add :

The entrywise combination of the multiply and addition operations.
\(A × B + C\)

Cross Product :

The cross product of A and B.
\(\begin{pmatrix} A_y \cdot B_z - A_z \cdot B_y \\ A_z \cdot B_x - A_x \cdot B_z \\ A_x \cdot B_y - A_y \cdot B_x \end{pmatrix}\)

Project :

The projection of A onto B.

Reflect :

The reflection of A around the normal B. B need not be normalized.

Refract :

For a given incident vector A, surface normal B and ratio of indices of refraction (IOR), refract outputs the refraction vector R.

Faceforward :

Orients a vector A to point away from a surface B as defined by its normal C. Computes \((dot(B, C) < 0) ? A : -A\).

Dot Product :

The dot product of A and B.
\(A_x \cdot B_x + A_y \cdot B_y + A_z \cdot B_z\)

Distance :

The distance between A and B.

Length :

The magnitude of A.
\(\sqrt{A_x^2 + A_y^2 + A_z^2}\)

Scale :

The result of multiplying A by the scalar input Scale.
\(\begin{pmatrix} s \cdot A_x \\ s \cdot A_y \\ s \cdot A_z \end{pmatrix}\)

Normalize :

The result of normalizing A. The resulting vector points in the same direction as A with a magnitude of 1. If A is (0, 0, 0), the result is (0, 0, 0).

[Related references](INDEX.md).
