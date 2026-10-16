# Group Output

## Group Output

The Group Output node defines a node group's final output, deciding which values pass out to the parent node tree (or, in the Compositor, to the renderer) — in the Compositor it sets the image result sent to the renderer or image output after rendering. It updates automatically after each evaluation or render, and interactively when connected inputs change, provided all inputs are fully evaluated. Note: with several Group Output nodes in a tree, only the active one is used and the rest show an "Unused Output" warning, the active one being chosen in the node header. Inputs: none by default — sockets appear when outputs are defined in the Sidebar's Group tab (or when dragging a connection onto the blank socket area), each input being a group output socket exposable to the parent tree, and in the Compositor only the first image input is the final render result while extras are ignored. Properties: see Group Sockets. The node has no output sockets, its sole job being to define which values leave the group.

[Related references](INDEX.md).
