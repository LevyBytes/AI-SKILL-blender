# Glossary: MIP, Mip-map

MIP
Mip-map
Mip-mapping
'MIP' stands for the Latin 'multum in parvo' — 'much in little'.
A mip-map is a chain of ever-lower-resolution copies of an image,
usually halved via squared interpolation using Anti-Aliasing.
Mip-mapping is the process of computing those lower resolutions of
the same image, cutting memory use to speed display but raising
memory use for calculation and allocation. Mip-mapping is also
used to make small anti-aliased samples of an image for texturing.
The math runs on CPUs, but modern graphic processors
can be chosen for the task and are far faster.

MIS
Multiple Importance Sampling
Gauging which way light rays travel so as to sample more efficiently.

See Multiple Importance Sampling and
also Importance sampling on Wikipedia.

Modifiers
A non-destructive operation applied on top of some data.

Motion Blur
What we perceive with a rapidly moving object.
It looks blurred thanks to our persistence of vision.
Simulating motion blur makes computer animation feel more realistic.

Multisampling
Rendering several samples per pixel, for Anti-Aliasing.

N-gon
A Face containing more than four Vertices.

NDOF
3D Mouse
A general term for a 3D mouse, or any input device that supports
more degrees of freedom than a conventional 2D one, see: Touchpad.

Non-manifold
Non-manifold meshes essentially describe geometry that couldn't exist in the real world.
Such geometry is unsuited to several kinds of operation,
especially those that need a clear inside/outside
(refraction, fluids, Boolean operations, or 3D printing, among others).
In such a mesh, a non-overlapping surface (from its connected faces)
won't settle a volume's inside or outside from its normals, defining
a single surface for both sides but ending with flipped normals.
For non-closed volumes, a non-manifold mesh always
has at least one break in normal direction, either
from an inverted connected loop or from an odd number of surfaces.
Such a mesh always works out to an odd surface count.

Non-manifold geometry comes in several forms:

- Some borders and holes (edges with only one connected face), since faces have no thickness.

- Edges and vertices belonging to no face (wire).

- Edges joined to three or more faces (interior faces).

- Vertices on faces that don't adjoin (e.g. two cones sharing the apex vertex).

See also: Select Non-Manifold tool.

Nonlinear Animation
An animation technique letting the animator edit motions as wholes,
not just individual keys. It lets you combine,
mix, and blend different motions into wholly new animations.

Normal
The unit vector standing perpendicular to a surface.

Normals can be attached to vertices and
faces and varied across a surface via Normal Mapping.

See also Normals on Wikipedia.

Normal Mapping
Like Bump Mapping, but instead of a grayscale heightmap
the image's colors say which direction the normal should shift,
the three color channels nudging the normal along X, Y, or Z.
That buys more detail and finer control.

[Related references](INDEX.md).
