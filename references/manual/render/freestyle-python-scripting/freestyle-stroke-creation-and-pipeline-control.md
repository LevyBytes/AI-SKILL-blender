# Python Scripting: Stroke Creation, User Control on the Pipeline Definition

### Stroke Creation

Operators.create() transforms active Chains into Strokes. It takes two arguments: a unary predicate on Interface1D for final chain selection, and a shader list for stroke rendering.

shaders_list = [
SamplingShader(5.0),
ConstantThicknessShader(2),
ConstantColorShader(0.2,0.2,0.2,1),
]
Operators.create(DensityUP1D(8,0.1, IntegrationType.MEAN), shaders_list)

This removes chains exceeding 0.1 mean density via DensityUP1D. Each chain becomes a stroke resampled every 5 units with 2-unit thickness and dark gray color.

### User Control on the Pipeline Definition

Style module writing permits different control types despite fixed module structure. One method: sequence different pipeline structures. Another: define functors passed throughout.

Different structures combine selection, chaining, splitting, and sorting steps. Stroke creation concludes every module.

Predicates, functions, chaining iterators, and stroke shaders inherit base classes and override methods. Reference manual entries for these base classes provide scriptable construct details.

See also
Predicates, functions, chaining iterators, and stroke shaders inherit base classes and override methods. Consult Freestyle python module for complete user-scriptable construct information.

[Related references](INDEX.md).
