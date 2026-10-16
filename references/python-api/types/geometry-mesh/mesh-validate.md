# bpy.types.Mesh: validate, validate_material_indices

validate ( * , verbose = False , clean_customdata = True )

Check the geometry; returns True if any invalid geometry on the mesh was fixed up or stripped out

Parameters :

- verbose ( bool ) – Verbose, Output information about the errors found (optional)

- clean_customdata ( bool ) – Clean Custom Data, Deprecated, has no effect (optional)

Returns :

Result

Return type :

bool
validate_material_indices ( )

Check the polygons' material indices; returns True if any invalid index on the mesh was reset (to the default of 0)

Returns :

Result

Return type :

bool

[Related references](INDEX.md).
