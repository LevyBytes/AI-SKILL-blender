# Compositor

## Compositor

The Compositor is where you wire up nodes for compositing; its use is covered in Compositing.

Interface — Header:
Node Tree — selects which node group (compositor node tree) to show and edit. Each Scene can hold its own compositor node tree, and you can also make and switch to custom node groups for reuse.
Pinned — when on, the editor sticks with the chosen node tree no matter which scene is active, handy when juggling several scenes but wanting the compositor fixed on one tree.

Gizmos — controls gizmo display in the Compositor. Clicking Show Gizmos turns every gizmo in the Compositor on or off, and the drop-down opens a popover of finer settings below.
Viewport Gizmos:
  Active Node — shows a context-sensitive gizmo for whichever node is selected, which might include transform handles or other visual aids depending on the node type.

Asset Shelf — offers quick access to compositor node assets, letting you drag and drop ready-made node setups straight into the compositor workspace; any node group marked as an asset turns up here on its own. Sitting at the editor's bottom, the shelf gives a compact, easy-to-reach interface for inserting and arranging compositor assets, and compared with the Asset Browser it blends more smoothly into the compositing workflow, and you can show or hide it whenever you like. The Asset Shelf helps you assemble node setups quickly from reusable assets, explore common compositing techniques and effects, and stay entirely inside Blender for post-processing. Toggle it from the compositor editor's header.

[Related references](INDEX.md).
