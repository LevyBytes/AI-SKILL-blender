# Screw: Usage

## Screw

### Screw 

Reference

Mode :

Edit Mode

Menu :

Edge ‣ Screw

This operator sweeps geometry along a helical path — handy for modeling screws, springs,
sea shells and the like.

It overlaps with the Screw Modifier, but several distinctions matter:

| Screw operator | Screw modifier |
| --- | --- |
| Works in world space. | Works in object space. |
| Extrudes only the selected geometry. | Extrudes all geometry. |
| The centerpoint can be specified manually. | The centerpoint is always the object's origin. |
| One revolution is always 360°. | The angle can be chosen freely. |
| The height offset of each revolution is calculated automatically based on the geometry. | The height offset must be specified manually. |
| Each revolution can also have a radial offset away from/towards the central axis (again determined by the geometry). | The radius stays constant. |

Per the table, both the per-revolution height and radial offset are worked out for you by the
operator. It derives them from the ends of an open profile — a string of joined edges that never
closes into a loop. Extrusion stacks the turns so that one revolution's top vertex meets the
following revolution's bottom vertex.

Sweeping such an open profile is the usual job, but it isn't the only one. Provided the selection
holds exactly one open profile — even a lone stray edge — you may also sweep closed profiles or
geometry that already carries faces.

A few examples follow.

| Description | Description |
| --- | --- |
| Wood Screw.  | Spring.  |

### Usage 

Begin by ensuring your mesh contains an open profile. To sweep something else (a circle or two,
say), add an open profile beside it.

With that ready, drop into Edit Mode and select the geometry to sweep, taking care to include
precisely one open profile. Too few or too many and the operator aborts with the error
"You have to select a string of connected vertices too."

Position the 3D Cursor at the point you want the geometry to revolve around. Confirm as well that
your screen's vertical axis lines up with the spin axis. Revolving around the global Z axis is
the typical case: for that, drop the 3D Cursor at the world origin and switch to an orthographic
side view.

You're set to run it now: open the Edge menu — click it in the 3D Viewport header or press
Ctrl - E: and pick Screw .

The step and turn counts can be changed afterward in the Adjust Last Operation panel.

If the open profile was only there to steer the sweep and you don't want its geometry, hover one
of its extruded faces, press L to grab them, and clear them with X or Delete .

[Related references](INDEX.md).
