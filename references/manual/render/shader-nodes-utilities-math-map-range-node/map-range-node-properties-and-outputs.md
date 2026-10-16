# Map Range Node: Properties, Outputs, Examples

### Properties

Data Type
Map Range handles both Float and Vector data types. Switching the data type updates the sockets to suit the choice.

Interpolation Type
The mathematical method used to bridge gaps between the numeric inputs.

Linear :

Linear interpolation between From Min and From Max values.

Stepped Linear :

Stepped linear interpolation between From Min and From Max values.

Smooth Step :

Smooth Hermite edge interpolation between From Min and From Max values.

Smoother Step :

Smoother Hermite edge interpolation between From Min and From Max values.

Clamp
Switch it on and the result gets held inside the destination span.

### Outputs

Result/Vector
What the input becomes once remapped.

### Examples

The Noise Texture node emits a value across [0, 1]. Map Range can shift that onto the range [-1, 1].

Example of Map Range node.

[Related references](INDEX.md).
