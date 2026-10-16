# Measure

## Measure

Reference — Mode: All Modes. Tool: Toolbar ‣ Measure.

Measure is an interactive tool: you drag lines across the scene to read off distances or angles. Switching on snapping to geometry sharpens accuracy and lets you gauge things like wall thickness. You reach it from the Toolbar.

Usage — a typical workflow:
Activate Measure from the Toolbar.
Drag in the viewport to lay down the ruler's first start and end points; you can place several rulers.
Drag either endpoint to reposition the ruler.
Hold Ctrl as you move to snap onto edges and vertices.
Hold Shift as you move to measure the gap between faces — this works best with parallel faces such as walls.
You can pan, zoom, or change the projection (orthographic, perspective) at any moment for a better angle on the ruler.
Click a ruler's midpoint to convert it into a protractor; that midpoint can then be dragged like the endpoints.
Remove a selected ruler with Delete or X. To wipe out every measurement, delete the "RulerData3D" layer in the Sidebar ‣ View ‣ Annotations panel.

Every measurement vanishes once another tool is chosen and reappears when Measure is active again; even so, you can still run editing operations while a ruler is live — adjusting the selected object's rotation or scale in the Sidebar, for instance. Measurements never appear in the Render output.

Dimensions are shown using the scene's unit settings and scale, so switching the unit system (metric versus imperial), the length units (cm, m, …), or the angle units (degrees, radians) refreshes the readouts.

Tip: in Edit Mode there's also a Measurement group in the Viewport Overlays popover; its settings let the viewport show measurements for selected edges and faces on their own, with no need to place a ruler by hand.

[Related references](INDEX.md).
