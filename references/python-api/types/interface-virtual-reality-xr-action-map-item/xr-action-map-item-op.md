# bpy.types.XrActionMapItem: op, op_mode, op_name, op_properties

op 

Identifier of the operator invoked on an action event (default “”, never None)

Type :

str
op_mode 

When the operator runs (default 'PRESS' )

- PRESS
Press – Execute operator on button press (non-modal operators only).

- RELEASE
Release – Execute operator on button release (non-modal operators only).

- MODAL
Modal – Use modal execution (modal operators only).

Type :

Literal[‘PRESS’, ‘RELEASE’, ‘MODAL’]
op_name 

Translated name of the operator invoked on an action event (default “”, readonly, never None)

Type :

str
op_properties 

Property values passed to the operator when it runs (readonly)

Type :

OperatorProperties

[Related references](INDEX.md).
