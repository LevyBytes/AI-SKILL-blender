# bpy.types.FunctionNodeBitMath: properties

## FunctionNodeBitMath(FunctionNode)

### FunctionNodeBitMath(FunctionNode) 

base classes: bpy_struct, Node, NodeInternal, FunctionNode
class bpy.types. FunctionNodeBitMath ( FunctionNode ) 

Apply bitwise operations to 32-bit integers
operation 

(default 'AND' )

- AND
And – Returns a value where the bits of A and B are both set.

- OR
Or – Returns a value where the bits of either A or B are set.

- XOR
Exclusive Or – Returns a value where only one bit from A and B is set.

- NOT
Not – Returns the opposite bit value of A, in decimal it is equivalent of A = -A - 1.

- SHIFT
Shift – Shifts the bit values of A by the specified Shift amount. Positive values shift left, negative values shift right..

- ROTATE
Rotate – Rotates the bit values of A by the specified Shift amount. Positive values rotate left, negative values rotate right..

Type :

Literal[‘AND’, ‘OR’, ‘XOR’, ‘NOT’, ‘SHIFT’, ‘ROTATE’]

[Related references](INDEX.md).
