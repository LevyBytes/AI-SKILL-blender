# Brushes: Brush Assets, Pixel Art Brushes

Smear
Brushes: Smear

Gathers colors from beneath the cursor and mixes them along your brush motion. Comparable to the "smudge" capability in Gimp.

Clone
Brushes: Clone

Transfers pigmentation from a reference location to the active surface.

In 3D painting, set the clone source with Ctrl - LMB. In 2D mode, reposition by dragging with RMB.

Clone from Paint Slot (3D projective only)
Select a reference image instead of using the 3D reference position in the current image.

Source Clone Slot
Designate an image as the clone reference.

Image (2D only)
The reference image for cloning.

Alpha (2D only)
Transparency level of the clone image display.

Fill
Brushes: Fill

Fills sizable regions with a chosen color. Adjacent pixels resembling the clicked color receive application.

Fill Threshold (2D only)
Sets the color similarity needed for a pixel to receive the fill. Low values match only very comparable hues. Higher thresholds encompass a wider spectrum.

Gradient option via the Color Picker allows gradient filling.

Apply gradient using the Fill brush by pressing LMB and dragging to mark the gradient line, or radius for radial gradients (depending on Gradient Fill Mode).

Gradient Fill Mode
Linear, Radial

Note

Overrides

For 3D painting, certain choices bypass standard options to apply color to the mesh. This means hidden, rear-facing, and unculled faces always receive application, regardless of settings.

Mask
Brushes: Mask

Deposits grayscale values on the designated mask texture channel. Any masked regions resist other paint brush application, similar to sculpt masking.

Mask Value
The strength of the mask, where zero = unmasked and one = completely masked. Press Ctrl to reverse the value.

Tip

Simpler alternative is face selection masking. Consult Face Selection Masking for information.

### Brush Assets

### Pixel Art Brushes

Paint Pixel Art
Brush Type: Draw

Deposits specified pixels (Image Editor only).

Erase Pixel Art
Brush Type: Draw

Clears pixels in the transparency channel (Image Editor only).

[Related references](INDEX.md).
