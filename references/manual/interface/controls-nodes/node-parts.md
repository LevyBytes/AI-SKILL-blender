# Node Parts

## Node Parts

All Blender nodes share a common construction — regardless of type — comprising the title, sockets, properties, and more.

Title: shows the node's name/type, which can be overridden via the node's Label. The collapse toggle on the title's left side collapses the node, which you can also do with H.
Preview: an overlay showing a small image above the node with the node's result. Not every node supports previews; those that do can be toggled via the icons in the node's top-right corner next to the title. Disable previews for the whole node tree with the Previews overlay toggle.

Sockets: a node's input and output values, shown as little colored circles on either side of the node; hide unused ones with Ctrl-H. Each socket is color-coded by the data type it handles.
Built-in:
- Shader (bright green): shaders in Cycles and EEVEE.
- Geometry (Sea Green): used in Geometry Nodes.
- Menu (Dark Grey): enum-style inputs shown as a dropdown menu or radio button in the UI.
- Bundle (dark turquoise): a generic bundle of multiple data types grouped together (e.g. geometry, vectors, or colors) for compact data transfer between nodes.
- Closure (light brown): used in Shader Nodes and Geometry Nodes for logical or procedural encapsulation; a closure stores and passes groups of node inputs and logic, enabling reusable "callable" node behaviors.
Data:
- Boolean (light pink): passes a true or false value.
- Color (yellow): accepts/produces color information, with or without an alpha component depending on the node tree type.
- Float (light gray): accepts/produces floating-point numbers.
- Integer (lime green): passes an integer value (a number without a fractional component).
- String (light blue): passes a text value.
- Vector (dark blue): vector data such as coordinates and normals, with 2, 3, or 4 components: 2D (shows and uses only X and Y), 3D (X, Y, and Z), 4D (X, Y, Z, and W).
- Rotation (pink): a rotation/quaternion.
- Matrix (dark pink): a 4×4 matrix of float values, often used to represent a Transformation Matrix.
Data-Blocks:
- Collection (white): passes a collection data-block.
- Object (orange): passes an object data-block.
- Material (salmon): passes a material data-block.
- Texture (pink): passes a texture data-block.
- Image (apricot): passes an image data-block.
- Font (brown): passes a font data-block.

Socket Shape: data sockets can take different shapes for the data structure used to transport data; the structure sets how values are passed and interpreted, and more complex structures move multiple values through a single connection.
- Auto: automatically detects a good structure type based on how the socket is used.
- Dynamic (Circle): works with multiple structure types.
- Single (Square): expects a single value.
- Fields (Diamond) — a value that can vary per element (e.g. per point, edge, or face); think of a field as a "value map," similar to how a grayscale image's pixel brightness represents varying values across space. Connecting a single value to a field socket implicitly broadcasts it, so every element receives the same value. Field appearances: Diamond (the socket accepts a field input or outputs a field; a constant single value can connect, but then the output often won't vary per element) and Diamond with Dot (the socket can be a field but is currently a single value — helpful for tracking where single values are calculated rather than a many-result field, and it makes Socket Inspection show the value instead of field input names). See the Geometry Nodes Fields documentation.
- Grid (Four Squares): a grid data structure storing values sampled across a 2D surface or a 3D volume (such as image pixels, voxel densities, or other sampled values in space), allowing complex operations where values are distributed continuously across space rather than attached to individual geometry elements.

Inputs: located on the node's bottom-left, supplying the data the node needs to do its job. Except for the green shader input, each input socket when disconnected has a default value editable via a color, numeric, or vector interface input. Some nodes have special sockets that accept multiple inputs, drawn with an ellipsis shape rather than a circle to mark their special behavior.
Outputs: located on the node's top-right, connectable to the inputs of nodes further down the node tree.
Conversion — some socket types can convert to others, implicitly or explicitly. Implicit conversion happens automatically without a conversion node — for example, Float sockets and Color sockets can link to each other. Once a conversion is made, data may be lost and can't be retrieved later down the tree, and implicit conversion can sometimes change the data units: plugging a Value input node into an angle socket defaults to radians regardless of the scene's Units, because the Value node has no unit while the angle input does.

Valid socket conversions connect color/vector, color/float, color/float/vector to shaders, integers/floats, floats/vectors, floats/booleans, and rotations/matrices. Explicit conversion uses nodes like Shader To RGB or RGB to BW. The Math Node also handles degree/radian conversion.

Most nodes have settings affecting input/output interaction, located below outputs and above inputs. Example: controls on the Chroma Key node illustrate property placement.

[Related references](INDEX.md).
