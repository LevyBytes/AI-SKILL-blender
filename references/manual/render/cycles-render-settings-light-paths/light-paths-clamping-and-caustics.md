# Light Paths: Clamping, Caustics, Fast GI Approximation

### Clamping

Direct Light
Limits peak intensity from rays not yet bounced. Reduces noise, sacrificing precision. Zero disables clamping. Lower values darken samples more than higher values.

Note

This provides Firefly mitigation, but as you exclude high values, other bright light and reflections dim too.

Care when using this setting balances firefly suppression with preserving intentional bright areas. Clamping indirect bounces separately proves useful since they tend to produce more fireflies than direct bounces. See Clamp Indirect setting.

Indirect Light
Same as Direct Light , but for rays after multiple bounces.

### Caustics

Caustics rank among common noise culprits.

See also

See Reducing Noise for clamping examples.

Filter Glossy
Values above 0.0 blur glossy reflections after diffuse bounces, cutting noise at precision cost. 1.0 offers a suitable starting adjustment.

Certain light paths occur rarely while contributing substantially. Such paths appear in some pixels but not others, generating Fireflies. A difficult path occurs when a small light creates a compact specular highlight on a sharp glossy surface, viewed through a rough glossy layer—approximating a caustic.

Path tracing struggles to locate the specular point, yet boosting the roughness enlarges and softens the highlight, easing detection. Often, existing material roughness masks this blurring, but sometimes detail loss occurs.

Caustics

Reflective
In theory, path tracing renders caustics given sufficient samples, yet practically, the noise proves prohibitive. Deactivate this option to suppress reflective caustics.

Refractive
Similar to reflective caustics: practically, noise becomes excessive. Deactivate to exclude refractive caustics.

### Fast GI Approximation

Reference

Panel :

Render ‣ Light Paths ‣ Fast GI Approximation

Substitute diffuse indirect lighting with background-tinted ambient occlusion. This delivers rapid global illumination substitution for interactive viewport rendering or final renders prioritizing speed over full fidelity.

Method
Fast GI technique selection.

Replace :

Substitute global illumination with ambient occlusion after specified bounces.

Add :

Supplement diffuse surfaces with ambient occlusion.

AO Factor
Ambient occlusion intensity.

AO Distance
Ray tracing extent from shading location. Shorter distance emphasizes nearby aspects, while longer captures farther objects.

Per-object override is available in Object Properties, valuable when scenes mix fine and large features.

Viewport Bounces
Substitute global illumination with ambient occlusion after specified bounces during viewport rendering. This lowers noise in interiors with minimal visual impact.

Render Bounces
Bounce count for final rendering.

Light Paths: Direct and Indirect Control

### Clamping

Reference
Panel: Render ‣ Light Paths ‣ Clamping

[Related references](INDEX.md).
