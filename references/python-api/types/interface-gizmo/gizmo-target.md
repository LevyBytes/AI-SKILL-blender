# bpy.types.Gizmo: target_set_prop, target_set_operator, target_is_valid, target_get_range, target_get_value, target_set_handler, target_set_value

target_set_prop ( target , data , property , * , index = -1 )

Parameters :

- target ( str ) – Target property (never None)

- data (AnyType) – The source the property is read from (never None)

- property ( str ) – Identifier of property in data (never None)

- index ( int ) – (in [-1, inf], optional)
target_set_operator ( operator , * , index = 0 )

The operator fired when the gizmo activates; this takes priority over any property targets.

Parameters :

- operator ( str ) – Target operator (never None)

- index ( int ) – Part index, (in [0, 255], optional)

Returns :

Operator properties to fill in

Return type :

OperatorProperties
target_is_valid ( property )

Parameters :

property ( str ) – Property identifier (never None)

Return type :

bool
target_get_range ( target )

Reads back the allowed range for the given target property.

Parameters :

target – Target property name.

Returns :

A (min, max) pair giving the property’s range.

Return type :

tuple[float, float]
target_get_value ( target )

Reads back the current value held by the given target property.

Parameters :

target ( str ) – Target property name.

Returns :

Depending on the target type, either a single value or an array holding the property’s value.

Return type :

float | tuple[float, …]
target_set_handler ( target , get , set , range = None )

Wires up callback functions for one of a gizmo’s properties.

Parameters :

- target ( str ) – Target property name.

- get ( Callable [ [ ] , float | Sequence [ float ] ] ) – Callback yielding this property’s value, as either one number or a sequence.

- set ( Callable [ [ tuple [ float , ... ] ] , Any ] ) – Callback receiving one value argument and writing it back.

- range ( Callable [ [ ] , tuple [ float , float ] ] | None ) – Callback yielding a (min, max) pair for range-based gizmos; whatever it returns is ignored.
target_set_value ( target )

Writes a new value into the given target property.

Parameters :

target ( str ) – Target property name.

[Related references](INDEX.md).
