# Bake Node

## Bake Node

Bake Node

Saves and retrieves intermediate geometries, baking portions of the node tree for performance gains. Geometry format is internal (non-interoperable except volumes, which use OpenVDB).

Important: Data compatibility between Blender versions is not guaranteed.

Inputs:
Geometry: Default bake item. Additional items via socket dragging into blank sockets or Bake Items panel. Renaming: Ctrl - LMB on socket name or Properties panel.

Bake Items:
Reference: Geometry Node Editor, Sidebar ‣ Node ‣ Bake Items

Bake Items Panel - Input/output socket management:
Bake Items List: Add, remove, rename, sort items.
Socket Type: Data (Sockets) to bake.
Attribute Domain: Field evaluation domain.
Is Attribute: Item is a stored geometry attribute.

Properties:
Note: Some properties edit only in Properties panel (Sidebar ‣ Node ‣ Properties).

Bake Mode - Frame selection:
Animation: Multiple frames. Scene range by default; Custom Range override available.
Still: Current frame only.

Bake: Execute geometry calculation and save.

Pack/Unpack: Consolidate or extract baked data. Unpacking offers options matching Unpack Resources operator.

Delete Geometry Node Bake: Remove bake data.

Bake Target - Storage location:
Inherit from Modifier: Copy modifier setting.
Packed: Embed in .blend file.
Disk: Separate directory.

Custom Path: Manual storage path.

Bake Path: Disk location. Also used for simulation zones.

Custom Range Animation: Override scene range.
Start, End: Frame boundaries.

Outputs:
For each input, a matching output acts as pass-through.
Geometry: Default bake item. Additional items via socket dragging or Bake Items panel. Renaming: Ctrl - LMB on socket name or Properties panel.

[Related references](INDEX.md).
