# Displacement Node

## Displacement Node

### Displacement Node 

The Displacement node shifts geometry along surface normals to introduce additional detail. Procedural textures or pre-baked displacement images can serve as input.

Bump Mapping alone is the default in Blender. Genuine displacement physically deforms rendered geometry. For authentic displacement, the Displacement method configuration is required.

Tip

Genuine displacement benefits from fine mesh subdivision to reveal texture detail.

See also

Material Displacement for comprehensive displacement workflow guidance.

### Inputs 

Height
The offset magnitude along the normal. Connect texture output here.

Midlevel
The neutral displacement threshold. At default 0.5, values below push surfaces inward; values above push outward.

Scale
Amplify or reduce displacement magnitude.

Normal
Standard normal input.

### Properties 

Space
Object Space causes displacement to scale with the object. World Space ignores object scaling.

### Outputs 

Displacement
Displacement data for the Material Output socket.

### Examples 

Typical displacement node setup. 

Bump only, displacement only, and both combined.

[Related references](INDEX.md).
