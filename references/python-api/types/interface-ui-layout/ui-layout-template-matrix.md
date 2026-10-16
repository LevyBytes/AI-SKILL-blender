# bpy.types.UILayout: template_matrix ( data , property )

template_matrix ( data , property )

Adds a read-only matrix display showing the translation, rotation and scale components. Point the property argument at an existing 4x4 float vector property whose subtype is ‘MATRIX’.

Parameters :

- data (AnyType) – Data from which to take property (never None)

- property ( str ) – Identifier of property in data (never None)

[Related references](INDEX.md).
