# Vector Displacement Node

## Vector Displacement Node

### Vector Displacement Node 

The Vector Displacement node shifts surfaces along arbitrary axes, contrasting the standard Displacement node which moves along the normal only.

Typical application involves importing vector displacement maps from external sculpting tools. Vector maps fully encode high-resolution detail on a smooth base mesh, unlike standard maps.

Bump Mapping is default in Blender. For genuine displacement, geometry physically deforms in the final render. This requires setting the Displacement method appropriately.

Tip

Genuine displacement achieves best results with fine mesh subdivision.

See also

Material Displacement for thorough displacement documentation.

### Inputs 

Vector
Three-axis displacement specification. Connect a texture node here.

Typically pre-baked vector displacement texture output is used. In Object Space, RGB colors are interpreted as XYZ offsets. In Tangent Space, R shifts along tangent, G along normal, and B along bitangent.

Midlevel
The neutral point. Default 0.0 means zero shift; lower values displace inward, higher values outward.

Scale
Multiply or divide displacement magnitude.

### Properties 

Space
Object Space suits static geometry with faster, lower-memory rendering. Tangent Space supports deforming meshes like animated figures, where displacement follows deformation.

### Outputs 

Displacement
Displacement data for the Material Output socket.

### Examples 

Standard and magnified vector displacement on a smooth base mesh.

[Related references](INDEX.md).
