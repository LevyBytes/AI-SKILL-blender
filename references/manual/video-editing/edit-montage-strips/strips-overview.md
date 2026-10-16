# Introduction

### Introduction

A strip functions as a container holding frames sourced from one or multiple inputs. It spans from a Start Frame to a defined Length and appears as a colored horizontal band in the display.

Strip schematic.

### Adding Strips

Reference

Menu: Add

Shortcut: Shift-A

The Add Menu.

The Add menu serves as the primary interface for inserting content into the Video Sequencer. Access it from the Sequencer header or by hovering over the workspace and pressing Shift-A.

Generally, the workflow involves loading video and audio media, inserting effects and transitions, and composing your edit by arranging and timing these elements. When adding content requiring external files, a file browser opens for selection, with compatible formats automatically filtered.

The Add menu also provides a Search… function, enabling rapid lookup and insertion of strips by name, matching conventions in other software.

Newly created strips begin at the playhead's current position. Adding multiple media items (videos, sounds) simultaneously places each sequentially.

### Adding Effects & Transitions

Blender includes a collection of effect strips for enhancing sequences.

To add an effect, select one source strip (video, image, or scene) by left-clicking. Some effects, like Cross transitions, need Shift-left-click on a second overlapping strip (depending on the effect type). Open the Add menu and choose your effect. The effect strip appears above the inputs. Independent effects like Color Generator position at the playhead.

Note

Most effect strips depend on one or two source strips, so their frame span and duration come from the inputs. Moving them directly may not work; adjust the input strips instead. With some effects, like Alpha Over, the selection order is significant. An effect strip can feed into another, creating layered effects.

If you select the wrong effect, use Effect Strip to swap it. Some effects like Brightness/Contrast and Hue/Saturation can be used through Strip Modifiers.

### Visualization

Strip types are assigned specific colors in the Video Sequencer display:

- Scene strip: Pale green.

- Clip strip: Navy blue.

- Mask strip: Bright red.

- Movie strip: Cyan.

- Image strip: Violet.

- Sound strip: Light blue-green.

Effect strips each have their own distinct color.

Apart from these defaults, individual strips can get custom colors via Strip Properties.

Note

Color assignment follows the active interface theme. The colors listed refer to Blender's standard theme.

[Related references](INDEX.md).
