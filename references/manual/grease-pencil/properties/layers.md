# Layers

## Layers

Reference — Mode: All Modes; Panel: Object Data tab ‣ Layers.

Grease Pencil objects organize their strokes into a tree (the layer tree) for grouping and arranging. A stroke belongs to just one 2D layer, and the selected layer is the active layer — only one layer or group is active at a time, and new strokes you draw land on the active layer. By default the viewport draws layers top to bottom. Layers can be gathered into Layer Groups (a layer sits in only one group at a time), moved into groups by drag-and-drop, and color-coded with a color tag. Each layer maps to a channel in the Dope Sheet editor (Grease Pencil mode; see Dope Sheet), can be combined with Modifiers to affect only part of a drawing (see Modifiers), and can mask other layers via Use Mask (mask icon) or the checkbox in the Masks panel header (see Masks). Tip: when off-layers distract you in the 3D Viewport, turn on the Fade Inactive Layers overlay to dim the non-active ones.

Layer Tree — a tree view of every layer and group on the Grease Pencil object. Each layer name carries four icon buttons for common properties:
- Use Mask (mask icon) — toggle whether Masks affect the layer.
- Onion Skinning (onion skin icon) — toggle whether the layer is used for Onion Skinning.
- Hide (eye icon) — toggle the layer's visibility in viewport and render.
- Lock (padlock icon) — toggle whether the layer is editable.

Add New Layer — add a new layer to the active object.
Add New Layer Group — add a new layer group to the active object; note that groups can't be added from the Dopesheet, only from the Properties editor.
Remove Layer/Group — remove the active layer or layer group.
Layer Specials — operators for working with layers:
- Duplicate — make an exact copy of the selected layer, appending a number to its name.
- Duplicate Empty Keyframes — copy the selected layer but with empty keyframes, handy for having empty keyframes ready for the cleanup or filling process.
- Show All — make every layer in the list visible.
- Hide Others — hide every layer in the list except the active one.
- Lock All — lock editing on all the layers in the list.
- Unlock All — unlock editing on all the layers in the list.
- Autolock Inactive Layer — automatically lock every layer in the list but the active one, so you don't accidentally change others without locking them each time.
- Ignore Material Locking — allow editing strokes even when they use locked materials.
- Merge Down (Shift-Ctrl-M) — combine the selected layer with the one below, keeping the lower layer's name.
- Merge Group — combine the active layer group's layers into a single layer.
- Merge All — combine all layers into the active layer.
- Mask with Layer Above/Below — add a mask to the active layer using the layer above or below.
- Copy Layer to Selected — copy the active layer to the selected Grease Pencil object.
- Copy All Layers to Selected — copy all layers to the selected Grease Pencil object.
- Reorder Layer — move the active layer or layer group up or down in the tree.

Below the layers list sit more settings:
Blend Mode — the layer blending operation to perform (see Color Blend Modes).
Opacity — set the layer's opacity.
Lights — when enabled, the layer is affected by lights.

Masks: in Grease Pencil there are no dedicated mask layers — any layer can mask others, and the system is flexible enough for both top-to-bottom and bottom-to-top masking. Layers used as masks can use all the blend modes and opacity values of any other layer (tip: for fully transparent masking, set the mask layer's opacity to 0). Add the layer(s) that should mask the current one to the Mask list view. In the Masks list, each name carries two icon buttons:
- Invert (mask icon) — invert the mask.
- Viewport/Render Visibility (eye icon) — toggle the layer's visibility in viewport and render.

Transform — allows per-layer location, rotation, and scale transformations.

Adjustments:
Tint Color — a color that tints any material colors used in the layer.
Factor — how much tint color to apply.
Stroke Thickness — a thickness value that overrides the strokes' thickness in the layer.

Relations:
Parent — choose a Parent object to manipulate the layer; the layer inherits the parent's transformations, especially useful when rigging for cut-out animation.
Pass Index — the layer's index number, usable with some modifiers to restrict changes to certain areas (see Modifiers).
View Layer — the View Layer the Grease Pencil layer uses; left empty, the layer is included in all View Layers, useful for separating drawing parts for compositing.
Use Masks in Render — when disabled, none of the layer's masks are included in the view layer render.

Display:
Channel Color — the color used in the Dope Sheet's channel region.

[Related references](INDEX.md).
