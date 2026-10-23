# Introduction

The Movie Clip Editor handles tracking and masking of movies.

Header - Mode:
Tracking: for dropping markers onto a video and following their motion.
Mask: for creating masks and animating them.

View Type:
Clip: the standard view, where you place and track markers.
Graph: charts the markers' movement speed on a graph.
Dope Sheet: gives a timeline overview of marker keyframes.

View Menu:
Toolbar (T): shows or hides the left-hand tab panel for creating and working with markers and masks.
Sidebar (N): shows or hides the Sidebar.
Adjust Last Operation: opens a pop-up panel for changing the properties of the operation you just finished.
Show Metadata: displays any metadata baked into the video, if present.
Frame All (Home): zooms and pans so the whole video fits in view.
Frame Selected (NumpadPeriod): zooms and pans to center the selected items.
Center View to Cursor (Mask Mode): pans so the 2D Cursor sits at the center.
Zoom: a menu of handy zoom levels and operations, the levels figured from the image resolution against the screen resolution: 12.5% (1:8) Numpad8 zooms out to 12.5%; 25% (1:4) Numpad4 to 25%; 50% (1:2) Numpad2 to 50%; 100% (1:1) Numpad1 resets to 100%; 200% (2:1) Ctrl-Numpad2 zooms in to 200%; 400% (4:1) Ctrl-Numpad4 to 400%; 800% (8:1) Ctrl-Numpad8 to 800%.
Zoom In/Out (Wheel): zooms in or out.
Zoom to Fit (F): behaves like Frame All but grabs as much editor space as possible.
Area: area controls; see the user-interface documentation.

Select Menu: for selecting markers and masks.
Clip Menu: for loading movie clips and building proxies.
Track Menu: for running tracking operations.
Reconstruction Menu: for setting up the reconstruction of 3D information from the points tracked in the 2D video.
Add Menu - adds primitive mask shapes: Circle adds a circular mask, Square a square one.
Mask Menu: operators for editing masks.

Other:
Clip: a data-block menu for loading and choosing movies; both video files and image sequences work, and loading a clip adds extra panels to the interface.
Pivot Point: see Pivot Points.
Proportional Editing (Mask Mode): see Proportional Editing.
Mask (Mask Mode): a data-block menu for creating and choosing masks.
Mask Display (Mask Mode): see Mask Display.
Toggle Lock Selection (L): keeps the view panning to follow the selected markers, so they hold the same on-screen spot during tracking and playback. This "locks the view onto the selection" and shouldn't be confused with the Sidebar's Lock option, which instead stops you changing the active marker.
Clip Display: see Clip Display.
Gizmos: see Viewport Gizmos.

[Related references](INDEX.md).
