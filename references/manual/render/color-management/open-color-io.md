# OpenColorIO

## OpenColorIO

### OpenColorIO 

Blender arrives with a standard OpenColorIO configuration that packs a handy set of display devices and view transforms.

OpenColorIO, though, is also built for a steady experience across many applications, and for that one shared configuration file can drive them all.
Blender reads the standard OCIO environment variable to load a configuration other than its own default. The OpenColorIO website spells out how to wire up such a workflow.

There is a second variable too, `BLENDER_OCIO` , which retargets the configuration for Blender alone. Where you can, favor OCIO so things stay compatible with other software and pipelines that may know nothing of `BLENDER_OCIO` . That said, configuration files now and then carry incompatibilities that make them awkward to share between applications.

### ACES 

Blender's standard configuration ships the essentials for ACES workflows: the ACEScg working space, the ACES 2.0 view transform, and OpenEXR images stored in the ACES2065-1 and ACEScg color spaces.

That handles most of what an ACES pipeline asks for. For fuller coverage, you can install the official ACES configurations by hand and select them through the OCIO environment variable.

### Roles 

scene_linear
The color space behind rendering, behind compositing, and behind every float precision image held in memory.

data
The color space set aside for data that is not color.

aces_interchange
The ACES2065-1 color space. It supplies the chromaticities the scene_linear color space derives, feeding effects like blackbody emission.

cie_xyz_d65_interchange
An intermediate display linear color space, bridging view transforms over to display color spaces.

color_picking
Shapes how colors spread across the color pickers. Expect it to run close to perceptually linear, carry the scene_linear gamut, and map 0..1 onto 0..1 in scene linear so material albedo edits behave predictably.

default_sequencer
The Sequencer's fallback color space, scene_linear where nothing is set.

default_byte
The fallback color space for byte precision images and files, texture_paint where nothing is set.

default_float
The fallback color space for float precision images and files, scene_linear where nothing is set.

### Writing Configurations for Blender 

Read to the letter, an OpenColorIO configuration omits a few things Blender relies on to run at its best.
Follow the pointers here to keep a configuration sound:

- Pair OpenColorIO v2 display_colorspaces and view_transforms with the cie_xyz_d65_interchange
intermediate display linear space. Blender draws on it to emulate the chosen display on the real one.
Lacking it, an older config switches display emulation off, leaving wide gamut and HDR display
shaky, and the colorspace metadata Blender saves for images and video hinges on it too.

- Give every display a view transform that skips tone mapping. Blender hunts for one
named Standard or Un-tone-mapped, or for the config-wide default_view_transform .
Coming up empty, it falls back to the display's first view transform. The point carries more weight
on OpenColorIO v1 configs lacking display_colorspaces , where it pins down an image's color space
once a view transform has been applied.

- Wherever you can, attach the interop ID from the Color Interop Forum
to each color space and display color space. Doing so lets image and video save
with the right colorspace information. Register the interop ID as an alias of the colorspace, and on
OpenColor 2.5 configs go further by setting the native interop_id attribute where you can.

- The icc_profile_name interchange attribute is honored, so ICC profiles can ride along when images save.

- Flag HDR displays by putting encoding: hdr-video on the matching colorspace.

- On HDR view transforms, work HDR 500 nits , HDR 1000 nits , HDR 2000 nits or HDR 4000 nits
into the name so maximum luminance for the mastering display metadata is read off automatically.

[Related references](INDEX.md).
