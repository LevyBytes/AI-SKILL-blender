# Material Settings

## Material Settings

### Material Settings 

Reference

Panel :

Material ‣ Settings and Shader Editor ‣ Sidebar ‣ Settings

### Surface 

Displacement
The way Displacement is carried out on materials.

Displacement Only :

The mesh vertices move before the render, reshaping the actual mesh.
A finely subdivided mesh gives the cleanest result here.
It is also why this route eats the most memory.

Bump Only :

As the surface shader runs, a doctored surface normal fills in for the genuine one.
Lighter on memory than real displacement, yet only an approximation.
Surface silhouettes come out off, and the displacement throws no self-shadow.

Displacement and Bump :

Pair the two: displace a coarser mesh, then let bump mapping carry the fine detail.

Emission Sampling
How the material's emissive part gets sampled.
It bites only when the material holds an emissive material node; without one it is skipped.

None :

Keep this surface out of light sampling entirely.

Auto :

Let emission intensity decide on its own whether the surface counts as a sampling light.

Front :

Sample only the surface's front face as a light, handy on closed meshes whose inside is never seen.

Back :

Sample only the surface's rear face as a light.

Front and Back :

Sample the surface as a light off both faces, front and back alike.

Transparent Shadows
Use transparent shadows where a Transparent BSDF lives; turning it off renders quicker but skews the shadows.

Bump Map Correction
Lays on fixes for the shadow terminator artifacts bump mapping stirs up.

### Volume 

Sampling Method

Distance :

For dense volumes lit from afar, Distance sampling is usually the leaner pick.

Equiangular :

Park a light inside or near the volume and Equiangular sampling pulls ahead.

Multiple Importance :

Got a blend of the two? Then multiple importance sampling comes out best.

Interpolation
Which interpolation method serves the volume objects and the smoke simulation grids.

Linear :

A plain interpolation that does fine on thin volumes.

Cubic :

A smoothed, high-grade interpolation denser volumes need, at the cost of speed.

Step Rate Biased
Sets the spacing between volume shader samples for volume shaders.
You typically tighten the step for procedural shaders that pile on detail through procedural textures the default step misses.
Live only while Render ‣ Volumes ‣ Biased is on.
See Volume Render Settings for more information.

[Related references](INDEX.md).
