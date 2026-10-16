# Introduction

### Traditional Animation
Here is how to animate a bouncing ball the traditional 2D way using Grease Pencil.

Begin by choosing File ‣ New ‣ 2D Animation to open a fresh 2D animation template. It comes primed for a fast start: a Grease Pencil object already exists, Onion Skinning is on, Auto Keyframe is enabled, and you are in camera view.

Set the Timeline to span frames 1 through 24. On the first frame, reach for the Draw Tool and place a ball in the upper-left of the viewport — your opening extreme. Advance to frame 12 and add a squashed ball down in the centre for the breakdown, then move to frame 24 and set another extreme over in the upper-right. From there, sketch in as many of the intervening frames as you like, leaning on the onion-skin ghosts to judge spacing. Press Spacebar to play it back.

Curves and Surfaces are specialized Blender object types.
They use mathematical functions (interpolation)
rather than linear interpolation between points.

Blender supports both Bézier and NURBS.
Both are defined using "control points"
(or "control vertices") forming a "control polygon".

Blender logo made from Bézier curves. 

Both are named for their mathematics. Choosing between them depends on computation style
rather than visual outcome. Bézier curves are intuitive—they start and end at chosen points.
NURBS are more efficient to calculate with many curves.

The main benefit of curves over polygonal meshes is that curves need
less data, consuming less memory and storage. However, this procedural approach can increase render costs.

Certain techniques, like
extruding a profile along a path,
require curves. Conversely, mesh editing offers finer vertex control; if precision matters,
mesh modeling may work better.

Bézier curves are standard for typography and logo design.

They appear often in animation, as motion paths (see constraints)
and as F-Curves
to vary object properties over time.

See also

Modifiers & Constraints

- Curve Modifier

- Follow Path Constraint

- Clamp To Constraint

Metaballs are implicit surfaces, defined not by explicit vertices or control handles but as mathematical formulas evaluated in real time by the renderer.

Visually, metas produce soft, fluid, gel-like shapes with pronounced curvature. When two metas approach each other, they interact—the surfaces merge and blend together like water droplets in freefall. Moving them apart restores each to its original form.

Each metaball corresponds to an underlying mathematical structure. The Active Element panel allows switching between these underlying types at any time.

Metas serve well for special effects or as the foundation for detailed modeling. A collection of metas can establish an initial form, which is later converted to a mesh for refinement or sculpting. They are also highly efficient for ray-traced rendering.

Objects bearing meta names determine family associations and interaction rules—only metas within the same family affect each other. Transformations applied in Object Mode directly alter the resulting geometry for affected families.

In Object Mode, the computed surface displays with a black selection ring.

In Edit Mode, the meta appears as a wireframe mesh (shaded or black outline, without individual vertices) surrounded by two colored circles: red for selection (highlighted pink when chosen) and green to directly adjust the meta's stiffness value (light green when active). Outside of scaling, highlighting either circle produces the same effect.

[Related references](INDEX.md).
