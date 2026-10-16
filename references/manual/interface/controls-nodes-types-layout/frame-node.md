# Frame Node

## Frame Node

The Frame node organizes and groups other nodes within the editor, helping manage complex node trees by visually clustering related nodes. It's especially useful when a setup is too large to view easily at once, or to separate logical sections of a tree without creating a reusable Node Group.

Usage:
- Add nodes to a frame by dragging them inside it.
- Moving the frame also moves all the nodes it contains.
- Resize a frame by dragging its corners or edges.
- A frame can display a custom label, handy for naming sections of your node setup.

Properties:
Label Size — the font size of the label, for example so subordinate frames have smaller titles.
Shrink — once a node is placed in the Frame, the Frame shrinks around it to remove wasted space; at that point you can no longer select the Frame's edge to resize it, since resizing instead happens automatically as the nodes inside are rearranged. Disable this option to change that behavior.
Text — to display more comprehensive text, a frame node can show the contents of a text data-block; this is read-only, so use the Text Editor to modify the contents.

Editing:
Join in New Frame (Menu: Node ‣ Join in new Frame; Shortcut: F) — create a new Frame node around the selected nodes; when invoked with F, a popup lets you assign a custom Label to the new frame, shown as its title to describe its contents.
Add to Frame (Shortcut: Ctrl-P) — once a frame node is placed, add nodes by dropping them onto the frame, or by selecting the node(s) then the frame and pressing Ctrl-P — think of it as parenting the selection to the frame.
Remove from Frame (Menu: Node ‣ Remove from Frame; Shortcut: Alt-P) — select nodes and press Alt-P to remove them from a frame — think of it as unparenting the selection from the frame.

[Related references](INDEX.md).
