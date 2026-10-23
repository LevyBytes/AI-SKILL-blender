# Common Modifier Options

## Common Modifier Options

Many modifiers share common options for controlling their effect on specific vertices using weights or textures.

Vertex Groups enable targeted per-vertex control. A group's weights determine how strongly the modifier acts on each vertex.

A field displays the current group name. When a group is renamed, any modifier referencing it loses the link (the field turns red), requiring manual re-selection.

Invert reverses the group's effect: selected vertices now represent areas the modifier will not touch. The inversion flips the weight values.

Texture-based masking allows any image (including procedural textures) to control modifier strength. Most often the grayscale value is used, though some modifiers (like Displace in certain modes) read RGB channels.

The Texture field selects which texture to use. A properties icon button jumps to that texture's settings.

Texture Coordinates specify how to sample the texture at each vertex:

UV uses face UV coordinates from the geometry. The system finds UV values for each vertex from the first face using it; additional faces are ignored. This can produce artifacts on meshes with discontinuous UVs.

UV Map selects which UV layer to sample. If missing, the system defaults to Local coordinates.

Object reads texture coordinates from another object's local space. Moving that object updates the texture position. If empty, Local is used.

Moving the source object also shifts the texture mapping. If you need stable displacement relative to the modified object, consider parenting the source object to it.

Global uses world-space coordinates.

Local uses the modified object's local space.

Use Channel selects which texture information to read:

Intensity takes the average of RGB channels (RGB 1.0, 0.0, 0.0 = 0.33 intensity).

Red/Green/Blue/Alpha reads individual color channels.

Hue extracts the HSV hue value (color position on the standard wheel).

Saturation extracts the HSV saturation (1.0 for pure colors, 0.0 for grays).

Value extracts the HSV brightness component.

All channels are gamma-corrected except Intensity.

[Related references](INDEX.md).
