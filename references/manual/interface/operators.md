# Operators

## Operators

### Operators

The instant you trigger one, an operator carries out its action — which is what sets them apart from tools, where some kind of input is needed first. You can fire operators off from Operator Buttons, Popup Menus, or Menu Search. Adding a fresh object, deleting it, or switching its shading to smooth all count as operators.

### Operator Properties
Properties for refining the result come with most operators. The pattern is to run the operator first (it falls back on default settings), then tune the properties over in the Adjust Last Operation region.

### Modal Operators
Sitting conceptually between Tools and ordinary operators are modal operators. Interactive input of some kind is required for them.

| Esc , RMB | Cancels a modal operator. |
| --- | --- |
| Return , LMB | Confirms the action of a modal operator. |

### Slider Operators
A percentage value gets adjusted interactively in the editor's Header through slider operators.

Drag the slider left or right to set the percentage. Hold Ctrl to make it coarser (snapping in 10% increments) and Shift to make it finer. On some sliders, E toggles "overshoot," letting you push past the 0-100% range.

### Searching for Operators

### Menu Search
Reference

Mode :

All Modes

Menu :

Edit ‣ Menu Search

Shortcut :

F3

Searching Blender's interface for a given operator and running it is what the Menu Search pop-up does. Type part of the operator's name to narrow the list, then either click it with LMB or walk to it with Down and Up and fire it with Return.

Beyond the operator names, the pop-up also surfaces the menus that house them.

The Menu Search pop-up.

See also

The Spacebar Action option in the Preferences.

### Operator Search
Reference

Mode :

All Modes

Menu :

Edit ‣ Operator Search

Turn on Developer Extras and the Operator Search becomes reachable from the Edit menu in the Topbar. Every operator inside Blender falls under this search, even ones absent from any menu. Python developers find it handy for testing. Blender may also bundle a few advanced operators exposed nowhere but here.

See also

An option in the User Preferences governs how search results get scored.

[Related references](INDEX.md).
