# Geometry attribute types and domains

## Attributes

An attribute stores per-element data within geometry. Every vertex might hold a number or a vector. Values update via a Group Output connection or through nodes that alter specific attributes.

Data types and domains convert implicitly where supported, like node sockets.

Named attributes appear in other Blender workflows: shaders, painting, UV mapping. In modifiers, use the icon next to a value to pick an attribute by searching existing ones on the input geometry.

Attribute Search display: left shows domain, middle the name, right the data type.

The Normal and Rotation outputs exemplify attribute fields—data stored on geometry referenced by socket.

Anonymous attributes are generic data without a name. Most Blender interfaces expose named attributes, but geometry nodes pass attributes via sockets as Attribute Field outputs. Nodes find the referenced data in the input geometry.

Anonymous attributes stay stored and interpolate across geometry changes, except in rare cases. As long as the socket connection persists, the attribute remains available. They cannot bridge completely separate geometries from different sources. Use Sample Index Node or Sample Nearest Surface Node to transfer between unrelated geometry.

The attribute's underlying representation.

Float: Scalar value (weights, intensity).
Boolean: True/false (conditions).
Integer: 32-bit whole number (indices, counts).
Vector: 3D direction or position.
Color: RGBA in linear space, 32-bit per channel (HDR, wide gamut).
Byte Color: RGBA in sRGB, 8-bit per channel (compact).
String: Text (names, labels).
2D Vector: Flat direction or UV pair.
8-Bit Integer: Compact range (−128 to 127).
2D 16-Bit Integer Vector: Compact 2D pair (signed).
2D Integer Vector: Standard 2D pair (signed, 32-bit).
Quaternion: Rotation representation.
4x4 Matrix: Transformation or spatial relationship.

Ordered from least to most "data-rich" (integer > boolean, more complex = more data). When joining geometries with matching names, the richer type is preferred. This matters with Join Geometry Node.

2D Vectors (UV) and Byte Colors require Store Named Attribute (no sockets).

Data conversions via Geometry Nodes:

Color ↔ Vector: Channel-to-component mapping.
Color ↔ Float: Color becomes grayscale.
Float ↔ Integer: Integer → Float direct; Float → Integer truncates.
Float ↔ Vector: Float → Vector copies to all components; Vector → Float averages.
Float ↔ Boolean: > 0 → True; True → 1, False → 0.

The domain defines the geometry element type the attribute binds to.

Point domain: Single spatial locations (mesh vertices, cloud points, curve control points).
Edge domain: Mesh edges.
Face domain: Mesh faces.
Face Corner domain: Face corners (e.g., UV maps).
Spline domain: Connected curve control point groups.
Instance domain: Instances in geometry; only in geometry nodes.
Layer domain: Grease Pencil layers.

Attributes auto-convert between domains. When Position (point domain) feeds a face selection, values interpolate to faces. Boolean interpolation uses special rules:

| From | To | Conversion |
| --- | --- | --- |
| Point | Edge | An edge is selected if both of its vertices were selected. |
| Point | Face | A face is selected if all of its vertices were selected too. |
| Point | Corner | Each corner's value is simply a copy of the value at its vertex. |
| Point | Spline | A spline is selected if all of its control points were selected. |
| Edge | Point | A vertex is selected if any connected edge was selected. |
| Edge | Face | A face is selected if all of its edges are selected. |
| Edge | Corner | A corner is selected if its two adjacent edges were selected. |
| Face | Point | A vertex is selected if any of the connected faces were selected. |
| Face | Edge | An edge is selected if any connected face was selected. |
| Face | Corner | Each corner's value is simply a copy of the value at its face. |
| Corner | Point | A vertex is selected if all connected face corners were selected and it is not a loose vertex. |
| Corner | Edge | An edge is selected if all corners on adjacent faces were selected. |
| Corner | Face | A face is selected if all of its corners were selected. |
| Spline | Point | Each point's value is simply a copy of the corresponding value of the spline. |

[Related references](INDEX.md).
