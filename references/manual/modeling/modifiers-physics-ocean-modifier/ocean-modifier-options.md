# Ocean Modifier: Options

## Ocean Modifier

### Ocean Modifier

What the Ocean modifier offers is a way to simulate and build a deforming ocean surface, paired with a texture that renders out the simulation data. The point of it is to model deep ocean waves and foam.

It comes across as a port of the open source Houdini Ocean Toolkit.

### Options

The Ocean modifier.

Geometry

Generate
Lays down a tiled grid of mesh that lines up exactly with the resolution of the simulation data.

When a mesh surface gets generated, the existing mesh object is wiped out entirely and replaced by the ocean grid,
which also sweeps away anything produced by earlier modifiers in the stack.
A UV channel comes along too, mapping the (0.0 to 1.0) UV space onto the simulation grid.

Repeat X, Y
Sets how many times the grid tiles across the X and Y directions.
UVs for those tiled mesh areas run on past the (0.0 to 1.0) UV space.

Displace
Keeps the existing geometry instead of swapping it out. Vertices get pushed along the local Z axis.

Resolution Viewport, Render
The chief knob trading quality against speed in the simulation engine.
It sets the resolution of the internal 2D grids the simulation builds for the 3D Viewport
or for the final render.

Those internal grids run to powers of two of the resolution value,
so a value of 16 yields simulation data sized 256×256 .
Crank the resolution up for more detail, at the cost of slower calculation.

Note

With the Generate modifier geometry option in use,
this resolution value also governs the resolution of the generated mesh surface,
matching that of the internal simulation data.

Time
The moment at which the ocean surface is evaluated.
For an animated ocean, you'll want to animate this value.
How fast the time value moves sets the pace of the wave animation.

Depth
The fixed depth of the ocean floor beneath the simulated patch.
Lower values stand in for shallower water, throwing up
higher frequency detail and smaller waves.

Size
A plain scaling factor that leaves the wave height and the simulation's behavior untouched.

Spatial Size
How wide a stretch of ocean surface gets simulated, in meters.
It also fixes the size of the generated mesh, or of the displaced area.
You can of course scale the Ocean modifier's object in Object Mode
to nudge its apparent size within your scene.

Random Seed
Change the Seed and you get a different simulation result.

Generate Normals
Works up extra normal map data.
The Ocean texture can draw on it, when mapped to Normals,
as a bump map, and it lets you generate normal map image sequences during baking.

[Related references](INDEX.md).
