# Volume Scatter

## Volume Scatter

### Volume Scatter

This node lets light scatter as it crosses the volume. A common job is adding fog; paired with the Volume Absorption node it also makes smoke.

### Inputs

Color
Per-channel scattering coefficients.

Density
How strong the scatter effect is.

Anisotropy Henyey-Greenstein Draine
Sets the balance between back- and forward-scattering.

IOR Fournier-Forand
Index of refraction of the scattering particles relative to water. Ordinary ocean water sits between 1.0 and 1.2, while denser, murkier water climbs higher.

Backscatter Fournier-Forand
Share of light thrown back the way it came. Most ocean particles fall between 0.001 (such as very large phytoplankton) and 0.1 (such as very small mineral grains); pure water sits at 0.5. Figures from
Ocean Optics Web Book.

Alpha Draine
A blend control between the Henyey-Greenstein ( \(\alpha = 0\) ) and Cornette & Shanks ( \(\alpha = 1\) ) phase functions.

Diameter Mie
Diameter of the scattering particles in µm.

### Properties

Phase
Volume scattering phase function.

Henyey-Greenstein :

A simple, widely used phase function, handy for roughly modelling scattering inside biological tissue.

Fournier-Forand :

Cycles Only
Aimed at modelling how light scatters underwater.

Draine :

Cycles Only
Aimed at modelling how interstellar dust scatters.

Rayleigh :

Cycles Only
Covers scattering by particles smaller than light's wavelength, like sunlight scattering through Earth's atmosphere.

Mie :

Cycles Only
Covers scattering by particles larger than light's wavelength, like cloud and fog.

Tip

A Mix Shader lets you combine these phase functions.

Volume scattering phase plotted against the angle between incoming and outgoing direction, on a logarithmic scale. Light arrives from the left.

### Outputs

Volume
Feed the Volume Shader result to the Volume Input on either the Material or World Output node.

### Examples

Example of Volume Scatter.

[Related references](INDEX.md).
