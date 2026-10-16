# Gizmos

## Gizmos

Gizmos let you change Geometry Nodes inputs directly in the 3D viewport, which is often more intuitive than adjusting them in the modifier or node editor.

Using Gizmos: node inputs that a gizmo can control carry an extra icon, and that node's gizmos show when it is selected; clicking the icon pins the gizmo so it shows even when the node isn't selected, and adjusting the gizmo in the viewport changes the socket's value.
Note: built-in nodes don't have their own gizmos yet, but you can build node groups that do.
Gizmos often propagate automatically when an input socket carrying a gizmo is linked — the gizmo then controls the value it propagates to, rather than the node group's input directly. Not every node supports propagating gizmos, but many math operations do, and a double link marks a successful propagation (for example, the gizmo propagated from the Size X input socket to the Value node). Gizmos can also propagate to Group Inputs, making them available on the parent group node too; and if the current group is used by a modifier directly, the gizmo is available on the modifier, where propagated gizmos always show while the modifier is active, regardless of whether any node is visible or selected.

Creating Custom Gizmos: adding custom gizmos to a node group that generates or modifies geometry can make it handier to use. To add one, use a gizmo node. The aspect that makes gizmos unintuitive at first is the bidirectional dependency: changing the gizmo position changes the controlled value, and vice versa. In the simplest setup, the Linear Gizmo node adds a gizmo drawn in the 3D viewport that controls the value plugged into it — but you'll notice the gizmo keeps jumping back to the origin even as the value changes, because the gizmo node's Position doesn't depend on the value yet. Once the gizmo position is made to depend on the value, it works more than you'd expect, now in both directions: changing the value moves the gizmo, and moving the gizmo changes the value. You can plug multiple values into a gizmo node's Value input at once, so moving the gizmo modifies them all together — use multiply or divide nodes if they should change at different rates. Join the gizmo node's Transform output into the geometry the gizmo controls, which helps Blender understand the gizmos should be transformed together with the geometry later on (for example, adding simple gizmos to the built-in Grid node).
Note: generally you can build the entire node group's functionality first and add gizmos afterward.

[Related references](INDEX.md).
