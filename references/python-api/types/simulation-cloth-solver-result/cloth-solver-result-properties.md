# bpy.types.ClothSolverResult: properties

## ClothSolverResult(bpy_struct)

### ClothSolverResult(bpy_struct)

base class: bpy_struct
class bpy.types. ClothSolverResult ( bpy_struct )

Cloth solver iteration outcome
avg_error

Average divergence over substeps (in [-inf, inf], default 0.0, readonly)

Type :

float
avg_iterations

Mean iteration count across substeps (in [-inf, inf], default 0.0, readonly)

Type :

float
max_error

Highest divergence in substeps (in [-inf, inf], default 0.0, readonly)

Type :

float
max_iterations

Highest iteration count in substeps (in [-inf, inf], default 0, readonly)

Type :

int
min_error

Lowest divergence in substeps (in [-inf, inf], default 0.0, readonly)

Type :

float
min_iterations

Lowest iteration count in substeps (in [-inf, inf], default 0, readonly)

Type :

int
status

Solver outcome flag (default set(), readonly)

- SUCCESS
Success – Computation was successful.

- `NUMERICAL_ISSUE`
Numerical Issue – The provided data did not satisfy the prerequisites.

- `NO_CONVERGENCE`
No Convergence – Iterative procedure did not converge.

- `INVALID_INPUT`
Invalid Input – The inputs are invalid, or the algorithm has been improperly called.

Type :

set[Literal['SUCCESS', '`NUMERICAL_ISSUE`', '`NO_CONVERGENCE`', '`INVALID_INPUT`']]

[Related references](INDEX.md).
