# Menus

## Menus

Blender uses many kinds of menus to reach options and Operators. Ways to interact with a menu:
Mouse selection — LMB the item you want.
Numerical selection — use the number keys or numpad to pick an item by position; Numpad1 selects the first item, and so on.
If a menu is too tall for the screen, a small scrolling triangle appears at the top or bottom; scroll by moving the mouse past that triangle.
Shortcuts:
- Use Wheel while hovering with the mouse.
- Navigate with the arrow keys.
- Each item has an underlined character you can press to trigger it.
- Number keys or numpad also activate items (1 for the first item, 2 for the second, and so on; in larger menus Alt-1 hits the 11th, up to Alt-0 for the 20th).
- Press Return to activate the highlighted item.
- Press Esc to close without choosing anything — you can also do this by moving the cursor far from the menu, or by LMB-clicking anywhere outside it.

Popup Menus: these list Operators you run by clicking with LMB or pressing the generated shortcut shown by the operator name's underlined character; every entry shows any relevant shortcut keys, which work without opening the menu. Search any popup menu by pressing Spacebar and typing the operator name; if the menu already has "Search" as an item, you can search it without pressing Spacebar first. All of an editor's popup menus can be searched via the Menu Search feature.
Collapsing Menus: to gain horizontal space in the header, collapse the menus from the header context menu — RMB the header and uncheck the Show Menus checkbox.

Select Menus: a Select Menu (or "selector") lets you pick from a predefined list of options, appearing as a text label and/or icon with a down arrow on the right. Click LMB to open it and choose; the choice then appears inside the button. You can also cycle options without opening it by scrolling over the button with Ctrl-Wheel.
Expanded View: some select menus use an expanded layout showing every option at once, with the active one highlighted by a colored background; in some cases you can pick multiple options by holding Shift and clicking LMB.

Popover Menus: like Select Menus, but able to show more varied content such as a title, buttons, sliders, and so on.

Context Menu: a pop-up opened with RMB (in most editors the Menu key works too), whose contents depend on where the pointer is. Opened in an editor, it lists operators sensitive to that editor's mode; opened over buttons and properties, common entries include:
Single — apply the change to a single value of a set (e.g. only the X coordinate of an object's Location).
All — apply the change to all values of a set (e.g. all coordinates of an object's Location).
Reset to Default Value(s) (Backspace) — replace the current value with the default.
Copy Data Path (Shift-Ctrl-C) — copy the Python property data path relative to the data-block; useful for Python scripting.
Copy Full Data Path (Shift-Ctrl-Alt-C) — copy the full Python property data path, including any needed context information.
Copy As New Driver — create a new driver using this property as input and copy it to the clipboard; use Paste Driver to add it to another property, or Paste Driver Variables to extend an existing driver with a new input variable.
Copy To Selected — copy the property value to the selected object's corresponding property (a use case is when the Properties context is pinned).
Assign Shortcut — define a keyboard or mouse shortcut for an operation; move the cursor over the button that pops up, and when "Press a key" appears, press and/or click the desired shortcut (Esc cancels). See Keymap.
Change Shortcut — redefine the shortcut.
Remove Shortcut — unlink the existing shortcut.
Open File Location, Open Location Externally — open the containing folder using the operating system's file manager.
Online Manual (F1) — open a Blender Manual page in a web browser.
Online Python Reference — context-sensitive access to the Python API Reference.
Edit Source — for UI development: create a text data-block with the source code associated with the control (when it's based on a Python script), pointing in the Text Editor at the line where the element is defined.
Edit Translation — for UI development: point at the translation code line.

Pie Menus: a pie menu spreads its items radially around the mouse. Tip: the fastest way to use one is to hold the invoking key(s), nudge the mouse slightly toward a selection, and release the key(s) to activate it — releasing without moving keeps the menu open so you can click an item, while moving before releasing instantly activates the item nearest the mouse.

The central disc widget of a pie menu shows the current direction; the selected item highlights. Menu validity for item selection depends on the mouse touching or extending beyond this center disc.

Pie menu items support key accelerators (underlined letters) and number keys for activation.

When sub-pies are present, a plus icon indicates their availability.

[Related references](INDEX.md).
