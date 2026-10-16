# Light Settings (Cycles): Using Shader Nodes, Light Output, Limitations

### Using Shader Nodes 

A light defaults to a plain node setup: one Emission shader feeding straight into the Light Output .

Bring in further shader and utility nodes and richer setups open up, for instance:

- Blending several Emission shaders so the light carries layered colors.

- Letting Texture nodes shift a light's color or intensity from one part of its surface to another.

- Steering a light's intensity or color through math nodes or animation.

That is the path to effects such as patterned lights, an animated flicker, or a light tinting itself by time or some other input.

### Light Output 

The Light Output node names the final shader the light object uses.
In Cycles, only shader nodes feeding this output sway how the light looks.

### Limitations 

- Only Cycles honors shader-based light definitions.
EEVEE runs on simplified light models and pays light shader node trees no mind.

- Lighting draws solely on Emission -based shading.
Hang any other shader type on a light, a BSDF shader say, and it does nothing.

Going the shader-node route for lights hands you fine-grained control and opens procedural lighting workflows that the standard light settings can never reach on their own.

[Related references](INDEX.md).
