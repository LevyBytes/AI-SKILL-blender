# Specular BSDF

## Specular BSDF

### Specular BSDF

EEVEE Only

The Specular BSDF folds several layers together behind one convenient node.

Think of it as a cousin of the Principled BSDF node that follows the specular workflow rather than the metallic one. It carries far fewer settings and covers fewer features; the two may eventually be folded into a single node.

Under the specular workflow you state the reflection colour seen face-on, along the normal. Because nothing enforces energy conservation, the result need not be physically plausible.

### Inputs

Base Color
Diffuse surface colour. Set it to black for conductors (metals).

Specular
How much specular reflection there is, given as the face-on (along-normal) reflectivity. Conductors (metals) may carry a coloured specular reflection.

Hint

To work this figure out for a real material whose index of refraction you know, use this special case of the Fresnel formula:
\(specular = ((ior - 1)/(ior + 1))^2\)

For example:

- water: ior = 1.33, specular = 0.02

- glass: ior = 1.5, specular = 0.04

- diamond: ior = 2.417, specular = 0.17

Roughness
Sets the microfacet roughness of the surface, covering both diffuse and specular reflection.

Hint

Coming from the older Glossy BSDF node, take the square root of the value you had there.

Emissive Color
Colour of the light given off. It is summed onto the BSDF result.

Transparency
A transparency factor, which is just the alpha channel inverted (1 - alpha) as found in an image. Run an Invert node to turn alpha into transparency. It only does anything when the material's blend mode is something other than opaque.

Normal
Drives the normals of the base layers.

Clear Coat
An additional white specular layer laid over the rest, handy for finishes such as car paint.

Clear Coat Roughness:
Roughness of clear coat specular.

Clear Coat Normal
Drives the normals of the Clear Coat layer.

Ambient Occlusion
How much occlusion to lay over indirect lighting, normally fed by a baked ambient occlusion map. The occlusion actually applied is whichever is smaller, this input or the runtime ambient occlusion effect.

### Properties

This node has no properties.

### Outputs

BSDF
Standard shader output.

[Related references](INDEX.md).
