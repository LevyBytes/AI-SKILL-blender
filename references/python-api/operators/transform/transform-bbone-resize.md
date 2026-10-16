# bpy.ops.transform.bbone_resize

bpy.ops.transform. bbone_resize ( * , value = (1.0, 1.0, 1.0) , orient_type = 'GLOBAL' , orient_matrix = ((0.0, 0.0, 0.0), (0.0, 0.0, 0.0), (0.0, 0.0, 0.0)) , orient_matrix_type = 'GLOBAL' , constraint_axis = (False, False, False) , mirror = False , release_confirm = False , use_accurate = False )

Modify the visual dimensions of chosen bendy bones

Parameters :

- value (mathutils.Vector) – Display Size, (array of 3 items, in [-inf, inf], optional)

- orient_type ( str ) – Orientation, Transformation orientation (optional)

- orient_matrix (mathutils.Matrix) – Matrix, (multi-dimensional array of 3 * 3 items, in [-inf, inf], optional)

- orient_matrix_type ( str ) – Matrix Orientation, (optional)

- constraint_axis ( Sequence [ bool ] ) – Constraint Axis, (array of 3 items, optional)

- mirror ( bool ) – Mirror Editing, (optional)

- release_confirm ( bool ) – Confirm on Release, Always confirm operation when releasing button (optional)

- use_accurate ( bool ) – Accurate, Use accurate transformation (optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
