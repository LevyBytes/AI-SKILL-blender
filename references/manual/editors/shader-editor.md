# Shader Editor

## Shader Editor

The Shader Editor is where you build the materials used for rendering. Materials for Cycles and EEVEE are defined by a node tree, so the editor's main window is a node editor. A full list of shader nodes lives in the rendering section.

Header:
Shader Type: the kind of data whose shader nodes you're editing: Object (the active object's Material), World (the World background), or Line Style (Freestyle Line Styles).
Use Nodes (Line Style): use shader nodes to define the freestyle line style's texture.
Slot: the Slot menu selects the active material slot on the active object, and the material selector beside it swaps which material sits in that slot.
/ Pinned — keeps the current material visible in the Shader editor even when another object or material is selected elsewhere.

Sidebar - Options: the Sidebar's Options panel carries the same settings found in the Properties' Material tab (they vary by render engine); they're duplicated so you can edit the whole material from the Shader editor.

[Related references](INDEX.md).
