# bpy.types.Node: warning_propagation

warning_propagation

Which message kinds get carried up from this node to the enclosing group node (default 'ALL' )

- ALL
All Messages – Propagate every info, error, and warning message upstream.

- `ERRORS_AND_WARNINGS`
Errors and Warnings – Propagate only error and warning messages upstream.

- ERRORS
Errors – Propagate only error messages upstream.

- NONE
None – Do not propagate any messages upstream.

Type :

Literal[‘ALL’, ‘`ERRORS_AND_WARNINGS`’, ‘ERRORS’, ‘NONE’]

[Related references](INDEX.md).
