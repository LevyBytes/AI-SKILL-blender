# Duplicate

## Duplicate

### Duplicate

Reference

Mode :

Edit and Object Modes

Menu :

Object ‣ Duplicate Objects

Shortcut :

Shift - D

Creates a visually-matching copy of the selected object(s). The copy appears at the original location, and you enter move mode automatically. Refer to the examples below.

This copy is a new object sharing some data-blocks with the original (by default, materials, textures, and F-Curves) while copying others (such as the mesh). This duplication variant is sometimes termed "shallow link," as data-blocks are partially shared.

Tip

The Preferences lets you choose which data-block types are linked or copied during duplication.

### Examples

The Cube object was duplicated.

The Cube was duplicated with Shift - D. Both cubes have separate meshes with distinct names: Cube and Cube.001.

- When the original left cube is edited, the duplicated right cube stays unchanged. Mesh data is copied, not linked.

- When one cube is edited in Object Mode, the other remains unchanged. The new object's properties and data-block are copies, not linked.

- Upon duplication, the copy inherited the original's material. Material properties are linked, not copied.

See above to create separate copies of normally-linked data-blocks.

[Related references](INDEX.md).
