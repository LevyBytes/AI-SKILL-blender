# idprop.types.IDPropertyGroup: pop ( key , default )

pop ( key , default )

Take an item out of the group and hand back its Python form.

Raises :

KeyError – When the item doesn’t exist and no default is given.

Parameters :

- key ( str ) – Name of item to remove.

- default ( Any ) – Value to return when key isn’t found (optional, a KeyError is raised when omitted and the key is not found).

Returns :

A Python representation of the removed item, or default .

Return type :

Any

[Related references](INDEX.md).
