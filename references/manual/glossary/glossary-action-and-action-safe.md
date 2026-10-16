# Glossary: Action, Action Safe

### Glossary

Definitions of terms that appear throughout Blender and this manual.

Action
Where Blender stores animation data. Animatable data-blocks don't keep their own animation data; instead they hold it in actions.

Action Safe
The screen region visible on most devices. Keep content within it so nothing gets clipped.

Active
With several items selected, the last one selected is the active item. Used where the interface only shows options for a single item at a time.

See also selection states.

Aliasing
Rendering artifacts that show up as jagged lines.

Alpha Channel
An extra image channel carrying transparency.

Straight Alpha
RGBA stored as (R, G, B, A), the RGB channels left untouched by alpha.
This is the alpha type paint programs like Photoshop or Gimp use,
and the one in common formats such as PNG, BMP, or TARGA.
So image textures and web output are usually straight alpha.

Premultiplied Alpha
RGBA stored as (R × A, G × A, B × A, A),
with alpha already folded into the RGB channels.

It's the natural output of render engines: RGB stands for the light heading
toward the viewer, and alpha for how much of the background's light is blocked.
OpenEXR works in this alpha type, so intermediate render and
composite files are commonly premultiplied.

Conversion (Straight/Premultiplied) Alpha
Converting between the two isn't trivial and can lose data,
since each type can express something the other can't, though the difference is often subtle.

Straight alpha is essentially an RGB image plus a separate alpha mask.
Where that mask is fully transparent, the RGB channels can still hold color.
Convert to premultiplied and the mask is applied, so those areas turn black and the color is lost.

Premultiplied alpha, by contrast, can describe renders that both emit light
and pass background light. A transparent fire render, for instance, might emit
light yet still let through everything behind it.
Convert that to straight alpha and the effect is gone.

Channel Packed
Each color and alpha channel gets its own stored image map.
Game engines often channel-pack to save memory and speed memory access.

Ambient Light
Light arriving from the surrounding environment as a whole.

Ambient Occlusion
A measure of how much Ambient Light a surface point is likely to catch.
A point tucked under a foot or table ends up far darker
than the top of someone's head or a tabletop.

Animation
The simulation of motion.

Anti-Aliasing
The technique for reducing Aliasing, e.g. by rendering several samples per pixel.

Armature
An Object made of Bones. Used to Rig characters, props, etc.

Asset
Curated data-blocks meant for reuse, usually held in an Asset Library.
See also Asset Libraries.

Note the word "asset" has other senses too — sometimes it's used
more loosely for any "useful thing," like images, models, materials, and more.

[Related references](INDEX.md).
