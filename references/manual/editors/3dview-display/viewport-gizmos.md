# Viewport Gizmos

## Viewport Gizmos

Reference — Mode: All Modes. Location: Header ‣ Gizmos.

Clicking Show Gizmos toggles every gizmo in the 3D Viewport, while the adjacent drop-down opens a popover of finer settings, covered below.

Viewport Gizmos:
Navigate — turns the navigation gizmo on or off.
Active Tool — turns the active tool's gizmo on or off.
Active Object — turns the Object Gizmos on or off for the active element (see below).

Object Gizmos let you translate, rotate, and scale interactively with the mouse in the 3D Viewport. They're labeled "object" gizmos in the popover, but they also serve other transformable items such as mesh vertices. Each operation gets its own gizmo, usable on its own or alongside the others. Every gizmo carries three color-coded axes — X (red), Y (green), Z (blue) — and dragging an axis with LMB transforms along it; the Move and Scale gizmos add small colored squares that transform along two axes simultaneously.

Several modifier keys apply:
Holding Ctrl at any moment toggles snapping and also makes rotation and scaling jump in coarse steps.
Holding Shift after the LMB press does the reverse — it "slows" the transform relative to mouse motion for finer control.
Holding Shift before the LMB press constrains the transform to the plane perpendicular to the axis you clicked (see Plane Locking).

The Gizmos popover exposes these object-gizmo settings:
Orientation — the orientation the gizmo uses; Default adopts the viewport's Transform Orientation, while the remaining choices override it.
Move — shows the location gizmo; dragging its small white circle frees movement within the viewing plane.
Rotate — shows the rotation gizmo; dragging the large white circle rotates about the viewing direction, and dragging the faint white disc inside it (visible only on hover) gives trackball rotation.
Scale — shows the scale gizmo; dragging the band between the small and large white circles scales on all three axes at once.
Those last three also appear in a pie menu if the Grave Accent / Tilde Action in your Keymap Preferences is set to Gizmos.
Note: if you're on a tool bound to its own gizmo setup (Move, Rotate, Scale, or Transform), the Move/Rotate/Scale checkboxes do nothing.
See also the Gizmo Preferences.

Empty — gizmo settings for empties: Image (a gizmo for adjusting the image's size and position) and Force Field (a gizmo for tuning the force field).

Light — gizmo settings for lights: Size (adjusts a spotlight's Spot Size) and Look At (adjusts a light's direction).

Camera — gizmo settings for cameras: Lens (adjusts focal length for Perspective cameras or orthographic scale for Orthographic ones) and Focus Distance (a gizmo for the focus distance; to see it, enable Viewport Display ‣ Limits in the camera's properties).

[Related references](INDEX.md).
