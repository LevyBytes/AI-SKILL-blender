# Volume Info Node

## Volume Info Node

### Volume Info Node

Retrieve information about Smoke Domains.

### Inputs

None.

### Properties

None.

### Outputs

- **Color** — Smoke color inside the Fluid Domain (same as vector output; Factor is channel average).
- **Density** — Scalar defining smoke density in the Fluid Domain.
- **Flame** — Scalar defining fire density in the Fluid Domain (all three outputs identical).
- **Temperature** — Volume temperature as scalar. Range 0–1 maps to 0–1000 Kelvin. Use with Blackbody or Principled Volume shaders for physically-based fire. Remap temperature first (Blackbody expects Kelvin values).

### Example

Smoke density visualization. / Fire color calculation using the Blackbody node.

[Related references](INDEX.md).
