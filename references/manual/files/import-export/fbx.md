# FBX

## FBX

The FBX (Filmbox) format is widely used to move 3D data between applications, especially animated characters and complex scene data; it's supported by software like Autodesk Maya, 3ds Max, and Cinema 4D, and by game engines such as Unity and Unreal Engine. Blender's FBX importer covers a broad range of FBX features and aims to be quick, light on memory, and broadly compatible with FBX files old and new.

Import — General — Scale: how much to scale the imported objects about the world's origin.
Custom Properties — imports user properties as Custom Properties.
Enums As Strings — stores custom-property enumeration values as strings.
Geometry:
Custom Normals — imports custom normals when present (otherwise Blender computes them).
Subdivision Data — imports FBX subdivision info as Subdivision Surface Modifiers.
Vertex Colors — imports vertex color attributes. None (skip color attributes), sRGB (file's vertex colors are in sRGB Color Space), or Linear (file's vertex colors are in Linear Color Space).
Materials — Material Name Collision: what to do when an imported material's name clashes with an existing one. Make Unique (bring each material in as its own Blender material) or Reference Existing (if a material of that name already exists, point at it rather than importing).
Animation:
Offset — how far to shift animation timestamps, measured in frames.
Layered Animation Support — each FBX "take" imports as its own Action, with each animated object given its own Action Slot.
Armature — Ignore Leaf Bones: skips the last bone at the end of each chain (which marks the previous bone's length).

Export — to export FBX files, use the FBX Add-on.

[Related references](INDEX.md).
