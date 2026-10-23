# bpy.types.ShaderNodeBsdfHairPrincipled: properties

## ShaderNodeBsdfHairPrincipled(ShaderNode)

### ShaderNodeBsdfHairPrincipled(ShaderNode)

base classes: bpy_struct, Node, NodeInternal, ShaderNode
class bpy.types. ShaderNodeBsdfHairPrincipled ( ShaderNode )

A physically grounded yet easy-to-handle shader for rendering hair and fur
model

Pick either the Chiang or the Huang model (default 'HUANG' )

- CHIANG
Chiang – Near-field hair scattering from Chiang et al. 2016, good for close-up shots but noisier when seen from afar..

- HUANG
Huang – Multi-scale hair scattering from Huang et al. 2022, works both up close and at a distance, handles elliptical cross-sections, and gives sharper highlights in forward-scattering directions..

Type :

Literal[‘CHIANG’, ‘HUANG’]
parametrization

Pick how the shader's color is parametrized (default 'COLOR' )

- ABSORPTION
Absorption Coefficient – Set the absorption coefficient "sigma_a" by hand, which is not the most intuitive route to coloring hair.

- MELANIN
Melanin Concentration – Set the melanin concentrations below for the most lifelike hair; you can look up typical concentrations for various hair types online.

- COLOR
Direct Coloring – Pick whatever color you like and let the shader estimate the absorption coefficient to match it.

Type :

Literal[‘ABSORPTION’, ‘MELANIN’, ‘COLOR’]

[Related references](INDEX.md).
