# Point Cloud Properties

## Point Cloud Properties

### Point Cloud Properties

### Attributes

Each point in a cloud carries data fields, and the Attributes panel is where those fields are listed.
Properties such as a point's location, its size, its color, and its motion are all defined through these attributes.

Browsing, creating, editing, and removing attributes all happen through the List View interface.

### Attribute Types

Point cloud objects ship with a set of common built-in attributes, listed below:

See also

Built-In Attributes covers the broader range of attribute types found across Blender's geometry system.

| Name | Type | Domain | Description |
| --- | --- | --- | --- |
| position | Vector | Point | Holds the point's 3D coordinates within the object's own local space. |
| radius | Float | Point | Sets how large each point appears (its visual radius) when drawn or rendered. |
| color | Color | Point | The point's display color, applied during viewport drawing or shading. |
| id | Integer | Point | Gives each point a one-of-a-kind identifier, handy for keeping references stable over time. |
| velocity | Vector | Point | Records which way the point is moving and how fast (used for simulations or motion blur, for example). |

Custom Attributes
Particles can be handed a custom attribute to carry a characteristic of your own choosing.

Name
What the attribute is called.

Data Type
Which kind of data the attribute will hold.

Float :

Floating-point value

Integer :

32-bit integer

Vector :

3D vector with floating-point values

Color :

RGBA color with floating-point precision

Byte Color :

RGBA color with 8-bit precision

String :

Text string

Domain
Which kind of element holds the attribute.
For now, Point is the only domain an attribute can live on.

### Custom Properties

Point cloud objects can also receive custom properties of their own.
Rather than living per point, these properties are attached at the object level.

The Custom Properties
documentation walks through how to add and work with them.

[Related references](INDEX.md).
