# Sidebar

## Sidebar

Item — displays the Transform settings of the active object.

Tool — displays settings for the active tool and Workspace.

View:
View Panel — adjusts other 3D Viewport settings.
  Focal Length — sets the focal length of the 3D Viewport camera.
  Clip Start/End — sets the nearest and farthest distances at which geometry stays visible; anything closer than Start or farther than End is hidden. Note: in Orthographic view the viewport uses a negative End rather than Start. Warning: a wide clipping range lets you see both near and far objects but cuts depth precision, producing artifacts; a very large range can even make depth-buffer-dependent operations unreliable, though that varies by graphics card and drivers (see Troubleshooting Depth Buffer Glitches).
  Local Camera — lets this 3D Viewport keep its own active camera, separate from the scene-wide one; the selector beside the checkbox picks it.
  Passepartout — shows the camera passepartout while in camera view.
  Render Region — uses the Render Region; marking a region with Ctrl-B turns this on automatically. Note that while you're looking through the active camera this option does nothing — there you must instead use Output Properties ‣ Format ‣ Render Region in the Properties editor, which affects both the viewport and the final render.
  View Lock:
    Lock to Object — pick an object to become the viewpoint's point of interest, so the view orbits and zooms toward it; unavailable while looking through the active camera.
    Lock – To 3D Cursor — designates the 3D Cursor as the viewpoint's focus; available only when Lock to Object is off.
    Lock – Camera to View — while looking through a camera, glues the camera to the view so it follows along as you navigate, its frame outlined with a red dashed line.
    Lock – Rotation — blocks changes to the 3D Viewport's orientation and perspective.
    Hint: if the camera is parented to an object, you can enable Camera Parent Lock in the camera's properties so navigating the viewport moves the camera's topmost parent instead of the camera directly.
3D Cursor:
  Location — the 3D Cursor's location.
  Rotation — the 3D Cursor's rotation.
  Rotation Mode — how rotations are computed (more in the manual's appendix). Euler aligns the coordinate axes to the Euler axis, exposing the underlying discrete XYZ axes and any potential Gimbal Lock. Axis Angle uses the X, Y, Z coordinates to set a point relative to the object origin; that point and the origin define an axis, around which the W value sets the rotation. Quaternion treats X, Y, Z, and W as the Quaternion components.
Collections:
  The Collections panel lists collections and lets you control their visibility; a collection holding objects shows a circle to the left of its name.
  Local Collections — lets each viewport hold its own collection-visibility state instead of one shared globally.
  Hide in Viewport (eye icon) — toggles whether the collection is shown.
  Clicking a collection's name "isolates" it, surfacing that collection along with its ancestors and descendants while concealing the others.
Annotations — see Annotations for more.

Animation:
Global Transform.

[Related references](INDEX.md).
