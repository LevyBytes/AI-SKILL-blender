# UV Operators: Options

### Options

Adjust Last Operation panel allows detailed control:

Method

Angle Based:

Uses Angle Based Flattening (ABF). Produces a precise 2D representation.

Conformal:

Uses Least Squares Conformal Mapping (LSCM).
Typically gives less accurate UV mapping than Angle Based, yet performs better on simpler shapes.

Minimum Stretch:

Uses Scalable Locally Injective Mapping (SLIM). Seeks to reduce both area and angle distortion.

Fill Holes
Pre-fill holes to better reduce overlaps and maintain symmetry during unwrap.

Use Subdivision Surface
Apply vertex positions from the Subdivision Surface Modifier (rather than pre-modifier positions).

Correct Aspect
Compensates UV mapping for the target image's aspect ratio.
UVs scale properly when unwrapping to non-square textures.

For this to function, the mesh needs a material with an Image Texture node, which must be chosen in the Shader Editor.

Iterations Minimum Stretch
Repetitions for Minimum Stretch method, with each reducing distortion further.

No Flip Minimum Stretch
Prevent faces from flipping. Flipping occasionally lowers distortion when pins are used.

Importance Weights Minimum Stretch
Use a vertex group to manually control face sizes in the UV map.
High-weight faces consume more UV space than low-weight ones.

Enabling reveals two additional settings:

Weight Group
The vertex group name to apply.

Weight Factor
A scale applied to all weights. Larger values exaggerate high-weight versus low-weight zones.

Margin Method
The Margin parameter's meaning, governing empty space between UV islands.

Scaled
Margin is somewhat arbitrary, independent of UV island sizes or texture dimensions.

Add
Like above, but without internal scaling.

Fraction
Margin is a fraction of UV bounds. On a 1024x1024 texture with Margin at 1/1024, islands get 1-pixel margins (and stay 2+ pixels apart).

Margin
Empty space between islands. Margin Method controls its interpretation.

[Related references](INDEX.md).
