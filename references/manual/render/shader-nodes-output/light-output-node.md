# Light Output Node

## Light Output Node

### Light Output Node

Define the final shader for a Light object. Control light emission using shader nodes. Currently, light shaders work only with Cycles; other renderers ignore this node.

See Nodes for shader node usage with lights.

### Inputs

- **Surface** — Shader controlling emitted light. Typically an Emission shader defining color and intensity. Only emission-based shading affects lighting; other shader types have no effect.

### Properties

**Target** — Specify which render engine uses the connected shader.

- **All** — Used by all render engines.
- **Cycles** — Used only by Cycles.
- **EEVEE** — Used only by EEVEE.

Multiple Light Output nodes with different targets enable renderer-specific light setups.

### Outputs

None.

[Related references](INDEX.md).
