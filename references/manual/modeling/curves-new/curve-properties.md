# Curve Properties

## Curve Properties

Hair Curves exhibit distinct properties in comparison to standard Curve objects, which are detailed below.

The Attributes panel holds diverse characteristics specific to hair, including strand placement and coloration. You can leverage the List View for attribute administration. For more details, consult the Attribute Reference documentation.

Hair requires an optional attachment surface: a mesh that anchors the curves and acts as a scalp for grooming operations. When you create a Curves object from the Add Menu, the selected object is automatically applied as the surface.

To assign a different surface, press Ctrl+P and choose Object (Attach Curves to Surface) from the Set Parent To popup. This option is also available in the Properties Editor under Curves settings.

The surface mesh attribute that governs curve attachment is named here. This determines which UV coordinate system on the surface each curve is anchored to.

If you modify the UV map on the surface, run Snap to Nearest Surfaces to realign the curves accordingly.

Reference

Editor: 3D Viewport
Mode: Edit Mode
Menu: Sidebar ‣ Item ‣ Curve Data

The Curve Data panel allows you to adjust settings for the active spline during editing. Options here control how the spline evaluates, appears, and is built mathematically.

The Cyclic option connects the final point back to the first, forming a closed loop when enabled or leaving it open when disabled. With the Default NURBS curve and a NURBS curve with Cyclic enabled shown side by side.

NURBS knot generation follows one of several patterns that govern how the spline parameterizes and bends:

Normal: Evenly distributed knots produce smooth curves with uniform influence from all control points.
Endpoint: Clamps the curve so the first and last control points lie on the path.
Bézier: The NURBS behaves like a Bézier, with control points functioning as Free handles.
Endpoint Bézier: Combines endpoint clamping with Bézier-like control.
Custom: You set knot values manually.

The Order setting controls the degree of the NURBS, determining how many control points affect each segment. Higher values create smoother transitions as each point influences a larger section. Lower values make curves sharper. Typical range is 2–6, contingent on control point count.

A NURBS curve with order 4 and a NURBS curve with order 2 illustrate the difference.

Resolution adjusts the number of subdivisions per segment. Increase for smoother results at the cost of computation; decrease for speed but less smoothness.

[Related references](INDEX.md).
