# Strip Modifiers: Color Balance Modifier, Compositor Modifier, Curves Modifier, Hue Correct Modifier, Mask Modifier, Tone Map Modifier

### Color Balance Modifier

Shift colors using Lift/Gamma/Gain or Offset/Power/Slope.

Functions like the Color Balance Node.

The chosen method applies these operations to scene colors:

Lift/Gamma/Gain

Lift
Brightens dark tones.

Gamma
Tweaks mid-brightness.

Gain
Tweaks bright tones.

Offset/Power/Slope (ASC-CDL)
For each RGB: \\(c_{out} = (c_{in}×s + o)^p\\)

Slope
Multiplier \\(s\\) shifts most color except black. Bright colors show stronger shifts.

Offset
After applying Slope, adds the Offset \\(o\\). UI shows minus 1, so default 1 means no shift.

Power
Exponent \\(p\\) , mostly affecting middle tones.

### Compositor Modifier

Compositor provides flexible effects. Switch the node context to sequencer in the compositor editor, add a tree, and use it on strips. Node trees become reusable assets.

Compositing explains further.

### Curves Modifier

Color and RGB curves.

Functions identically to the RGB Curves Node.

### Hue Correct Modifier

HSV multi-point curves.

Matches the Hue Correct Node.

### Mask Modifier

Shapes the Alpha Channel using a Mask or strip.

Mask Input Type
What kind of input defines the masking.

Strip :

Another strip's grayscale modulates alpha.

Mask :

A mask data-block modulates alpha.

Mask
The Strip or Mask to use.

Mask Time Mask Input Only
How the mask's start is timed.

Relative :

Mask offset to the strip start.

Absolute :

Mask syncs with scene time.

### Tone Map Modifier

Translates one set of hues to another to display high-range images on limited-range displays.

Matches the Tone Map Node.

[Related references](INDEX.md).
