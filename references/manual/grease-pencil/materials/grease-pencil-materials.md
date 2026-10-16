# Grease Pencil Materials

## Grease Pencil Materials

### Grease Pencil Materials

Strokes are what Grease Pencil objects are made of. Any stroke can carry a stroke (outline) part, a fill part, or both, and Grease Pencil materials decide how those parts look.

A stroke points to one material data-block, and inside it the Stroke and Fill parts are set up on their own. So a stroke and its fill may run off a single shared material while still having their visual settings dialed in separately within it.

A material sets the base color, texture, and shading for both the stroke outline and the filled region.

The list always holds exactly one active material, the selected entry. New strokes you draw take that active material.

Override the base material color with the tools in Vertex Mode, or with the Draw and Tint tool over in Draw Mode.

A material stays bound to its strokes, so editing it updates every stroke that uses it on the spot.

Same stroke linked to different materials.

### Material Shader

To render stroke outlines and fills, Grease Pencil materials lean on a purpose-built shader.

Two independent sections make up the material:

Stroke
Governs how the outline looks, that is line color, thickness shading, and stroke textures.

Fill
Governs how enclosed areas look. Fill only reaches regions bounded by closed strokes, where the start and end points join up.

A checkbox in each panel header turns either part on or off independently.

Note

This is no ordinary BSDF shader. You set up the Grease Pencil shader in the Material Properties panel, and it sits apart from the Shader Editor node system.

### Setting Up Materials

Reference

Mode :

Drawing Mode

Panel :

Material ‣ Material Slots

Shortcut :

U

Just like any other Blender material, Grease Pencil materials get created and handled from the Material properties. Material assignment covers general usage.

Flip the 3D Viewport to Material Preview or Rendered shading for a live look at materials as you work.

Being data-blocks, Grease Pencil materials can be assigned across one or many objects, and a single object can mix different materials on different strokes.

A stroke's final look in Grease Pencil comes from the brush settings paired with the chosen material.

Material slots add further controls for handling and switching materials mid-draw or mid-edit.

### Properties

### Material Slots

### Surface

### Settings

[Related references](INDEX.md).
