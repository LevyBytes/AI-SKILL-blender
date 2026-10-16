# Node Bundles

## Node Bundles

Bundles group multiple values into one socket, like programming structs, enabling single-link passage of many values. Mixed types include geometry, fields, values, objects, or nested bundles. This reduces exposed group inputs/outputs and clarifies interfaces.

Available nodes: Combine Bundle and related nodes for bundle manipulation.

Usage: Simplified interfaces (group inputs into single sockets); physics simulations (package entities/constraints); declarative systems (store structured data for later evaluation); texture sets (combine PBR maps into one socket).

Socket syncing matches bundle inputs/outputs by name. Auto-sync occurs on first connection. Existing sockets don't auto-update (avoiding data loss). A Sync Sockets button appears when mismatches are detected, enabling manual synchronization.

### Node Bundles

A container grouping multiple values into one socket—like a struct in programming.
Bundles pass many values through a single link.
Reduce exposed inputs/outputs in a node group.
Mix data types: geometry, fields, values, objects, nested bundles.

Combining a cube and cylinder into a bundle, then unpacking.

### Nodes

Dedicated nodes for bundle creation and decomposition.
Both support flexible socket count and type.

### Usage

Bundles serve multiple workflows:

- **Simplified interfaces:** Group inputs into one socket.
- **Physics solvers:** Package entities and constraints.
- **Declarative data:** Store complex structured state for later evaluation.
- **Texture sets:** Combine PBR maps (Base Color, Roughness, Normal).

### Socket Syncing

Names match bundle inputs to outputs.
Mismatched signatures prompt automatic sync.

- First connection syncs automatically.
- Existing sockets never change auto-sync to prevent data loss.
- A Sync Sockets button appears in the header when mismatch is detected.

[Related references](INDEX.md).
