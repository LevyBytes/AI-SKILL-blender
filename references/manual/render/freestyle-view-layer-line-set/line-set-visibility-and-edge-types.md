# Line Set: Visibility, Edge Types

## Line Set

Line Set: Edge and Feature Selection

Reference
Panel: Properties ‣ View Layer ‣ Freestyle Line Set

A line set selects which detected Freestyle edges render using its attached line style through various selection methods.

Freestyle Line Set panel.

Select By

Image Border
Restrict Freestyle calculation to in-view geometry. Reduces render time but increases continuity problems when geometry moves in/out of view.

### Visibility

Type
Determine visibility usage for feature edge selection.

Visible:
Only unoccluded lines render.

Hidden:
Lines occluded by at least one surface render.

Proof of concept of visible and hidden edges by LightBWK
(blend-file).

Quantitative Invisibility:
Lines occluded by a surface range render.

Start, End
Occluding surface count bounds for line rendering.

QI Range proof of concept demo, Start: 3, End: 7, by LightBWK
(blend-file).

### Edge Types

Edge type selection algorithms identify lines from geometry. Parameter editor use requires minimum one edge type for output, but multiple types combine in one line set. Press X beside types to exclude them from calculation.

Examples of some basic edge types:
Silhouette (green), Crease (black), Border (blue) and Edge Marks (red)
(blend-file by LightBWK).

Type

Silhouette
Outline closed objects by rendering where surface normals transition from camera-facing to away. Works well for organic objects (e.g., Suzanne), poorly for sharp edges (e.g., boxes). Cannot render open meshes like open cylinders and planes.

Crease
Show edges whose adjacent faces form angles sharper than the view map's Crease Angle.

Crease Angle proof of concept for 121° by LightBWK
(blend-file).

Border
Display open mesh edges: edges belonging to one face only. Open cylinders have border edges at top/bottom; planes border all around. Suzanne's eye socket is border.

Edge Mark
Render marked edges. See Edge Marks for details.

Contour
Outline each object, separating from objects behind or the background.

External Contour
Outline all objects, separating from background only, not each other.

Left pair: Contour; Right pair: External Contour.

Material Boundary
Draw where two materials meet on an object.

Suggestive Contour
Draw lines that would form the Silhouette if viewing direction shifted. Depends on view map Kr Derivative Epsilon and Sphere Radius settings.

Ridge & Valley
Mark surface crests and troughs: ridges and valleys where curvature peaks. Depends on Sphere Radius.

[Related references](INDEX.md).
