# Object Data: Vertex Groups, Shape Keys, UV Maps, Color Attributes, Creating a New Color Attribute

## Object Data

### Object Data

Select a mesh object and these panels appear in the Data tab of the Properties Editor.

Mesh data-block
Use the Data-Block Menu up top to repoint the object at different mesh object data.

### Vertex Groups

A vertex group tags a set of vertices, optionally weighted, for some operator to act on. One object can hold several, assignable in Weight Paint mode or in Edit Mode through this panel.

See Vertex Groups for more information.

### Shape Keys

Use Shape Keys to morph one shape into another. See Shape Keys Panel for more information.

### UV Maps

A UV Map projects a 3D object onto a 2D plane, fixing where a texture lands on it. You can keep separate UV Maps for separate textures. For more information see UV Maps.

### Color Attributes

Rather than going through a texture or material, you can paint color straight onto an object's vertices. Two paint modes exist. Vertex Paint mode paints per face corner once you turn on the header's paint mask, which helps keep crisp edges in the color attribute on low-poly assets. Sculpt mode, by contrast, lets you paint across a far denser vertex count.

### Creating a New Color Attribute

Click the plus icon beside the attribute list to make one. A pop-up opens asking for:

Name
What the Color Attribute is called, usable as a reference elsewhere in Blender.

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

Color
The starting fill color for every element in the domain.

[Related references](INDEX.md).
