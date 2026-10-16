# Fly/Walk Navigation

## Fly/Walk Navigation

The standard navigation controls can feel limiting, particularly in large environments like architectural models. There, first-person controls are often preferable: you look around while "standing" in place rather than orbiting a central point.

Blender provides two such methods, Flying and Walking. Launch either from the View ‣ Navigation menu, or start your preferred one (chosen in the Preferences) with Shift-AccentGrave.

Common uses for Fly/Walk:
Navigating — a fast way to cross a large scene.
Positioning a camera — started from a camera view (Numpad0), the camera travels with you.
Recording camera movement — capture your path by entering a camera view, turning on Auto Keying, starting playback, then activating Fly/Walk navigation; the route is stored as camera keyframes you can render. Playback can't be controlled while Fly/Walk is active, so when you finish recording you must first leave navigation with LMB before you can halt playback.

Walk Navigation — Reference: Mode: All modes; Menu: View ‣ Navigation ‣ Walk Navigation. This behaves like a typical first-person game, combining keyboard keys with mouse movement.
Usage: move the mouse toward what you want to look at and use the keys below to walk through the scene. When the view suits you, press LMB to confirm; to return to where you began, press Esc or RMB. Every one of these keys also shows up in the Status Bar as you move around, and you can tune options like mouse sensitivity and default speed in the Preferences.
W / Up — move forward.
S / Down — move backward.
A / Left — strafe left.
D / Right — strafe right.
E — move up (global); available only with Gravity off.
Q — move down (global); available only with Gravity off.
R — move up (local); available only with Gravity off.
F — move down (local); available only with Gravity off.
Spacebar — teleport to the spot under the crosshair (offset by the Camera Height value in the Preferences).
WheelUp / NumpadPlus — raise the movement speed.
WheelDown / NumpadMinus — lower the movement speed.
Shift — speed up temporarily.
Alt — slow down temporarily.
V — jump; available only with Gravity on.
Tab — toggle Gravity.
Z — straighten the view's Z axis (smoothly roll it upright rather than tilted).
Period — raise the jump height.
Comma — lower the jump height.

Fly Navigation — Reference: Mode: All modes; Menu: View ‣ Navigation ‣ Fly Navigation. On activation the cursor sits centered inside a rectangle marking a safe zone; move the cursor outside that zone and the view rotates/pans.
Usage: move the mouse beyond the safe zone toward what you want to look at. Click LMB or press Spacebar to keep the current view and leave Fly navigation; press Esc or RMB to return to where you started.
W / Up — accelerate forward.
S / Down — accelerate backward.
A / Left — accelerate left.
D / Right — accelerate right.
E — accelerate upward.
Q — accelerate downward.
MMB — drag to pan the view; flight pauses while you do.
WheelUp / NumpadPlus — increase acceleration along the current heading; with no motion, begin accelerating forward.
WheelDown / NumpadMinus — decrease acceleration along the current heading; with no motion, begin accelerating backward.
Alt — slow down while held, until the view eventually stops.
Ctrl — disable rotation while held, so view rotation doesn't steer the flight; this lets you fly past an object yet keep it centered as you move away.
X — toggle X-axis correction; when on, the view smoothly pitches toward the horizon while the cursor sits in the safe zone.
Z — toggle Z-axis correction; when on, the view smoothly rolls back to upright.

[Related references](INDEX.md).
