# Glossary: Display Referenced, from one to the other.

Display Referenced
Describing an image whose Luminance channel is capped to a set range of values (usually 0-1).
It's called display referenced because a display can't show an infinite range of values.
So a Scene Referenced image must pass through a transfer function to convert
from one to the other.

DOF
Depth of Field
The span in front of and behind the subject that appears in focus. For any lens setting,
only one distance is precisely in focus, but focus drops off gradually to either
side of it, leaving a zone where the blur is tolerable. That zone is larger behind
the focus point than in front, because the light rays' angle changes more rapidly there;
they near parallel as distance grows.

Double Buffer
A way of rendering and showing content on the screen.
Blender uses two buffers (images) to draw the interface:
one buffer is displayed while drawing happens on the other.
When drawing finishes, the buffers swap.

DPI
Dots Per Inch
A physical measure of how many individual dots fit in a one-inch line span.

The term properly applies to printing, though it's loosely stretched to mean PPI just as often.

See also:

- Pixel Density support for image formats

- Pixel Density support for render output

Edge
A straight segment (line) joining two Vertices, which can form part of a Face.

Edge Loop
A chain of Edges along consecutive Quads.
It ends at a pole or a boundary. Otherwise it's cyclic.

Edge Ring
Every Edge running along a Face Loop whose two faces both belong to that loop.

Elastic
Objects able to snap back to their original shape
once all outside forces are removed.

Elasticity
How elastic versus inelastic a material is.

Empty
An Object with no Vertices, Edges, or Faces.

Euler
Euler Rotation
A rotation method applying rotations to each of the X, Y, Z axes in a set order.

Euler orders in Blender read most naturally backwards: XYZ Euler is like rotating
around Local Z with the Rotate tool in the 3D Viewport, then Local Y, then Local X .

F-Curve
A curve holding the animation values of one specific property.

Face
A mesh element defining a patch of surface. It's bounded by three or more Edges.

Face Loop
A chain of consecutive Quads. It stops at a Triangle or N-gon
(neither of which belongs to the loop), or at a boundary. Otherwise it's cyclic.

Face Normal
The normalized vector perpendicular to the plane a Face lies in. Each face has its own.

Fake User
A special Data User, a program construct
used to mark an object (a material, say) to be saved in a blend-file,
even when no Real User references it.
Objects used by no Data User aren't written into saved blend-files.

Field of View
The region in which objects are visible to the camera. See also Focal Length.

[Related references](INDEX.md).
