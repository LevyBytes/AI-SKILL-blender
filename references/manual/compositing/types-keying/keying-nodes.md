# Keying Nodes

## Keying Nodes

The Keying nodes give the essential tools for making a Matte for images that lack their own alpha channel — a typical case being blue- or green-screen footage where live action is shot before a colored backdrop to be replaced by a matte painting or virtual background. In general, hook them to a viewer, set the Image Editor to the Viewer node, and adjust the sliders in real time on a sample frame to dial in the settings, where small tweaks can remove artifacts or foreground degradation (taking out too much green can leave actors flat or bluish/purplish). You can and should chain these nodes, refining masking and color correction in successive passes that each build on the previous output — the Keying Node comes closest to a do-it-all green-screen node, but the best results combine techniques. Note: a Garbage Matte isn't a node but a technique — a Mask identifying content to remove that automatic processes like chroma keying can't, used either to select specific content to drop or as the inverse of a rough subject selection (removing everything else); some nodes take a garbage matte directly, and for those that don't, you can subtract the garbage matte from the node's generated matte. Simple garbage mattes come from the Box Mask or Ellipse Mask, and more complex shapes from a Double Edge Mask or a Mask.

[Related references](INDEX.md).
