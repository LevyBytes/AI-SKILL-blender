# Principled Volume

## Principled Volume

### Principled Volume

The Principled Volume shader gathers every volume-shading component behind one convenient node. A single node can render volumes like smoke and fire, since it bundles scattering, absorption and blackbody emission together.

### Inputs

Color
Volume scattering color.

Color Attribute
Volume grid that colours the volume. Use "color" for smoke simulations.

Density
Density of the volume.

Density Attribute
Volume grid that sets the density, usually "density".

Anisotropy
Backward or forward scattering direction.

Absorption Color
Volume shadow color tint.

Emission Strength
Amount of light to emit.

Emission Color
Emission color tint.

Blackbody Intensity
Blackbody emission for fire. Set to 1 for physically accurate intensity.

Blackbody Tint
Color tint for blackbody emission.

Temperature
Kelvin temperature driving blackbody emission; raise it to emit more.

Temperature Attribute
Volume grid that sets the temperature, usually "temperature".

### Properties

This node has no properties.

### Outputs

Volume
Feed the Volume Shader result to the Volume Input on either the Material or World Output node.

### Examples

[Related references](INDEX.md).
