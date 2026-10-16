# Input

## Input

In the Input preferences you can tune how Blender responds to the mouse and keyboard, and define your own keymap.

Keyboard:
Emulate Numpad — the Numpad keys see heavy use in Blender and aren't bound to the same actions as the regular number keys; on a keyboard without a Numpad (a laptop, say), tick Emulate Numpad to have Blender treat the ordinary number keys as Numpad keys.
Default to Advanced Numeric Input — for transform mode, start in Advanced Mode rather than Simple Mode.

Mouse:
Emulate 3 Button Mouse — Blender can be set up for pointing devices lacking an MMB, with the three buttons' roles reached by holding Alt-LMB. The mouse/keyboard combinations this manual cites can be expressed as shown in the table — MMB drag, for example, becomes Alt-LMB drag.
  Warning: this option locks you out of certain features, since Alt-LMB is itself used for some operations: adjusting several items' values in one go (objects, bones, and so on), peeling edge/face rings off the selection in Edit Mode, pulling node links apart, and shifting the Compositor's background image. Some touchpads offer a three-finger tap for the middle button, which may serve as an alternative.
  Modifier — the modifier key that emulates the middle-mouse bindings; unsupported on Microsoft Windows. Alt (use the Alt key) or OSKey (use the OSKey, which avoids clashing with the existing Alt-MMB shortcuts noted above).
Continuous Grab — keeps an action like moving objects or panning from being cut short by your screen's edges, by warping the mouse within the view. Note: cursor warping works only with relative input devices (mouse, trackball, trackpad); graphics tablets generally use absolute positioning, so the feature is off while a tablet is in use. This is detected per action, so a tablet's presence won't switch Continuous Grab off for ordinary mouse-cursor input.
Release Confirms — dragging an object with LMB moves it, and confirming that (and other) transforms normally needs an LMB click; turn this on and releasing LMB does the confirming.
Double Click Speed — the time in milliseconds that triggers a double click.
Mouse Drag Threshold — how many pixels a UI element must move before Blender treats it as a drag; smaller moves register as clicks.
Tablet Drag Threshold — the drag threshold applied to tablet events.
Drag Threshold — the threshold for non-mouse/tablet events (keyboard or NDOF, say); it affects the Pie Menu on Drag keymap preference.
Motion Threshold — how many pixels the cursor must move before the move registers, helpful for tablet pens that are hard to hold still and prone to cursor stutter. Note: unlike the click/drag distinction, this catches small movements — picking selection, for example, cycles through elements near the cursor until the cursor passes this threshold, at which point cycling stops and the closest item is chosen.

Touchpad — Note: this panel appears on Windows, macOS, and on Linux under Wayland.
Multi-touch Gestures — navigate with the touchpad using multi-touch gestures rather than scroll-wheel emulation (see Configuring Peripherals for the supported gestures).
Scroll Direction — which way scrolling responds to scroll gestures; Linux/Wayland only. Traditional (gestures up scroll content down) or Natural (gestures up scroll content up).

Tablet:
Tablet API (Windows only) — choose the native Windows Ink or the older Wintab system for pressure sensitivity; Blender auto-picks the API for your OS and tablet, but you can set it by hand if there are problems (you may need to restart Blender).
Max Threshold — how much pressure is needed for full intensity.
Softness — shapes the onset of the low-pressure response via a gamma curve.

NDOF — these control how an NDOF device (3D mouse) works with the 3D Viewport, covering navigation, orbit behavior, and motion sensitivity; on supported devices the NDOFMenu button opens a pop-up to adjust them right in the viewport.
Navigation Mode — how the 3D mouse navigates the 3D Viewport. Object (feels like holding the object — moving the 3D mouse moves the object that way), Fly (sends the camera through the scene as if flying or piloting a helicopter — push the 3D mouse up and the camera climbs), Drone (a Fly-style navigation where pushing the cap forward while looking down doesn't change altitude; "Lock Horizon" is always on here).
Lock Horizon — keeps the view level, preventing horizon tilt while navigating.
Orbit Center – Auto — works out the rotation center automatically: the full model's center of volume when it's all visible, shifting to the nearest visible object when zoomed in.
Orbit Center – Selected Items — keeps the orbit center at the midpoint of whatever objects are currently selected.
Show – Orbit Axis — overlays an axis showing the current orbit rotation direction.
Show – Orbit Center — overlays a marker at the current orbit center.

Advanced:
Pan Sensitivity — how fast the view pans per NDOF input.
Orbit Sensitivity — how fast the view orbits per NDOF input.
Deadzone — the minimum threshold for motion detection, avoiding stray movement from slight touches.
Zoom Direction — which 3D-mouse direction triggers zooming. Forward/Backward (push or pull the 3D mouse forward/backward to zoom).

Up/Down — push or pull the 3D mouse upward/downward to zoom.
Invert Pan — inverts panning on the chosen X, Y, or Z axis.
Invert Rotate — inverts rotation on the chosen X, Y, or Z axis.
Pan / Zoom Camera View — while in camera view, pans or zooms the camera rather than leaving the view during orbiting.

[Related references](INDEX.md).
