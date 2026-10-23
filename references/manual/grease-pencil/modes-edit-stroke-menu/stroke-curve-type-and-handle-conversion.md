# Stroke Menu: **Set Curve Type.**, Handles - includes handle information during conversion.

**Set Curve Type.**

Menu ‣ Stroke ‣ Set Curve Type; shortcut V. Sets the spline type for stroke splines in the selection.

Type: target spline type; see Spline Types for details:
- Bézier: converts the spline to Bézier type. Poly splines convert with vector handles; NURBS or Catmull Rom with automatic handles.
  Note: converting a NURBS spline to Bézier requires at least six points; if the count is not a multiple of three, the spline truncates.
- NURBS: converts to NURBS type.
- Poly: converts to poly type.
- Catmull Rom: converts to Catmull Rom type.

Handles: includes handle information during conversion.

**Set Resolution.**

Menu ‣ Stroke ‣ Set Resolution. Controls the number of points interpolated along each curve segment (between two handles).

**Set Stroke Type.**

Menu ‣ Stroke ‣ Set Stroke Type. Converts selected curves to a different component type.

Type:
- Stroke: retains outlines only; removes any fill.
- Fill: keeps fill areas only; discards the outline.
- Both: activates both outline and fill simultaneously.

**Reset UVs.**

Menu ‣ Stroke ‣ Reset UVs. Resets the UV transformation of selected curves to default values, removing any scaling, rotation, or offset adjustments applied to material coordinates.

**Join Fills.**

Menu ‣ Stroke ‣ Join Fills; shortcut Shift+J. Combines multiple selected fill regions into one; helpful for unifying separate bounded areas.

**Separate Fills.**

Menu ‣ Stroke ‣ Separate Fills; shortcut Alt+P. Divides a unified fill region back into separate fills per boundary curve, enabling independent editing of formerly merged areas.

Individual: creates a separate fill for each individual stroke.

[Related references](INDEX.md).
