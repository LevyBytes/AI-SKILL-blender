# freestyle

## Freestyle

Freestyle: View Map Configuration

Reference
Panel: Properties ‣ View Layer ‣ Freestyle

Each view layer has one view map governing edge detection. Freestyle toggles per-View Layer via panel header checkbox.

View Layer: Freestyle panel.

Control Mode
Select how detected edges render and how they appear:

Parameter Editor Mode:
Define Line Sets and line styles through a user interface.

A view map can include multiple Line Sets, each linked to one line style.

Python Scripting Mode:
Lines render via Python scripting: powerful yet complex.

View Map Cache
Reuse a previously computed view map for subsequent renders. Auto-updates when mesh geometry changes.

Offers major performance gains for Freestyle animation when camera-space geometry is static or when repeatedly rendering with stylization-only updates.

Though view layer-specific, cache memory is shared across all layers and scenes. Using Freestyle on multiple layers (possibly across scenes via Compositor) means one cache replaces another, negating gains.

As Render Pass
Freestyle lines do not overlay immediately. Instead, render as a Render Pass compositable with the image via Alpha Over node.

### Edge Detection

Crease Angle
When adjacent faces form an angle smaller than Crease Angle, the edge renders via Crease edge type in a line set. Affects Silhouette edge type selection.

Culling
Discard out-of-view edges. Saves processing and memory but may degrade result quality.

Face Smoothness
Incorporate Smooth Shading into edge calculations.

Sphere Radius
Impact on curvature calculation for Ridge, Valley, and Suggestive Contour edge type selection. Vertex curvature is computed by averaging surface shape within the specified radius. Higher values reduce noise and detail.

Kr Derivative Epsilon
Threshold controlling minimum curvature change rate filtering for Suggestive Contour edge type output. Higher values reduce rendered lines, starting with smoother object areas.

[Related references](INDEX.md).
