# Navigation

## Navigation

Orbit - Reference: Mode: All modes; Menu: View ‣ Navigation ‣ Orbit; Shortcut: MMB, Numpad2, Numpad4, Numpad6, Numpad8. Rotate around the point of interest by dragging MMB over the viewport area; RMB cancels the orbit. Alt changes orbiting in several ways: Alt-MMB on a point makes it the new point of interest the view circles; holding Alt and then dragging MMB in a direction squares the view to an axis and goes orthographic; dragging MMB and then holding Alt orbits while snapping to the world axes and the diagonals between them. To step the angle discretely, use Numpad8/Numpad2 for up/down and Numpad4/Numpad6 for left/right, and press Numpad9 to swap to the opposite side of the view (a 180° turn about the Z axis). See also the Orbit Style Preference and the Auto-Perspective Preference.

Roll - Reference: Mode: All modes; Menu: View ‣ Navigation ‣ Roll; Shortcut: Shift-Numpad4, Shift-Numpad6. Rotates the viewport camera about its viewing direction in 15° steps by default (configurable via the rotation-angle preference). To zero the roll, square the view to the global X axis with Numpad3, then orbit back to a normal perspective view; RMB cancels the roll.

Pan - Reference: Mode: All modes; Menu: View ‣ Navigation ‣ Pan; Shortcut: Shift-MMB, Ctrl-Numpad2, Ctrl-Numpad4, Ctrl-Numpad6, Ctrl-Numpad8. Slides the 3D Viewport left, right, up, or down without rotating, handy for repositioning the view while keeping its orientation:
Shift-MMB: pan freely by dragging.
Shift-WheelUp / Shift-WheelDown: pan vertically.
Shift-WheelLeft / Shift-WheelRight: pan horizontally.
Ctrl-Numpad8 / Ctrl-Numpad2: pan up/down in fixed steps.
Ctrl-Numpad4 / Ctrl-Numpad6: pan left/right in fixed steps.

Zoom In/Out - Reference: Mode: All modes; Menu: View ‣ Navigation ‣ Zoom In/Out; Shortcut: Ctrl-MMB, Wheel, NumpadPlus, NumpadMinus. Moves the view toward or away from the point of interest; zoom by rolling the Wheel or dragging Ctrl-MMB, or step discretely with NumpadPlus and NumpadMinus. Hint: if you get lost in 3D space (it happens), Frame All and Frame Selected will bring your scene's contents back into view. RMB cancels the zoom.

Zoom Region - Reference: Mode: All modes; Menu: View ‣ Navigation ‣ Zoom Region…; Shortcut: Shift-B. Drag a rectangle with LMB to mark a region and the view zooms into it; drag with MMB instead to zoom out.

Dolly View - Reference: Mode: All modes; Menu: View ‣ Navigation ‣ Dolly View…; Shortcut: Shift-Ctrl-MMB. Usually zooming is enough for a closer look, but zoom only carries you up to the point of interest and no further. When you hit that wall, Dolly instead by holding Shift-Ctrl and dragging up or down with MMB, which moves the point of interest (and the view with it); RMB cancels the dolly. Hint: dolly converts orthographic views to perspective, because moving forward/backward under an orthographic projection doesn't read as zooming, so dolly works poorly there.

Frame All - Reference: Mode: All modes; Menu: View ‣ Frame All; Shortcut: Home. Adjusts the view so every object is visible.

Frame Selected - Reference: Mode: Object, Edit, Pose; Menu: View ‣ Frame Selected; Shortcut: NumpadPeriod. Adjusts the view so the selected object(s) are visible.

Frame Last Stroke - Reference: Mode: Texture Paint, Vertex Paint, Weight Paint, Sculpt; Menu: View ‣ Frame Last Stroke; Shortcut: NumpadPeriod. Centers the view on the area of the most recent brush stroke.

Orbit & Pan:
Orbit Method: your preferred way of interactively rotating the 3D Viewport.
  Turntable: rotates while keeping the horizon level, like a potter's wheel or record player: two axes of rotation, and the world keeps a clear sense of "up" and "down." The trade-off is some lost flexibility with your objects, but you gain that orientation, which helps when you feel disoriented.
  Trackball: less restrictive, allowing any orientation.
Orbit Sensitivity: tunes how responsive and fast orbiting is, working differently per Orbit Method: under Turntable it's the rotation per pixel; under Trackball it's a simple speed factor.
Orbit Around Selection: makes the selection center the viewport's rotation center (the last selection is used when nothing is selected). How the center is found depends on mode: Object mode uses the selection's bounding-box center, Edit and Pose mode use the selected elements' center, and Paint modes use the last brush stroke's center. Note: handy as it sounds, it can be awkward for large objects like a terrain mesh, whose center isn't necessarily what you care about.
Auto – Perspective: on, the view goes Perspective when you orbit and Orthographic when you align to an axis (Top, Side, Front, Back, etc.); off, you switch by hand.
Auto – Depth: uses the depth under the mouse to improve pan, rotate, and zoom; good with Zoom To Mouse Position.
Smooth View: how long (in milliseconds) the transition animation runs when you switch views (Top/Side/Front/Camera…); set it to zero to drop the animation.
Rotation Angle: the rotation step in degrees when Numpad4, Numpad6, Numpad8, or Numpad2 rotate the 3D Viewport.

Zoom:
Zoom Method: your preferred interactive-zoom style.
  Scale: scale zooming keys off where you first click: move toward the area center to zoom out, away from it to zoom in.
  Continue: lets you control the speed (not the amount) of zoom by moving away from the initial cursor spot; up from the click point or to the right zooms out, down or left zooms in, and the further you move the faster it goes. The Vertical and Horizontal radio buttons and the Invert Zoom Direction option can change the directions.
  Dolly: works like Continue except the zoom speed stays constant.
Zoom Axis: the mouse axis used for zooming. Vertical (up zooms out, down zooms in) or Horizontal (left zooms in, right zooms out).
Zoom to Mouse Position: on, the pointer's position becomes the zoom focus instead of the 2D window center, which avoids panning when you zoom in and out a lot. Tip: pair it with Auto Depth to zoom straight to the point under the cursor.
Invert Zoom Direction – Mouse: flips which way Dolly and Continue zooming go.
Invert Zoom Direction – Wheel: inverts the mouse-wheel zoom direction.

Fly & Walk:
View Navigation: which mode interactive first-person navigation starts in by default (see Fly/Walk Navigation).
Walk:
  Reverse Mouse: inverts the mouse's Y movement.
  Mouse Sensitivity: the speed factor for looking around; higher means faster.
  Teleport Duration: the time-warp interval when teleporting in navigation mode.
  Walk Speed: the base speed for walking and flying.
  Speed Factor: the multiplier for the speed boost.
Gravity: simulates gravity while walking.
  View Height: the distance from the ground to the camera when walking.
  Jump Height: the highest a jump reaches.

[Related references](INDEX.md).
