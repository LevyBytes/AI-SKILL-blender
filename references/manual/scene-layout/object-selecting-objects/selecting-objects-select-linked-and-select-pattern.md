# Selecting Objects: Select Linked, Select Pattern

### Select Linked

Reference

Mode :

Object Mode

Menu :

Select ‣ Select Linked

Shortcut :

Shift - L

Selects all objects which share a common data-block with the active object. Select Linked uses the active object as a basis to select all others.

Object Data
Selects every object that is linked to the same Object Data, i.e. the data-block that specifies the type (mesh, curve, etc.) and the build (constitutive elements like vertices, control vertices, and where they are in space) of the object.

Material
Selects every object that is linked to the same material data-block.

Instanced Collection
Select every object that is linked to the instanced collection.

Texture
Selects every object that is linked to the same texture data-block.

Particle System
Selects all objects that use the same Particle System .

Library
Selects all objects that are in the same Library.

Library (Object Data)
Selects all objects that are in the same Library and limited to Object Data .

### Select Pattern

Reference

Mode :

Object Mode

Menu :

Select ‣ Select Pattern…

Selects all elements whose name matches a given pattern. Supported wild-cards: * matches everything, ? matches any single character, [abc] matches characters in abc , and [!abc] match any character not in abc . As an example *house* matches any name that contains house , while floor* matches any name starting with floor .

Matching can be configured to respect or ignore letter casing.

Extend
When the Extend checkbox is active, the selection expands rather than being replaced.

## Selecting Objects

This page covers the selection tools unique to the 3D Viewport; the general-purpose ones live in the Interface section.

The 3D Viewport has two keys that influence selection:
Select by Origin (Ctrl) — selects objects by their origin instead of their geometry.
Selection Menu (Alt) — when several objects sit under the pointer, pops a menu so you can pick the one you mean.
Combine the two for a selection menu based on object origins.

The mode-specific selection pages follow.
Object Mode: Object Mode.
Edit Mode: Mesh Edit Mode, Curve Edit Mode, Surface Edit Mode, Metaball Edit Mode, Text Edit Mode, Grease Pencil Edit Mode, Bone Edit Mode, Lattice Edit Mode.
Pose Mode: Pose Mode.
Particle Edit Mode: Particle Edit Mode.

[Related references](INDEX.md).
