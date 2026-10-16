# Introduction

### Introduction 

Blender's physics infrastructure enables simulation of numerous real-world behaviors. These capabilities facilitate both static and dynamic effects including:

- Hair, grass, and flocks

- Rain

- Smoke and dust

- Water

- Cloth

- Jello

- etc.

### Quick Effects 

Reference

Editor :

3D Viewport

Mode :

Object Mode

Menu :

Object ‣ Quick Effects

Automatically constructs fundamental simulation configurations, pre-populating with essential components like domains or particle systems bearing predefined parameters. This approach delivers immediate visible results.

### Quick Fur 

Applies a fur configuration to target objects. The fur system builds on Geometry Nodes, utilizing Hair Node Groups bundled with Blender as native resources.

Density

The surface density of hair curves to generate.

Length

The span of produced hair curves.

Hair Radius

The width measurement of hair, used by rendering engines.

View Percentage

Density scale factor applied in the viewport.

Apply Hair Curves

Executes the modifier employing the Generate Hair Curves node group.

Noise

Applies noise-based deformation to hair curves. Inspect the Hair Curves Noise node group for implementation details.

Frizz

Uses random vectors per point to disorder hair curves. Reference the Frizz Hair Curves node group.

[Related references](INDEX.md).
