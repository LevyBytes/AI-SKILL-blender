# Skin Modifier

## Skin Modifier

The Skin modifier turns vertices and edges into a skinned surface, using a per-vertex radius to better shape it; the output is mostly quads, with some triangles around intersections. It's a quick way to make base meshes for sculpting and/or smooth organic shapes with arbitrary topology.
Note: faces in the original geometry are ignored.

Options:
Branch Smoothing — a branch point is a vertex with three or more connected edges, which tend to produce more complicated, sometimes overlapping topology; this setting relaxes the surface around such points, with the side effect of shrinking it.
Symmetry — these checkboxes keep the output topology symmetrical on their respective axes, avoiding merging triangles across an axis unless they form a symmetric quad.
Note: they don't add geometry flipped across an axis — for that, use the Mirror modifier, typically placed above the Skin one.
Smooth Shading — output faces with smooth shading rather than flat; the input geometry's smooth/flat shading isn't preserved.
Create Armature — create an armature over the object, with each edge becoming a bone.
Note: if the root vertex has more than one adjacent edge, an extra bone is created to serve as the root.
This does the following: adds a new armature object with bones matching the input mesh and switches the active selection to it; adds weight groups to the input mesh (which the Skin modifier propagates to the output); and adds an Armature modifier directly below the Skin one — placed after Skin because it should only deform the output, since above it might change the resulting topology.
Add Skin Data — this modifier uses a custom set of data in the mesh, generated automatically the first time you add the modifier; if you remove or otherwise lose that data, this operator regenerates it.
Mark/Clear Loose — by default a branch vertex (three or more connected edges) generates extra edge loops along adjacent edges to keep the output tight; click Mark Loose to make branches loose so the output stretches between all adjacent vertices, and Clear Loose to disable that again.
Mark Root — marking a vertex as root makes it the basis for calculating rotations of connected limbs, and it also affects the armature output as the origin for root bones; each set of connected vertices should have one root (one is selected by default if you assign none), and Mark Root enforces the one-root-per-set rule, so you needn't manually unmark roots.
Equalize Radii — make the skin radii of selected vertices equal on each axis.

Skin Mesh Data: the modifier needs a specific set of data in the original mesh to work — defining each tree's root vertices, which ones are loose, and the skin size (radius) at each vertex; input vertex radii can be scaled individually in Edit Mode with Skin Resize.

Examples: a simple creature made with only the Skin and Subdivision Surface modifiers.

External Links: an early demonstration of the Skin Modifier by Nicholas Bishop (March 2011) at Blender Nation; the research this modifier is based on — Ji, Zhongping; Liu, Ligang; Wang, Yigang (2010), "B-Mesh: A Fast Modeling System for Base Meshes of 3D Articulated Shapes," Computer Graphics Forum 29(7), pp. 2169-2178 (DOI 10.1111/j.1467-8659.2010.01805.x); and a related thread on Blender Artists.

[Related references](INDEX.md).
