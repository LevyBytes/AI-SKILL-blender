# bpy.ops.sculpt.mask_by_color

bpy.ops.sculpt. mask_by_color ( * , contiguous = False , invert = False , preserve_previous_mask = False , threshold = 0.35 , location = (0, 0) )

Form a mask using the present color property

Parameters :

- contiguous ( bool ) – Contiguous, Apply masking exclusively to adjoining color zones (optional)

- invert ( bool ) – Invert, Reverse the generated mask (optional)

- preserve_previous_mask ( bool ) – Preserve Previous Mask, Maintain the earlier mask and incorporate or withdraw the fresh one derived from the colors (optional)

- threshold ( float ) – Threshold, How color shifts influence the masking generation (in [0, 1], optional)

- location ( Sequence [ int ] ) – Location, Zone coordinates of sampling (array of 2 items, in [0, 32767], optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

[Related references](INDEX.md).
