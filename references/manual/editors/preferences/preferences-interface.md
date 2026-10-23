# Interface

## Interface

Interface configuration changes how UI elements look and behave.

Display:
Resolution Scale: sizes fonts and buttons relative to the auto-detected DPI; in normal use you may prefer the zoom available across much of Blender's interface.
Line Width: the scale of lines and points in the interface, e.g. button outlines, plus mesh edges and vertex dots in the 3D Viewport. Thin, Default, Thick.
Splash Screen: show the Splash Screen at startup.
Developer Extras: surfaces settings and menu items aimed at developers, including Operator Search and Sequencer Cache Settings, plus these Button Context Menu entries: Online Python Reference (open the Python reference manual), Copy Python Command (copy the expression a button runs), Edit Source (edit the Python that defines the button), and Edit Translation (edit UI translations, available only with the Manage UI translations add-on enabled).
Preferences - Experimental Tab: lets you enable work-in-progress features currently under test.
Tooltips:
  User Tooltips: when on, hovering a control pops a tip explaining what's under the pointer and showing any hotkey; when off, you can still force a tip by holding Alt while hovering.
  Python Tooltips: adds a property's Python information beneath the tip.
Search – Sort by Most Recent: puts the most recently chosen items atop search results; otherwise results sort alphabetically.
Search – Show Hidden: shows data-blocks with dot-prefixed names in search menus, affecting search pop-ups and filtering data-block selectors. These names hide by default so internal or helper data-blocks aren't used by mistake (see Dot-Prefixed Names (Hidden Data)).

Editors:
Region Overlap: lets regions overlap the viewport, so the Toolbar and Sidebar draw over the main area.
Show – Corner Handles: draws small handles in each Area's corners for splitting or joining areas by click-and-drag, especially handy on touch devices where precise right-clicks or edge selection are harder.
Show – Numeric Input Arrows: on, numeric fields always show increase/decrease arrows; off, the arrows appear only on hover.
Show – Navigation Controls: shows navigation controls at the area's top-right, affecting the 3D Viewport and image spaces alike. Note: if you know the navigation shortcuts, you can switch this off.
Border Width: the padding around each editor area; a larger value widens the hit zone for area controls, improving usability on pen tablets, touch screens, or for accessibility.
Color Picker Type: which Color Space style you prefer for the Color picker shown when you LMB a color field: Circle HSV, Circle HSL, Square (SV + H), Square (HS + V), or Square (HV + S).
Header Position: the default header position for a newly opened editor. Keep Existing (top for most editor types, plus the positions saved in the start-up file) or Top/Bottom (always at the top or the bottom).
Factor Display Type: how factor values appear. Factor (floats from 0.0 to 1.0) or Percentage (0 to 100).
Temporary Editors: when certain operations open a new window, you configure their behavior here.
  Render In: when rendering, the UI can: Keep User Interface (no change; the render runs in the background), Maximize Area (a new Image editor opens as a full-screen temporary window), Image Editor (the largest on-screen area is swapped for a temporary Image editor), or New Window (a new Image editor opens as a regular-sized temporary window).
  File Browser - when opening files: Maximize Area (a new File Browser opens full-screen as a temporary window) or New Window (a regular-sized temporary window).
  Preferences: how the User Preferences editor opens: Maximize Area (a temporary full-screen editor in the current window) or New Window (a separate, regular-sized window).
Status Bar: preferences affecting the Status Bar.
  Show:
    Scene Statistics — information about the active scene's data: Collection (the active Collection's name), Active Object (the active selected object's name), Geometry (scene data by mode and object type — vertices, faces, triangles, or bones), Objects (the selected count and the total).
    Scene Duration: the playback's total time plus the current frame number and total frame count, formatted per the Timecode Style.
    System Memory: an estimate of Blender's RAM use; on a single-instance, single-machine setup it measures against the machine's hardware limit.
    Extensions Updates: how many extensions have updates available.
    Blender Version: the version number of the running Blender.

Language:
Language: the language used to translate the UI; the list is split into categories by how complete each translation is.
Translate:
  Tooltips: translates the descriptions shown when hovering UI elements.

Interface: translates all the labels across menus, buttons, and panels.
New Data: translates the names given to new data-blocks.

Accessibility:
Reduce Motion: avoids interface animations and motion effects, cutting visual distraction and easing comfort for users sensitive to motion or who prefer a static interface.

Text Rendering:
Anti-Aliasing: enables interface-text anti-aliasing; off, text is rendered straight, filling only absolute pixels.
Subpixel Anti-Aliasing: renders text for the best horizontal placement.
Hinting: adjusts font hinting, which controls the spacing and crispness of displayed text.
Interface Font: a replacement for the default UI font.
Mono-space Font: a replacement for the default mono-space UI font (it's used in the Text editor and the Python Console).

Menus:
Close Menu on Leave: closes menus when the mouse leaves the region.
Open on Mouse Over: pick this to open a menu by hovering its entry rather than clicking.
  Top Level: the delay, in 1/10 second, before a menu opens (needs Open on Mouse Over enabled).
  Sub Level: as above, but for submenus (e.g. File ‣ Open Recent).
Pie Menus:
  Animation Timeout: how long the opening animation of Pie Menus lasts.
  Tap Key Timeout: keystrokes held past this length dismiss the menu when released (measured in 1/100ths of a second).
  Recenter Timeout: the windowing system tries to hold the pie menu within the window's borders; for this span (in 1/100ths of a second) the pie uses the initial mouse position as its center, enabling fast dragged selections.
  Radius: the Pie Menu's size, given as the distance (in pixels) of the menu items from the pie's center.
  Threshold: the distance from center before a selection can be made.
  Confirm Threshold: the distance threshold past which a selection is made (zero disables it).

[Related references](INDEX.md).
