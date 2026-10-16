# Color Picker

## Color Picker

### Color Picker

Circle HSV color picker.

A pop-up control for setting and tweaking color values is what the Color Picker provides. Edit any color property in Blender — materials, lights, brushes, interface themes — and it pops up.

Several color models and ways of interacting are on offer here to fit different workflows, and colors can be shown or edited in either linear or perceptual (display-referred) color spaces.

### Interface
Color Picker
Two color components at once are what the big color field lets you choose, with the pair depending on the picker type in use. A slider beside the field handles the remaining component (value or saturation, say).

How the picker looks and acts is governed by the type set in the Preferences; see Types below.

Value/Lightness
Brightness or lightness of the chosen color is what this vertical, gradient-backed slider sets. Scroll the Wheel for fine tweaks, or grab the handle and drag.

A handful of options sit under the color-picking widget; the first decides how component values get computed.

Linear :

Reports the component figures in the scene's linear working space — the one Blender keeps internally for compositing and rendering.

Perceptual :

Reports them instead in the color picking space (sRGB unless changed), the space that lines up with how the color widgets look and tends to feel more natural when you're choosing.

Which Color Model applies is what the next batch of options governs. Available choices hinge on the Color Picker Type.

RGB :

Builds a color straight from a blend of its Red, Green, and Blue parts.

HSV/HSL :

Builds a color through Hue, Saturation, and Value (or Lightness) instead — handy when you want tone and intensity dialed in separately.

Component Values
Beneath the picker, numeric fields carry the RGB or HSV/HSL components. The scale Blender uses runs from 0.0 to 1.0. Should the color carry an Alpha Channel, one more slider and field show up.

Hex
Displays or reads the color as a hexadecimal (hex) string. A shorthand form works too (FC0 standing in for FFCC00, say).

Note

Gamma correction for the sRGB Color Space is applied to hex values on their own. For more information, see Color Management.

Eyedropper
Picks up a color from any point within the Blender window via the Eyedropper.

Linear color space is how sampled colors are read, so display transforms like view or exposure adjustments are ignored. Pulling colors off overlays, reference images, or video preview regions can come out wrong, since those may render after color management transforms.

### Shortcuts

- Ctrl - LMB (drag): Snaps hue to 30° steps.

- Shift - LMB (drag): Slows the motion down for precise color tweaks.

- Wheel : Dials value or lightness.

- Backspace : Sends the current value back to its default.

### Types
How colors are shown and picked comes down to the Color Picker Type. Each type lays out hue, saturation, and value adjustment a little differently. Which one you use is purely a matter of taste and workflow.

A default picker type can be set in the Preferences under Interface Preferences.

| Circle HSV | Circle HSL | |
| --- | --- | --- |
| Square (SV + H) | Square (HS + V) | Square (HV + S) |

### Notes

- Internally, Blender operates in linear color space; it converts from sRGB or any other space on its own.

- What the picker shows is the color under the present view transform, yet the value held in storage stays linear.

- To keep output steady across renders and across display hardware, see Color Management.

[Related references](INDEX.md).
