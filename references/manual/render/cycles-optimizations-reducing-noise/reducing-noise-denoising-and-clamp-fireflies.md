# Reducing Noise: Denoising, Clamp Fireflies

### Denoising

Despite the techniques described, some render noise persists regardless of sample count. Implement post-processing denoising to clean this final noise layer. Activate Denoising in the Render tab of the Properties.

An example render by The Pixelary appears below.

| Description | Description |
| --- | --- |
| Example render before denoising. | Example render after denoising. |

### Clamp Fireflies

Even with earlier strategies, Fireflies occasionally appear. Individual light ray contributions to each pixel are clamped using the integrator Clamp setting, limiting their maximum intensity.

Overly aggressive clamping removes intentional bright features needed for effects like bloom or glare. To balance these concerns, clamp only indirect bounces, preserving direct highlights without modification.

| Description | Description |
| --- | --- |
| No Clamp (0). | With Clamp set to 4. |

[Related references](INDEX.md).
