# bpy.types.FunctionNodeAlignEulerToVector: properties

## FunctionNodeAlignEulerToVector(FunctionNode)

### FunctionNodeAlignEulerToVector(FunctionNode) 

base classes — bpy_struct, Node, NodeInternal, FunctionNode
class bpy.types. FunctionNodeAlignEulerToVector ( FunctionNode ) 

Turn an Euler rotation so it points along a supplied direction
axis 

Which axis gets aligned to the vector (default 'X' )

- X
X – Align the X axis with the vector.

- Y
Y – Align the Y axis with the vector.

- Z
Z – Align the Z axis with the vector.

Type :

Literal[‘X’, ‘Y’, ‘Z’]
pivot_axis 

Which axis serves as the pivot for the rotation (default 'AUTO' )

- AUTO
Auto – Automatically detect the best rotation axis to rotate towards the vector.

- X
X – Rotate around the local X axis.

- Y
Y – Rotate around the local Y axis.

- Z
Z – Rotate around the local Z axis.

Type :

Literal[‘AUTO’, ‘X’, ‘Y’, ‘Z’]

[Related references](INDEX.md).
