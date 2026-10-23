# Camera View

## Camera View

The Camera view presents the scene from the active camera's vantage point. Use it to block out shots and preview the rendered look — everything inside the dashed frame ends up in the rendered image.

See also Camera Settings for how camera settings drive display and rendering.

Hint: while looking through the camera, a click on its dashed frame selects it, as long as the camera object isn't hidden.

Viewing the Active Camera - Reference: Mode: All Modes; Menu: View ‣ Cameras ‣ Active Camera, View ‣ Viewpoint ‣ Camera; Shortcut: Numpad0. Flips the view to the active camera.

Setting the Active Camera - Reference: Mode: Object Mode; Menu: View ‣ Cameras ‣ Set Active Object as Camera; Shortcut: Ctrl-Numpad0. Promotes the current active object to active camera and switches to camera view. The active camera is the one used for rendering and the one you look through when you choose camera view. You can also assign it from the Scene tab of the Properties. Note: the active camera is normally a scene-level setting, identical across all 3D Viewports, but you can also make a camera active within a single Viewport only (see Local Camera).

Animated Camera Switching: a scene starts with one camera but may hold several, and you can bind cameras to specific points on the timeline to cut between viewpoints (see Animating Cameras).

Frame Camera Bounds - Reference: Mode: All Modes; Menu: View ‣ Cameras ‣ Frame Camera Bounds; Shortcut: Home. Centers the camera view within the 3D Viewport's area and resizes it to fit the area's bounds.

Zoom Camera 1:1 — Reference: Mode: All Modes; Menu: View ‣ Navigation ‣ Zoom Camera 1:1. Zooms so the camera frame matches the output resolution exactly, letting you preview precisely how big objects will appear in the rendered image/animation.

Camera Positioning: there are several ways to place a camera, letting you align it to the viewport, navigate while driving the camera, or perform classic cinematography moves. Hint: the active "camera" can be any object serving as the scene camera, and these techniques work for positioning and aiming other objects, such as lights, too.
Align Active Camera to View: see Align Active Camera to View. This operator matches the active camera to the current 3D View, useful once you've framed a composition in the viewport and want the camera dropped exactly there.
Camera Navigation: turn on Lock Camera to View and switch to camera view (Numpad0); with this on, navigating the viewport moves the camera rather than the view. You can also toggle the lock via the navigation gizmo while in camera view. This lets you position the camera interactively with the usual navigation controls. See also Fly/Walk Navigation for first-person navigation that likewise drives the active camera.
Roll, Pan, Dolly, and Track: to make these moves the camera must be selected (so transforms target it) and you should be in camera view. Then manipulate it with the same tools you'd use on any object:
  Roll: press R to start rotation; by default it rotates about the camera's local Z axis (the one perpendicular to the camera view), which is precisely a camera "roll".
  Vertical Pan or Pitch — a rotation about the local X axis: press R, then X twice (the first press chooses the global axis, the second the local; this works for any axis — see Axis Locking).
  Horizontal Pan or Yaw: a rotation about the camera's local Y axis: press R, then Y twice.
  Dolly: hit G, then MMB (pressing Z twice does the same thing).
  Sideways Tracking: begin with G and drag the mouse (tapping X or Y twice restricts it to purely horizontal or vertical tracking).

[Related references](INDEX.md).
