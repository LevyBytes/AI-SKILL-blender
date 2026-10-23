# Bevel Node

## Bevel Node

### Bevel Node

*Cycles Only*

Add softened edges to shading using this node. Like bump mapping, it only affects shading, not actual geometry. Realistic specular highlights emerge from slightly rounded edges, mimicking real-world materials.

Bevel is computationally expensive and may reduce render speed by 20% even with high scene complexity. Reserve it for baking or static frame renders where render time is less critical. The Bevel Modifier offers faster alternatives but sometimes fails on complex geometry.

**Limitations:**
- The node produces invalid results when the object is a Caustic caster or receiver while the scene contains active caustic elements (caster, receiver, and Shadow Caustic Light).
- Does not work with Open Shading Language active on OptiX backends.

### Inputs

- **Radius**: Width of the bevel effect on edges.
- **Normal**: Normal to apply bevel atop; combines with Bump Nodes. Defaults to surface normal when disconnected.

### Properties

**Samples**: Number of samples per shader evaluation. More samples improve accuracy but slow rendering. 4 is typical; extra AA samples resolve remaining noise.

### Outputs

- **Normal**: Standard normal output.

### Examples

Minimal node setup for bevel work. / Bevel shader revealing specular highlights on edges.

[Related references](INDEX.md).
