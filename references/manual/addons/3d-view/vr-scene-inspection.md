# VR Scene Inspection

## VR Scene Inspection

VR Scene Inspection is a bundled (GPL) add-on that surfaces — and modestly extends — Blender's built-in virtual-reality support inside the UI; its scope is deliberately narrow (inspecting a scene), and going further generally means extending it in code. The underlying tech is the OpenXR specification, which needs the setup described under Head-Mounted Displays (HMD). Every control sits under 3D Viewport ▸ Sidebar ▸ VR tab.

VR Session: "Start VR Session" tries to reach the OpenXR runtime and share the viewport with a headset. Two tracking switches apply — Positional (turn it off to track only head rotation, leaving the viewer's location fixed) and Absolute (which drops the eye offsets that otherwise snap the viewer onto a landmark, so the origin can be set independently of the headset). "Use Controller Actions" turns on the stock bindings for haptics, controller tracking, and navigating the viewport.

View: a set of Show switches decide what appears inside the headset — the ground Floor, Annotations strokes, Selection outlines, the motion Controllers (needs Use Controller Actions), Custom Overlays (operator drawing such as the teleport beam), and Object Extras (empties, lights, cameras). Alongside them: an object-type visibility filter, a Controller Style, Clip Start/End (same idea as the viewport's clipping), and Fly Speed for free-flying.

Landmarks save reusable viewer base poses (a position with a rotation); for the Custom Object and Custom Pose types you can also set a base reference scale. The Landmark List drives which landmark's settings show beneath it, and merely changing the selection leaves the VR view untouched. Actions include: Activate (make a landmark the VR view's base pose), Add, Remove, and "Add from Session" (build one from the running session's viewer pose). More helpers cover making a camera plus landmark from the session, deriving a landmark from the active camera, refreshing a custom landmark from where the viewer currently is, snapping the 3D cursor onto a landmark, placing the scene camera there, or spawning a fresh camera from it. A landmark's Type is one of: Scene Camera (track whatever camera is active), Custom Object (any chosen object sets the pose), or Custom Pose (you key in the position and rotation by hand).

Action Maps: a gamepad (for instance a Microsoft Xbox Controller) can stand in for the motion controllers when issuing VR actions like navigation. Binding Extensions add per-device mappings — among them HP Reverb G2, HTC Vive Cosmos, HTC Vive Focus 3, and Huawei controllers — though support varies by platform.

Viewport Feedback: optionally draw, in the ordinary 3D Viewport, a marker for the live VR viewer pose (its place and orientation), markers for the tracked controllers (again gated on Use Controller Actions), and landmark markers; "Mirror VR Session" makes the viewport mimic the headset's view.

Preferences (under Preferences ▸ Navigation ▸ VR Navigation, visible only with the add-on on): Vignette Intensity dials the movement vignette's strength; Turn Speed governs rotation rate while turning continuously; Turn Amount fixes the per-step angle for snap turning; Snap Turn flips between continuous and stepped turning; and Invert Rotation flips the rotation controls. For reference, its category is 3D View, and it lets you view the viewport through VR head-mounted displays at 3D Viewport ▸ Sidebar ▸ VR tab.

[Related references](INDEX.md).
