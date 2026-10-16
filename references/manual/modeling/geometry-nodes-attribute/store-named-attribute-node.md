# Store Named Attribute Node

## Store Named Attribute Node

The Store Named Attribute node writes a field result onto geometry with a specified name. If the attribute exists, its type and domain update. Built-In Attributes cannot change type or domain.

Compared to Capture Attribute, this stores under a name instead of anonymously. For local reuse, Capture Attribute avoids name collisions.

If geometry contains multiple component types, the attribute is placed on each component supporting the chosen domain.

Geometry: Standard input.

Selection: Boolean field determining which elements receive the stored value. Unselected parts fill with zeros if the attribute is new, otherwise remain unchanged.

Value: The field to store.

Name: The attribute's identifier.

Data Type: The stored data kind.
Domain: The attribute category.

Geometry: Standard output.

[Related references](INDEX.md).
