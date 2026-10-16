# Generate Hair Curves

## Generate Hair Curves

### Generate Hair Curves

Generate Hair Curves builds brand-new strands procedurally over a mesh surface, growing them from nothing at sampled points rather than reusing existing hair. When curves should instead interpolate or trail existing guides, switch to the Interpolate Hair Curves node.

Note

This node or modifier only works with valid Surface geometry or object inputs plus a Surface UV Map .

### Inputs

Surface Input Type
Picks how surface data is supplied for interpolation.

Object :

Provide the surface through an object reference.

Geometry :

Wire a geometry input straight to the surface mesh.

Surface
The surface object generation runs on. For placement to land right, its transforms must line up with the modifier object's.

Surface UV Map
The UV map that fixes where strand roots sit on the surface mesh.

Surface Rest Position
On, the surface mesh drops to its rest pose before strands grow, keeping attachment spots consistent when the surface deforms later.

Tip

Pairing this with Deform Curves on Surface, enable Surface Rest Position when the deform node sits after this one in the stack, so generation reads pre-deformed surface positions.

Hair Length
Length of the generated strands.

Hair Material
Material handed to the generated strands.

Control Points
Control points per generated strand. More points mean smoother deforms and finer control.

### Distribution

Distribution Method
Sets how root points spread over the surface.

Random :

Drops points randomly across the surface.

Poisson Disk :

Holds a minimum gap between points via Poisson disk distribution. Distribute Points on Faces covers the specifics.

Density
Strands per unit of surface area. Crank it up for denser coverage.

Density Mask
A scalar factor modulating density over the surface, so regions carry more or fewer curves.

Mask Texture
An image texture that discards curves by pixel value, read through the Surface UV Map input. White keeps curves; black clears them.

Tip

Read once root points exist, the texture is not capped by mesh vertex density. The Density Mask input tends to be quicker; pairing both trades flexibility against efficiency.

Viewport Amount
A factor thinning viewport curve density for speed; the final render stays whole.

Seed
The distribution's random seed. Move it to reshape the pattern with everything else held.

### Outputs

Geometry
Output geometry holding the generated hair curves.

Curves
A standalone output of the generated curve data alone, ready to process or inspect.

Surface Normal
Where each strand attaches, the surface normal heading there.

[Related references](INDEX.md).
