# Viewport Render

## Viewport Render

Viewport rendering turns out quick preview renders from your current vantage point, rather than from the active camera the way an ordinary render would. You can use it for both still images and animations.

Note: viewport rendering is limited to the Workbench and EEVEE engines — Cycles isn't supported.
Tip: switch overlays off to get a render free of clutter such as rigs and empties.

Settings: for the most part Viewport Render just honors the current viewport settings. A handful of settings come from the properties of whichever render engine draws the view — Solid mode uses Workbench's render settings, Material Preview mode uses EEVEE's. On top of that, several output settings apply: Resolution, Aspect, Output path, and File format.

Rendering: triggering Viewport Render renders from the currently active view. If you aren't in an active camera view, a stand-in camera is built to match the present perspective; to capture the camera's viewpoint, enter the active camera view with Numpad0. As with a normal render, Esc aborts it.
Render a Still Image — use 3D Viewport ‣ View ‣ Render Viewport Preview.
Render an Animation — use 3D Viewport ‣ View ‣ Render Playblast.
Render Keyframes — use 3D Viewport ‣ View ‣ Render Playblast on Keyframes to render only the frames where the selected objects hold an animation key. Frames without a key are still written out, but they simply repeat the last rendered frame. For example, with a six-frame animation whose selected objects are keyed on frames 3 and 5, the output runs like this: frame 1 always renders; frame 2 repeats it (no key); frame 3 renders; frame 4 repeats it; frame 5 renders; frame 6 repeats it.
Tip: you can confine the viewport render to a chosen area with Render Regions.

[Related references](INDEX.md).
