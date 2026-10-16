# Curve Data

## Curve Data

Reference: 3D Viewport Editor, Edit Mode, Sidebar ‣ Item ‣ Curve Data

The Curve Data panel in Edit Mode controls the active Grease Pencil curve's behavior, affecting evaluation, display, and rendering. Cyclic: Closes the spline by connecting the final control point to the first, forming a continuous loop when enabled; remains open when disabled.

Knot Mode (NURBS): Determines knot generation along the spline, affecting parameterization and shape. Normal uses evenly spaced knots for uniform influence. Endpoint clamps the curve through first and last control points. Bézier makes NURBS resemble Bézier curves; control points act like Free handles. Endpoint Bézier combines clamping with Bézier behavior. Custom permits manual knot specification.

Order (NURBS): Defines the mathematical order, controlling how many control points influence each segment. Higher values increase point influence and smoothness. Lower values reduce influence and create sharper transitions. Typical range is 2–6, depending on point count.

Resolution (NURBS/Bézier/Catmull Rom): Subdivisions per segment. Higher resolution smooths but increases cost. Lower resolution reduces detail but improves speed.

Fill Opacity: Fill area transparency—0 is fully transparent; higher increases visibility.

Start Cap: Round adds rounded beginning. Flat ends sharply. End Cap: Round adds rounded end. Flat ends sharply.

Softness: Fill transition toward boundary smoothness. Higher creates softer edges.

U Scale: Texture coordinate scaling along length; controls material/texture repetition.

Aspect Ratio: Width-to-height scaling for material/texture effects; stretches or compresses patterns.

[Related references](INDEX.md).
