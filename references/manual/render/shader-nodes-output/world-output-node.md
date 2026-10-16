# World Output Node

## World Output Node

### World Output Node

Output color to the scene's World. Switch the Shader Editor header to World mode to access this node.

### Inputs

- **Surface** — Environment appearance. Usually connects to a Background shader.
- **Volume** — Volumetric world effects. See Principled Volume, Volume Absorption, Volume Scatter.

Note: Surface and Volume cannot coexist—surfaces sit at infinite distance, so they fully occlude volume.

### Properties

**Target** — Render engine for input shaders. Default: shaders shared between Cycles and EEVEE. Multiple output nodes enable engine-specific setups.

### Outputs

None.

[Related references](INDEX.md).
