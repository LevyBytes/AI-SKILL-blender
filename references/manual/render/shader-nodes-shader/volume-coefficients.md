# Volume Coefficients

## Volume Coefficients

### Volume Coefficients

This node captures three physical effects inside a volume — absorption, scattering and emission — each via its coefficient. The usual approach is to feed it numbers taken from real-world measurements.

### Inputs

### Absorption

Coefficients
Per-channel probability density that light is absorbed over each unit of distance through the medium. This equals \((1-\text{Color}) \times \text{Density}\) in
Volume Absorption.

### Scatter

Coefficients
Per-channel probability density of an out-scattering event over each unit of distance through the medium. This equals \(\text{Color} \times \text{Density}\) in
Volume Scatter.

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

Note

The inputs above match those in Volume Scatter.

### Emission

Coefficients
Per-channel radiance added onto a ray over each unit of distance. This equals \(\text{Color} \times \text{Strength}\) in Emission.

### Properties

Phase

Note

Same as Phase in Volume Scatter.

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

### Outputs

Volume
Feed the Volume Shader result to the Volume Input on either the Material or World Output node.

[Related references](INDEX.md).
