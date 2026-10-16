# Grease Pencil Material Properties: Material Slots, Specials, Lock & Visibility Controls, Surface

## Grease Pencil Material Properties

### Grease Pencil Material Properties

How strokes and fills render is what Grease Pencil materials set. Each stroke points at a single material, and that material keeps separate Stroke and Fill settings inside it.

From the Material Properties panel you handle material slots, toggle visibility and locking, and dial in the look of stroke and fill shading.

### Material Slots

Grease Pencil material slots panel.

Material slots are how materials get attached to the Grease Pencil object, and every stroke keeps a reference to one of them.

Newly drawn strokes use the active material, while existing strokes hold onto their assigned material until you change it by hand.

Beside each material name sit controls for the usual visibility and editing toggles:

/ (Show/Hide in Ghosts)
Sets whether the material appears in Onion Skinning previews.

/ (Hide/Show Material)
Flips viewport visibility for strokes drawn with this material.

/ (Lock/Unlock Material)
Stops strokes using this material from being edited in Edit Mode.

### Specials

A set of operators for handling visibility and locking across many materials at once:

Show All
Make every material visible.

Hide Others
Conceal every material apart from the active one.

Lock All
Lock the whole set against editing.

Unlock All
Free the whole set for editing.

Lock Unselected
Lock any material the selected strokes do not use.

Lock Unused
Lock and conceal any material no stroke is assigned to.

Copy Material to Selected
Push the active material onto the selected Grease Pencil objects.

Copy All Materials to Selected
Push every material slot onto the selected Grease Pencil objects.

Remove Unused Slots
Clear out slots that no stroke is assigned to.

### Lock & Visibility Controls

(Isolate Material)
Lock everything else so editing is confined to the active material.

(Isolate Material)
Conceal everything else so only the active material shows.

### Surface

Shader panel with only Stroke component enabled.

The look of strokes and fills falls to the Surface panel, where each material splits into two independent components:

- Stroke – Drives how the outline renders.

- Fill – Drives how the interior of closed strokes renders.

Each component can be enabled or disabled independently.

[Related references](INDEX.md).
