# Tone Map Node

## Tone Map Node

Tone mapping maps high-dynamic-range colors into the display's more limited range while keeping the appearance as close as possible. This is a legacy node — it's recommended instead to use view transforms in the color management settings and output linear HDR images from the compositor rather than low dynamic range. Inputs: Image (an HDR image); Type, the algorithm — Rh Simple (a simplified Reinhard operator using the image's average luminance, good for quick general-purpose tone mapping) or R/D Photoreceptor (a more complex model of human photoreceptor response allowing finer adaptation, contrast, and color-correction tuning); Intensity (R/D Photoreceptor — below zero darkens, above brightens); Contrast (R/D Photoreceptor — 0 uses an estimate from the input); Light Adaptation (R/D Photoreceptor — 0 global, 1 by pixel intensity); Chromatic Adaptation (R/D Photoreceptor — 0 the same for all channels, 1 independent per channel); Key (Rh Simple — the value the average luminance maps to); Balance (Rh Simple — normally 1, but usable to alter the brightness curve); and Gamma (Rh Simple — set to 1 if unused). Output: Image (an LDR image).

[Related references](INDEX.md).
