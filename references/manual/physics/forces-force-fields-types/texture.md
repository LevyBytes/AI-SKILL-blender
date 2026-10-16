# Texture

## Texture

### Texture 

Reference

Panel :

Physics ‣ Force Fields

Type :

Texture

A Texture field permits establishing intricate force distributions with directional intensity encoded by color. Red maps to the X axis, green to Y, and blue to Z (matching 3D Viewport coordinate axis coloring). A value of 0.5 signifies zero force. Values exceeding 0.5 produce acceleration along the negative axis direction (e.g., -Z), while values under 0.5 accelerate along the positive direction (e.g., +Z).

### Options 

UI for a Texture force field. 

Texture Mode

Specifies how force vectors derive from the texture.

Curl :

Derives the force vector from the curl of the 3D-RGB texture (RGB vector rotation). Functions exclusively with color textures. Example use: crafting appealing turbulence with color clouds textures incorporating Perlin noise.

Gradient :

Produces the force vector as the 3D gradient of texture intensity (grayscale). The gradient points in the increasing brightness direction.

RGB :

Applies color components directly as force vector components in the matching axis directions. Requires an RGB texture (image or color ramp), making single-color Blend textures insufficient.

Nabla

Specifies the offset for computing partial derivatives in Gradient and Curl modes.

Use Coordinates

References emitter object coordinates (plus rotation and scale) as the particle texture space. Enables force fields that move and rotate alongside an object.

Root Texture Coordinates

Valuable for hair simulations; applies the texture force calculated at the particle root to the complete hair strand.

2D

Disregards particle Z position, utilizing only X and Y for texture coordinates.

Procedural textures exhibit true three-dimensionality.

### Examples 

- A uniform texture (0.5, 0.0, 0.5) generates positive Y-axis force, aligning hair along the Y direction.

- A blend texture with color ramp establishes a force boundary. Left edge (0.5, 0.5, 0.5), right edge (1.0, 0.5, 0.5) creates a plane perpendicular to XY and parallel to Z. Object coordinate assignment lets the object reposition particles through space.

- An animated wood texture produces wave-like particle motion.

Texture

Maps a texture onto Freestyle strokes.

Line Style: Texture.

Use Nodes
In Cycles, shader Nodes define textures.

Spacing Along Stroke
Adjusts how frequently textures repeat along the stroke.

Go to Linestyle Textures
Provides quick access to texture settings in the Properties Textures panel. Ensure Use Nodes is activated beforehand.

### Nodes

[Related references](INDEX.md).
