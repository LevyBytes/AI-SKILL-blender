# Glossary: sRGB, or showing images outside Blender.

sRGB
A widely used display-referred color space on the Rec.709 Primaries with a D65 white point.
It applies a roughly 2.2 gamma transfer function to better suit human brightness perception.
sRGB is the norm for monitors, images, and the web, the usual choice for saving
or showing images outside Blender.

- Linear is the recommended choice for internal work like rendering and compositing.

- sRGB is typical for output images bound for screens and general distribution.

- Wide-gamut and high-dynamic-range pipelines may reach for other spaces, ACES among them, according to
the active OCIO config.

Concave Face
A face with one vertex sitting inside a triangle formed by the face's other vertices.

See also Convex and concave polygons
on Wikipedia.

Constraint
A way to control one Object using another's data.

Convex Face
A face where lines drawn from each vertex to every other vertex
all stay within the face. The opposite of a Concave Face.

Coplanar
Describing any set of elements all lying on the same 2D plane in 3D space.

Crease
An Edge property. Used to set the sharpness of edges on Subdivision Surface meshes.

Current File Asset Library
An asset library that isn't a disk directory but only mirrors the assets in
the current blend-file. It's available no matter where the
blend-file lives. See The Current File Asset Library.

Curve
An object defined by a line interpolated between Control Vertices.
Types include Bézier, NURBS and Poly.

Curve Segment
The stretch of a curve between two neighboring control points.

Cyclic
Usually meaning an object is closed/circular. The term is often paired with Curve.

Data User
An existing Blender object that uses either its own data or
data linked in (owned and managed by a different Blender object).

Data-Block
Data-blocks are the named items that form the base unit of
data in a blend file, and that can be linked into other blend files. Some
examples are objects, materials, armatures, meshes,
node-trees, and actions.

Dielectric Material
A material for real-world objects that are electrical insulators, such as plastic, wood, glass, etc.
In short, anything solid and non-metallic.

Diffuse Light
Even, directed light leaving a surface.
For most subjects, diffuse light is the main illumination we register.
It comes from a particular direction or place and produces shading.
Surfaces toward the light source read brighter,
those facing away darker.

Directional Light
Light with a specific direction but no location.
It appears to come from an infinitely far source, like the sun.
Surfaces facing it are lit more than those facing away, but their position is irrelevant.
A directional light lights every object in the scene, wherever they sit.

Displacement Mapping
A method for distorting vertices from an image or texture.
Like Bump Mapping, but acting on the mesh's real geometry.
So the mesh needs enough geometry to carry the image's detail.

[Related references](INDEX.md).
