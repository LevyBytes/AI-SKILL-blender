# Simulation Nodes

## Simulation Nodes

### Simulation Nodes 

Geometry Nodes can construct custom physics simulations via Simulation Zones.
Simulation zones enable one frame's output to influence the next, allowing simple rules to produce complex behaviors over time.
Physics simulation with dedicated solvers represents the most common use case.

See also

Simulation Zones documentation

### Baking 

Playback automatically caches the simulation.
A bright yellow timeline line marks valid cache frames, enabling animators to review all previous frames rapidly.

Cached frames in the Timeline. 

Once complete, baking to disk permits non-sequential rendering.

Simulation and Physics, Geometry Nodes interface. 

Note

Baking simulations bakes all simulations in all modifiers for selected objects.

Calculate to Frame
Computes geometry node simulations from start to current frame.

Bake
Commits simulations in geometry node modifiers to disk.
The blend-file must be saved; file location determines baked-data location.
Modifier Internal Dependencies allow per-modifier baked-data directory changes.

Delete Cached Simulation
Removes cached/baked geometry node simulations.

Cache
For scenarios where current frame alone matters, disable caching to conserve memory.

### Examples 

Combined with Index of Nearest, this enables numerous sphere-based simulations.

[Related references](INDEX.md).
