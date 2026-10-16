# Introduction: Interface

### Interface

Every modifier's interface is built from the same set of basic parts, see Fig. Panel layout (Subdivision Surface as an example)..

Panel layout (Subdivision Surface as an example).

The panel header sits at the top.
Reading left to right, each icon stands for a different setting on the modifier:

/ Expand
Folds the modifier down so only its header shows and the options are hidden.

Type
An icon serving as a quick visual cue to the modifier's type.

Name
Within a single object every modifier carries its own unique name. Two on the same object can't share a name,
yet two on different objects can. The default name derives from the modifier type.

On Cage Meshes
Hinges on the prior setting; when on, you can edit the modified geometry directly
rather than the original.

Warning

Although items appear in their final, modified positions, what you edit is still the original data.

Wherever those positions drift apart the result can get confusing,
so you might prefer to switch it off in such cases.

Worth noting too: a few features ignore the cage positions, including:

- Snapping targets, vertex snapping among them.

- The transform gizmo works off the original positions.

Apply On Spline Curves Surfaces Text
Run the whole modifier stack, up to and including this one, on the control points of the curve or surface
rather than on its tessellated geometry.

Note

Out of the box, curves, texts and surfaces get turned into mesh-like geometry
before the modifier stack ever runs on them.

Edit Mode
Shows the modified geometry while in Edit Mode, alongside the original geometry you can still edit.

/ Realtime
Switches the modifier's effect on or off in the 3D Viewport.

/ Render
Switches the modifier's effect on or off in the render.

Note

Depending on the object and modifier type, the Square , Triangle and Surface icons might not show up.

[Related references](INDEX.md).
