# Introduction

The Texture Node Editor lets you build custom textures by combining colors, procedural patterns, and images in assorted ways — a step beyond the built-in textures, where you mostly just pick a type from a list.

Note: textures — built-in and node-based alike — are a legacy feature. For their original main job, texturing objects, they've been superseded by Materials, set up in the Shader Editor. These days Textures are used only for:
Brushes.
The Displace Modifier.
Influencing the size, density, etc. of particle systems.
Influencing where fire/smoke simulations emit.
On top of that, the Displace modifier and fire/smoke simulations don't accept node-based textures and work only with the built-in ones.

Using Texture Nodes: the default Blender layout has no workspace with the Texture Node Editor, so you open it yourself in an area of choice. Once it's open, set the empty Texture Type selector to Brush, then use the Data-Block Menu to start creating textures; note that you must switch on Use Nodes in the header before nodes can be added.

Header: see Nodes for the header items shared by all node editors.
Texture Type:
  World: deprecated; the scene's World Environment now comes from a Material instead of a Texture.
  Brush: shows brush Textures in the data-block menu; since the other two types are deprecated, this effectively shows every Texture.
  Line Style: deprecated; Line Styles for the Freestyle renderer are now defined with Materials rather than Textures.

[Related references](INDEX.md).
