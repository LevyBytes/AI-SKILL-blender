# Passes: Shader AOV, Light Groups, Light Group Sync, Combining, Cycles, EEVEE, EEVEE Limitations

### Shader AOV

Shader AOVs (Arbitrary Output Variables) comprise user-designed visual data containers for composition purposes. Build a pass in the Shader AOV area,
send to it from a material using the AOV Output Node,
and subsequently retrieve in the Compositor utilizing the socket on the Render Layers node.

Name
The tag for the output channel. Used in both the AOV Output node and the
Render Layers node. The designation can be arbitrary provided it avoids
clashing with other (operational) options.

Data Type
The storage category for the output per location.
Choose Color for hue, direction, or additional vector information.
Pick Value for single-number information.

### Light Groups

Cycles only

A Light Group creates a restricted Combined pass rendering illumination from
designated lights only. These individual passes can then get joined in composition to assemble the final product
with complete illumination. The basic technique involves combining them with
the Mix Color Node, though more intricate assemblies
enable tuning hue and brightness of distinct lights absent re-rendering.

To link a Light item to a new or existing Light Group, locate the panel
Object ‣ Shading ‣ Light Group (specifics).

To link the World backdrop to a Light Group, locate the panel
World ‣ Settings ‣ Light Group (specifics).

Name
The label of the light grouping.

### Light Group Sync

These operations appear via the
Light Group catalog selector.

Add Used Lightgroups
Build Light Groups for any lights mentioning a non-existent group.

Remove Unused Lightgroups
Erase any Light Groups which no lights employ.

### Combining

### Cycles

The individual output stages get assembled to yield the complete result as:

### EEVEE

The stages can get merged to yield the complete result as:

### EEVEE Limitations

- Depth of Field and Motion Blur
stay unrendered in outputs apart from Combined .
You can create them in the Compositor using the Defocus Node
plus the Vector Blur Node.

- See-through materials configured with Blended Render Method get left unrendered in outputs apart from Combined and Transparent .
Switch to the Dithered alternative instead.

- The Shader To RGB Node produces right results
in the Combined option only as EEVEE leaves parts of the BSDF equation unprocessed.

- A cap of 16 Color plus 16 Value AOVs (custom outputs) exists.

[Related references](INDEX.md).
