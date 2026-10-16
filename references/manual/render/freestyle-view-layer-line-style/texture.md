# Texture

### UV Along Stroke Node

UV Along Stroke Node.

This node enables texture application across strokes, allowing simulation of pencil, brush, and various artistic media effects.

Note

UV coordinates are created exclusively by Freestyle's rendering pipeline. Standard UV Map nodes are incompatible, as they work with permanent mesh UV data.

#### Inputs

This node has no inputs.

#### Properties

Use Tips
Designates the lower portion of a texture image for stroke tips (endpoints), with the upper portion spanning the main body.

#### Outputs

UV
Texture coordinates projected along the stroke path.

### Line Style Output Node

Line Style Output Node.

This node merges texture data with the base line-style coloration.

#### Inputs

Color
Incoming color from the texture.

Color Factor
Blending strength for the Color input.

Alpha
Incoming transparency from the texture.

Alpha Factor
Blending strength for the Alpha input.

#### Properties

Mix
Choose the blending method (refer to Color Blend Modes).

Clamp
Caps the output color to a maximum of 1.0.

#### Outputs

This node has no outputs.

### Example

The setup shown below demonstrates how to apply a floral image across strokes. The UV Along Stroke node extracts Freestyle-generated texture coordinates, feeding them to an Image Texture node's Vector input. Once a texture is loaded into the Image Texture node, its output connects to the Line Style Output node's Alpha input. When Alpha Factor is one, the texture replaces the line style's alpha (as shown in the Freestyle Line Style panel). The Color connection employs Mix blending with Color Factor at zero, preserving the line style's gradient overlay.

Example of Line Style Nodes
(blend-file).

The FS_floral_brush.png image featured here is a Freestyle brush texture with dual regions: a seamless tile for the stroke body (top), and tip caps for endpoints (bottom).

[Related references](INDEX.md).
