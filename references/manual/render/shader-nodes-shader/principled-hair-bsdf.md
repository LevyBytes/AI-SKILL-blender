# Principled Hair BSDF

## Principled Hair BSDF

### Principled Hair BSDF

*Cycles Only*

A physically-based, artist-friendly shader for hair and fur rendering.

Tip: Realistic hair requires minimal variance across strands. The shader supports this via Random Color and Random Roughness, remapping specified Melanin/Roughness to ±Randomization% range.

### Inputs

### Common

- **Color**: Strand RGB color (Direct coloring only). Converted to absorption via the formula (section 4.2 [CBTB16]): σₐ = ln(Color) / (5.969 − 0.215·β_N + 2.532·β_N² − 10.73·β_N³ + 5.574·β_N⁴ + 0.245·β_N⁵)², where β_N is the radial roughness of the hair after randomization (if specified).
- **Melanin**: Pigment quantity. Range [0, 1] = [0%, 100%]. Linear mapping: melanin_qty = -ln(max(1.0 - Melanin, 0.0001)).
- **Melanin Redness**: Pheomelanin/eumelanin ratio. Range [0, 1] = [0%, 100%]. Formula: eumelanin = Melanin×(1.0-MelaninRedness), pheomelanin = Melanin×MelaninRedness. Converted (after randomization, if specified) to absorption concentration via the formula (section 6.1 [EFHLA11], for the range [0, 1]): σₐ = eumelanin × [0.506, 0.841, 1.653] + pheomelanin × [0.343, 0.733, 1.924].
- **Tint**: Hair dye color after melanin pigment. Not randomized. Disable via white. Converted and added to melanin absorption.
- **Absorption Coefficient**: Attenuation coefficient σ.
- **IOR**: Index of refraction. 1.0 = transparent; higher = more refraction. Default 1.55.
- **Offset**: Cuticle scale angle relative to hair shaft. Humans typically have low values.
- **Random Color**: Per-strand melanin variance by RandomFactor. Range [0, 1] = [0%, 100%] of concentration. Formula: randomFactor = 1.0 + 2.0×(Random - 0.5) × RandomColor.
- **Random Roughness**: Per-strand roughness variance by RandomFactor. Range [0, 1]. Same formula as Random Color.
- **Random**: Random number source. Auto-instanced from Hair Info ‣ Random if unconnected.

### Chiang Model

Based on Gaussian distribution with separate roughness along and perpendicular to hair.

- **Roughness**: Smoothing along hair shaft. Low values risk metallic appearance and fireflies; high values risk Lambertian look.
- **Radial Roughness**: Smoothing across hair width. Low = concentrated glint; high = spread light. Mapped to logistic scale (section 4.1 [CBTB16]).
- **Coat**: Shiny fur coat reducing Roughness by this factor on first bounce. Range [0, 1] = [0%, 100%] reduction.

### Huang Model

Based on microfacet reflection/transmission; supports elliptical hair.

- **Aspect Ratio**: Minor/major axis ratio. 0.8–1 Asian; 0.65–0.9 Caucasian; 0.5–0.65 African. Major axis aligns with curve normal (geometry nodes; unsupported in legacy particles).
- **Roughness**: Microfacet roughness for reflection/transmission.
- **Reflection**: First-bounce modulation (always white). Keep 1.0 for physical accuracy.
- **Transmission**: Transmission modulation (picks up pigment color). Keep 1.0 for physical accuracy.
- **Secondary Reflection**: Transmitted-in, back-reflected, transmitted-out component (pigment color). Keep 1.0 for physical accuracy.

### Properties

**Color Parametrization**: Three coloring methods.

- **Direct Coloring**: Choose RGB; shader approximates absorption coefficient.
- **Melanin Concentration**: Define color via pigment quantity/ratio (eumelanin/pheomelanin). Quantity in Melanin; ratio in Melanin Redness. Increasing darkens hair: White (0), Blonde (0.25), Reddish (0.5), Brown (0.75), Black (1). Tint allows dyeing post-pigment.
- **Absorption Coefficient**: Specify attenuation σₐ via Beer-Lambert law. For technical users using literature coefficients without conversion.

### Outputs

- **BSDF**: Standard shader output.

### References

Implementation of Chiang et al. [CBTB16] and Huang et al. [HHH22].

[CBTB16] (1,2,3) Chiang, M. J., Bitterli, B., Tappan, C. and Burley, B. (2016), A Practical and Controllable Hair and Fur Model for Production Path Tracing. Computer Graphics Forum, 35: 275-283. doi:10.1111/cgf.12830

[EFHLA11] d'Eon, E., Francois, G., Hill, M., Letteri, J. and Aubry, J. (2011), An Energy‐Conserving Hair Reflectance Model. Computer Graphics Forum, 30: 1181-1187. doi:10.1111/j.1467-8659.2011.01976.x

[HHH22] Huang W., Hullin M.B., Hanika J. (2022), A Microfacet-based Hair Scattering Model. Computer Graphics Forum, 41: 79-91. doi:10.1111/cgf.14588

[Related references](INDEX.md).
