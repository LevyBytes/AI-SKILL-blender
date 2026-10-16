# Render Baking: Influence

### Influence 

Combined

Lighting

Direct
Fold in the direct lighting.

Indirect
Fold in the indirect lighting.

Contributions

Diffuse
Fold in the diffuse share.

Glossy
Fold in the glossy share.

Transmission
Fold in the transmission share.

Emit
Fold in the emission share.

Diffuse, Glossy, Transmission

Contributions

Direct
See above.

Indirect
See above.

Color
Colorize the pass.

- Select Color on its own and you receive the pass color, a surface trait that holds no matter how far sampling refines.

- Leave Color off and the direct or indirect contributions come back in gray-scale.

- Turn on Color together with Direct or Indirect, and those contributions come back tinted.

Normal

Space
You can bake normals into any of a few spaces:

For materials, the same set of spaces sits in the image texture options, right beside the Normal Map setting already there. For a correct result, keep this choice in step with whatever you baked with.

Object :

Normals stated in object coordinates: object transformation leaves them be, while deformation does move them.

Tangent :

Normals stated in tangent space coordinates, untouched by object transformation and by deformation alike.
This is the default and the right call most of the time, because the normal map then carries over to animated objects too.

Swizzle R, G, B
Which axis lands in each of the red, green and blue channels.

[Related references](INDEX.md).
