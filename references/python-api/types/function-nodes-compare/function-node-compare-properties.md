# bpy.types.FunctionNodeCompare: properties

## FunctionNodeCompare(FunctionNode)

### FunctionNodeCompare(FunctionNode) 

base classes: bpy_struct, Node, NodeInternal, FunctionNode
class bpy.types. FunctionNodeCompare ( FunctionNode ) 

Run a comparison between the two supplied inputs
data_type 

(default 'FLOAT' )

Type :

Literal[Node Socket Data Type Items]
mode 

(default 'ELEMENT' )

- ELEMENT
Element-Wise – Compare each element of the input vectors.

- LENGTH
Length – Compare the length of the input vectors.

- AVERAGE
Average – Compare the average of the input vectors elements.

- `DOT_PRODUCT`
Dot Product – Compare the dot products of the input vectors.

- DIRECTION
Direction – Compare the direction of the input vectors.

Type :

Literal[‘ELEMENT’, ‘LENGTH’, ‘AVERAGE’, ‘`DOT_PRODUCT`’, ‘DIRECTION’]
operation 

(default 'EQUAL' )

Type :

Literal[Node Compare Operation Items]

[Related references](INDEX.md).
