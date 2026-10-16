# Attributes: Vertex Group: Create a Vertex Group (float, point domain).

Built-in attributes always exist and cannot be deleted. Type and domain are fixed.

| Name | Type | Domain | Notes |
| --- | --- | --- | --- |
| position | Vector | Point | Vertex or point location in object-local space. Moved by Transform Geometry Node, Set Position Node, and similar. |
| radius | Float | Point | Point cloud size marker. On curves, scales control points when converted to mesh or used in operations. |
| id | Integer | Point | Stability marker from Distribute Points on Faces, and instance motion-blur index. Expected to be high-valued, unordered. Unlike other built-ins, can be removed. Used by Random Value Node and similar for seeding. |
| material_index | Integer | Face | Material slot assignment per face. |
| sharp_edge | Boolean | Edge | Flat (vs. smooth) shading toggle for viewport and render. |
| sharp_face | Boolean | Face | Flat (vs. smooth) shading toggle for viewport and render. |
| resolution | Integer | Spline | Evaluated points between control points (NURBS and Bézier only; poly always 1). |
| cyclic | Boolean | Spline | Whether the spline connects first and last control points. |
| handle_left | Vector | Point | Left Bézier handle location (curve start side). Present only with Bézier splines. |
| handle_right | Vector | Point | Right Bézier handle location (curve end side). Present only with Bézier splines. |

These attributes do not exist by default but are expected by certain Blender functions. Type can change, unlike built-ins, but Blender may expect specific types.

| Name | Type | Domain | Notes |
| --- | --- | --- | --- |
| bevel_weight_vert | Float | Point | Bevel modifier vertex control. |
| bevel_weight_edge | Float | Edge | Bevel modifier edge control. |
| crease_edge | Float | Edge | Subdivision Surface modifier input (range 0–1). |
| crease_vert | Float | Point | Subdivision Surface modifier input (range 0–1). |
| custom_normal | 2D 16-Bit Integer Array | Face Corner | Custom Split Normals mesh support. |
| freestyle_edge | Boolean | Edge | Mesh edge mark. |
| freestyle_face | Boolean | Edge | Mesh face mark. |
| rest_position | Vector | Point | Pre-deformation point location. Auto-created before Shape Keys and Modifiers with Add Rest Position. |
| sculpt_face_set | Integer | Face | Sculpt Face Sets Feature marker. |
| sculpt_mask | Float | Point | Sculpt Masking Feature marker. |
| surface_uv_coordinate | 2D Vector | Curve | Curve anchor location on mesh surface; hair system use. |
| uv_seam | Boolean | Edge | UV island boundary marker. |
| velocity | Vector | Point | Motion-blur indicator during animation render. |

Vertex groups, UV maps, and Color Attributes are accessible as attributes. Reference them by name. Avoid name collisions (same name across categories); a collision masks one attribute. Other names are created on first use.

Geometry nodes may not always output expected types (e.g., Join Geometry may not create vertex groups). If you change a vertex group's type from Float, it ceases being a vertex group.

The Attributes panel in the property editor houses this operator, which converts an attribute's domain or data type.

Since attributes are still maturing in many Blender areas, some tools do not yet support the generic attributes (named, any domain, any type) that geometry nodes produce. This operator bridges that gap for cases requiring compatibility.

Mode:

Generic: Interpolate and convert per domain/type rules described here.
Vertex Group: Create a Vertex Group (float, point domain).

Note: This only affects original object data, not modifier results. To change procedurally generated attributes, apply modifiers first.

[Related references](INDEX.md).
