# Keymap

## Keymap

On this screen you configure keyboard and mouse shortcuts. See also Keymap.

Presets — at the top you select and manage presets.
Keymap Presets — the selector offers built-in presets: Blender (the default keymap, the one this manual uses), Blender 27x (the legacy keymap from Blender 2.79 and earlier), and Industry Compatible (a keymap closer to other 3D editing apps).
Add Custom Keymap Configuration — adds a custom keymap configuration.
Remove Keymap Configuration — removes a custom keymap configuration.
Import — opens a File Browser to pick a .py file holding a custom preset.
Export — saves the current keymap configuration as a preset for others.
All Keymaps — off, only the shortcut assignments you've changed are exported (think of it as a "keymap delta"); on, the whole keymap is written.

Filtering — below the preset list you can filter the operations to quickly find one.
Filter Type — Name (filter operations by name, like New File) or Key Binding (filter by the currently assigned shortcut, like ctrl n).
Search — the text to search (blank shows every operation).

Preferences — these apply to the Blender keymap only.
Select with Mouse Button — which mouse button selects items. Left-click select is the default since it matches most software, but right-click select has workflow upsides in some cases.
  Left — LMB selects, RMB opens the context menu. Pros: familiar to users from other apps; context-menu access matches industry norms; easier transition from other 3D and design software. Cons: selection and transformation share the primary button, raising accidental movement near gizmos; placing the 3D Cursor needs a modifier (e.g. Shift-RMB).
  Right — RMB selects, LMB places the 3D Cursor. Pros: separates selection from transformation, cutting accidental edits during modeling; quick, direct 3D Cursor placement with LMB; historically tuned for precision modeling. Cons: less familiar to newcomers; the context menu needs an alternate shortcut depending on configuration.
Spacebar Action — what Spacebar does. Play (starts/stops playback, good for animation or video editing), Tools (opens the Toolbar under the cursor to swap the active tool fast, good for lots of modeling or rigging), or Search (opens Menu Search, good for newcomers unfamiliar with the menus and shortcuts — though F3 reaches search regardless). With Tools, you can pick a tool several ways: press Spacebar then click one; hold Spacebar, move to a tool, and release; press Spacebar then the key shown in the popover (e.g. T for Transform); or press Spacebar and the tool's key together (e.g. Spacebar-T for Transform). If you pick something other than Play, Shift-Spacebar starts/stops playback instead.
Activate Gizmo Event — the event that activates drag-capable gizmos; available only when Select with Mouse Button is Left. Press (the gizmo's operation starts, with extra options in the Status Bar, the moment you press the mouse button on it) or Drag (it starts only once you begin dragging).
Tool Keys — how tool-activation shortcuts behave. Immediate (the tool is in use at once — press Ctrl-B while editing a mesh and a Bevel starts straight away, mouse to size it, LMB to confirm) or Active Tool (the tool is merely selected, as if clicked in the Toolbar — press Ctrl-B and the Bevel tool is selected with its gizmo visible, and you drag the gizmo to bevel).
Alt Click Tool Prompt — tapping Alt shows a status-bar prompt for a second keystroke to activate the tool; unavailable with Emulate 3 Button Mouse.
Alt Tool Access — holding Alt lets you use the Active Tool where the gizmo would normally be needed (with the Move tool selected, say, hold Alt and drag anywhere in the viewport to move the selection rather than dragging its gizmo); available only when Select with Mouse Button is Left and Emulate 3 Button Mouse is off.
Select All Toggles — makes the Select All shortcut A deselect all whenever a selection exists.
Region Toggle Pie — with this on, N raises a pie menu for toggling Regions instead of always toggling just the Sidebar.

3D Viewport:
Grave Accent / Tilde Action — Navigate (a Viewpoint pie menu, handy without a numeric keypad) or Gizmos (a Transform-gizmos pie menu for switching gizmos fast; it doesn't apply to tools that force a gizmo — Move, Rotate, Scale, Transform — where the gizmo stays put whatever you pick).
Middle Mouse Action — what MMB dragging does in the viewport (trackpads too). Orbit (orbits the view around a central point, with Shift-MMB for panning).

Pan — pans the view, with Shift-MMB for orbiting.
Alt Middle Mouse Drag Action — how the new viewpoint is decided when dragging Alt-MMB. Relative (the result depends on both the mouse direction and the current viewpoint — dragging horizontally rotates 90° around the view's current vertical axis) or Absolute (the result depends only on the mouse direction — drag right and you always end up looking from the positive side of the global X axis).
Tab for Pie Menu — normally Tab toggles Edit Mode while Ctrl-Tab opens a pie menu of all modes; this option swaps the two shortcuts.
Pie Menu on Drag — when on, certain keys act differently when tapped versus held-and-dragged (which shows a pie menu):
  Tab — Tap: toggle Edit Mode. Drag: show the Object Mode pie menu.
  Z — Tap: toggle wireframe view. Drag: show the Viewport Shading pie menu.
  AccentGrave — Tap: start first-person Fly/Walk Navigation. Drag: show the viewpoint pie menu.
Extra Shading Pie Menu Items — adds more items to the shading menu (Z key).
Transform Navigation with Alt — requires holding Alt to navigate the view while transforming something, in exchange for not needing Alt for certain other operations. For example, with it off, MMB drag always orbits and Alt-MMB locks movement to an axis while moving an object; with it on, those invert while moving — MMB does the axis lock, and you use Alt-MMB to orbit, Shift-Alt-MMB to pan, and Alt-Wheel to zoom. It also applies to Proportional Editing (where Wheel sizes the influence area) and Auto IK (where Wheel sets the temporary IK chain's length): with it off, Wheel zooms the view and you use Alt-Wheel to change those. See also Transform Modal Map.
File Browser:
  Open Folders on Single Click — enter folders with one click rather than two.

Editor — the Keymap editor is where you reassign the default hotkeys for every one of Blender's editors.
Usage: find the operation whose shortcut you want to change (filtering helps); decide whether a keyboard key, a mouse button, or some other input should trigger it; then click the button at the right and press the shortcut you want.
Active — uncheck to disable this keymap item.
Map Type — Keyboard (a single hotkey or combination), Mouse (mouse-button, tablet, or touchpad input), NDOF (movement or a button from a 3D-mouse device), Tweak (mouse click-and-drag, optionally mapping drag direction to different actions), Text Input (used by entering text), or Timer (for Blender's internal use).
Operator ID Name — the identifier of the operator to call. Hint: see bpy.ops for the operator list (drop the bpy. prefix for the identifier).
Event:
  Type — the key or button that fires this item (per the map type).
  Value — the action (press, release, click, drag, etc.; per the map type).
  Modifier — extra keys to hold (Ctrl, Shift, Alt).
  Operator Properties — starting values for the operator's own properties.
See also Keymap Customization.
Restoring — to restore a keymap's defaults, click the Restore button at its top-right. Tip: rather than editing the default keymap, you can add a new one.

Known Limitations — Blender Versions: the trouble with editing your own keymap is that newer Blender versions may change how tools are reached, breaking your customizations. The keymap can be updated by hand, but the more you've changed, the likelier conflicts become in newer versions.

[Related references](INDEX.md).
