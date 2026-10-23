# bpy.types.Attribute: overview

class bpy.types. Attribute ( bpy_struct )

Geometry attribute
## Attribute(bpy_struct)

A data channel attached to geometry elements.

Attributes store information tied to vertices, edges, faces, or other geometry components.
Each attribute has a name, a type, and is stored on a specific domain.

`name`
The `name` of this attribute. Names are distinct within a given geometry.
If the name starts with a `.`, the attribute remains hidden in the user interface.

Data type
The `data_type` describes what kind of values this attribute holds, like floating-point, integer, color, and so forth.
See Attribute Type Items.

`domain`
The geometry area where the attribute is stored.
See Attribute Domain Items.
### Handling Attributes 

Attributes can be stored on geometries like Mesh, Curves, PointCloud, etc.
These geometries have attribute groups (usually called attributes ).
The linked `radius_attribute` example accesses attributes by name.


The linked `create_point_attribute` example calls `attributes.new`.


The linked `remove_drawing_attribute` example removes a custom attribute.


Note

Some attributes are required and cannot be removed, like "position" .

Attribute values are read by accessing their attribute.data collection property.
However, in cases where multiple values should be read at once,
it is better to use the bpy_prop_collection.foreach_get function and read the values into a numpy buffer.


Note

Some attribute types use different named properties to access their value.
Instead of value , vectors use vector , and colors use color .

Writing to different attribute types is very similar. You can simply assign to a value directly.
Again, when writing to multiple values, it is recommended to use the bpy_prop_collection.foreach_set function
to write the values from a numpy buffer.


The bpy_prop_collection.foreach_get / bpy_prop_collection.foreach_set methods require a flat array.
This is sometimes not desirable, e.g. when reading/writing positions, which are 3D vectors.
The linked `read_positions` example uses `np.ravel` to pass a flat array.


base class: bpy_struct

subclasses —
BoolAttribute, ByteColorAttribute, ByteIntAttribute, Float2Attribute, Float4x4Attribute, FloatAttribute, FloatColorAttribute, FloatVectorAttribute, Int2Attribute, IntAttribute, QuaternionAttribute, Short2Attribute, StringAttribute

[Complete example](../../examples/attribute-value-access.py).

Pass the geometry owner named in each function signature. Radius examples require at least one curve point and an existing radius attribute; position access requires a position attribute. The drawing-removal example expects an attribute named `some_attribute`.

[Related references](INDEX.md).
