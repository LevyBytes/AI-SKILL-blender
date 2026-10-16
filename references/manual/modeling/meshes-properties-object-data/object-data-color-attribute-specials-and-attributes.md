# Object Data: Color Attribute Specials, Attributes, Texture Space, Remesh, Geometry Data

### Color Attribute Specials

The menu to the right of the list holds these operators.

Duplicate Color Attribute
Copies the active color attribute into a new list entry.

Convert Color Attribute
Switches the storage format of the color attribute.

Domain
Which slice of geometry holds the attribute. See Attribute Domains for more information.

Vertex :

One color value per vertex.

Face Corner :

One color value per face corner.

Data Type
How colors are represented internally.

Color :

Floating-point RGBA.

Byte Color :

8-bit RGBA.

### Attributes

An attribute is per-element mesh data, each one carrying a data type, domain, and name. This panel shows only custom attributes, leaving out built-ins like position and the likes of vertex groups.

See Attributes Reference for more information.

### Texture Space

Every object can carry an auto-generated UV map, tunable from here.

See Generated UV Properties for more information.

### Remesh

Meshes built to portray organic forms often end up with uneven geometry, which trips up rigging or any workflow wanting simpler topology, 3D printing among them. Remeshing regenerates that geometry with more uniform topology, adding or cutting detail to hit your chosen resolution. It's a particular help in sculpting, giving you cleaner topology once the rough shape is blocked in.

See Remeshing for more information.

### Geometry Data

A mesh object can hold various kinds of custom data. It's mostly for internal use, though some exporters can write it out. See Geometry Data for more information.

[Related references](INDEX.md).
