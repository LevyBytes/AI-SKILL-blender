# UV Map Node

## UV Map Node

### UV Map Node

Output texture coordinates from a specific UV map. Useful when working with multiple UV layouts in one material. Connect typically to texture node Vector inputs for placement and manipulation.

Note: Unlike Texture Coordinate Node (which outputs only the active render UV map), this node accesses any assigned UV map.

### Inputs

None.

### Properties

**From Instancer** *(Cycles Only)* — See Texture Coordinate Node's From Instancer option.

**UV Map**: Name of the UV map to use. Populated from the object's mesh UV maps. If unset, uses the Active Render UV map.

### Outputs

- **UV**: Coordinates from the specified UV map.

[Related references](INDEX.md).
