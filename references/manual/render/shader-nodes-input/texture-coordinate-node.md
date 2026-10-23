# Texture Coordinate Node

## Texture Coordinate Node

### Texture Coordinate Node

Output various coordinate systems for procedural textures, image textures, and vector-based texture inputs. Connect typically to texture node Vector inputs to place or manipulate textures in different spaces.

### Inputs

None.

### Properties

**Object**: Specific object for object-space coordinates. Affects only the Object output.

**From Instancer** *(Cycles Only)* — When geometry is instanced from vertices or faces, source texture coordinates from the instancer. Affects Generated and UV outputs only.

Note: From Instancer works with UV output only when the object is instanced (particles or faces).

### Outputs

- **Generated**: Auto-generated coordinates from mesh vertex positions (non-deformed). Range 0.0–1.0 across object bounding box; stays attached to surface under animation. See Texture Spaces.
- **Normal**: Object-space normal for texturing fixed to the object as it transforms. Works on Point and Spot lights, accounting for light rotation.
- **UV**: Active Render UV map coordinates. See UV Mapping. To use non-active UV maps, use UV Map node.
- **Object**: Uses another object (often an empty) as coordinate source. Easily places small images at specific locations or animates texture movement.
- **Camera**: Position in camera space.
- **Window**: Screen location (0.0–1.0 left-to-right, bottom-to-top). Suited for blending objects.
- **Reflection**: Direction of reflection vector as coordinates. Use for reflection maps and environment mapping.

[Related references](INDEX.md).
