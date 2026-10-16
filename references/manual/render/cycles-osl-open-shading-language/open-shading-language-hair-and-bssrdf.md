# Open Shading Language: Hair, BSSRDF, Volume, Other, Attributes

### Hair

- hair_reflection(N, roughnessu, roughnessv, T, offset)
- hair_transmission(N, roughnessu, roughnessv, T, offset)
- principled_hair(N, absorption, roughness, radial_roughness, coat, offset, IOR)

### BSSRDF

Models subsurface light scattering.

bssrdf ( method , N , radius , albedo )

Parameters :

- method ( string ) – Algorithm for simulating subsurface scattering.

- burley :
An approximation to physically-based volumetric scattering. Trades accuracy for faster noise reduction in some situations relative to random_walk.

- random_walk_skin :
Delivers accurate results for thin and curved shapes. Uses volumetric scattering within the mesh; works best for closed surfaces. Overlapping faces and mesh holes cause artifacts.

- random_walk :
Similar to random_walk_skin but adjusts Radius based on Color , Anisotropy , and IOR . Attempts to maintain greater surface definition and color compared to random_walk_skin .

- N ( vector ) – Surface normal at the shaded location.

- radius ( vector ) – Average scatter distance below the surface. Larger values yield softer appearance as light penetrates shadows and the object. Specify scatter distance separately for RGB, useful for materials like skin where red light penetrates deeper. X, Y, Z map to R, G, B.

- albedo ( color ) – Surface color, or the likelihood light reflects at each wavelength.

### Volume

- henyey_greenstein(g)
- absorption()

### Other

- emission()
- ambient_occlusion()
- holdout()
- background()

### Attributes

Geometry attributes load via getattribute() . This includes UV maps, color data, and outputs from geometry nodes.

These built-in attributes are also accessible:

geom:generated
Procedurally generated texture coordinates from undeformed geometry.

geom:uv
Primary render UV coordinate.

geom:tangent
Primary tangent vector, in object space.

geom:undisplaced
Position prior to displacement, in object space.

geom:dupli_generated
For instances, generated coordinate from the source object.

geom:dupli_uv
For instances, UV coordinate from the source object.

geom:trianglevertices
Triangle vertex positions.

geom:numpolyvertices
Polygon vertex count (currently always three).

geom:polyvertices
Polygon vertices (always three currently).

geom:name
Object name.

geom:is_smooth
Smooth or flat face shading flag.

[Related references](INDEX.md).
