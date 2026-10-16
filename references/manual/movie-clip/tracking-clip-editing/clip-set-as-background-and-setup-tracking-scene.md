# Clip: Set as Background, Setup Tracking Scene

### Set as Background

Reference

Mode :

Tracking

Menu :

Clip ‣ Set as Background

Makes the clip you're editing the camera background across every visible 3D Viewport.
Nothing happens if no 3D Viewport is visible or the Clip Editor is running full screen.

### Setup Tracking Scene

Reference

Mode :

Tracking

Menu :

Clip ‣ Setup Tracking Scene

Runs through the usual steps for getting a scene ready for match moving and compositing automatically.

It sketches out a bare-bones VFX workflow by:

- Dropping in reference objects — a floor plus a stand-in cube — so you can confirm the track holds up.

- Adding a camera object and wiring it to follow the motion that was tracked.

- Building a compositor node tree that lays the rendered 3D scene over the background plate.

The end result hands you a launch pad for placing 3D objects into live footage.

Tip

- Lean on the generated floor reference to seat 3D objects on the footage's ground plane.

- Swap out the stand-in cube, or keep it around to sanity-check that the tracked motion lines up.

- Push the compositor setup further with masks, color grading, or whatever extra effects you need.

Note

Treat this operator as a convenience shortcut.
Heavier VFX work may still call for a hand-built compositor node setup or manual scene tweaks.

[Related references](INDEX.md).
