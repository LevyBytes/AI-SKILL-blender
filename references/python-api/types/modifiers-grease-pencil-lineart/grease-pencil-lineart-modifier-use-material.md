# bpy.types.GreasePencilLineartModifier: use_material, use_material_mask, use_material_mask_bits, use_material_mask_match

use_material

Build strokes from the borders between materials (default False)

Type :

bool
use_material_mask

Apply material masks to drop occluded strokes (default False)

Type :

bool
use_material_mask_bits

Mask bits to match from Material Line Art settings (array of 8 items, default (False, False, False, False, False, False, False, False))

Type :

bpy_prop_array[bool]
use_material_mask_match

Demand that every material mask match instead of only one (default False)

Type :

bool

[Related references](INDEX.md).
