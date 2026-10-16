# Viewer Node

## Viewer Node

The Viewer node previews image data or value maps anywhere in a compositor graph — a diagnostic tool to inspect intermediate results without affecting the final output. Assign a node to a Viewer quickly with Shift-Ctrl-LMB on it, switch between Viewers by selecting one with LMB, and only the active Viewer (with the header icon) shows in the backdrop or Image Editor. Input: Image (sent straight to the viewer result; unconnected, the output is black). The node has no output sockets. Usage — keyboard shortcuts: Viewers offer a quick way to toggle between viewer nodes while compositing — Assign Shortcut (Ctrl-1, Ctrl-2, etc.: select a node and press to assign it, creating and activating a Viewer if none is attached, with the number shown at the node's upper right) and Activate Node (1, 2, etc.: press the assigned number to activate that node's Viewer output), supporting only number keys 1-9. Using the Image Editor: the Viewer can display results there by selecting Viewer Node in the header's linked Image data-block menu, showing the currently selected Viewer's image; save it with Image ‣ Save As… (Alt-S); and the Image Editor's header has three more options to view images with or without alpha, or the alpha or Z itself, with click-and-hold sampling values. (For Viewer-specific overlays like text info and render guides, see Guides Overlays.)

The Viewer node previews a node's results.

Inputs:
Color — the usual color input.

Properties — this node exposes no properties.

Outputs — this node produces no outputs.

Viewer Node

Displays data from inside a geometry node group in the Spreadsheet Editor and 3D Viewport. Geometry and attributes connected to the viewer display in the viewport; evaluated values appear in the spreadsheet. Scalar values and grids also show in the spreadsheet.

Note: The Viewer node cannot be used in the Tool context—only in the Modifier context.

Activation and Deactivation: Use Shift+Ctrl+LMB on a node or socket to connect it to the active viewer. In the View menu, toggle Viewer Node to show or hide all visualizations, comparing the result against the final output.

Keyboard Shortcuts
Assign (Ctrl+1, Ctrl+2, etc.): Select a viewer node and press to assign a number shown in the upper-right.
Activate (1, 2, etc.): Press the assigned number to activate that viewer. Only keys 1–9 work.

Viewing Single Socket Values: Sockets can show evaluated values directly in the node editor. The current value displays beside the input, enabling inspection without a Viewer node. Works for scalars and small types (Float, Integer, Boolean, Vector). Geometry and grids need the Viewer node or Spreadsheet.

Attribute Field Visualization: With both Geometry and field inputs connected, values visualize in the Viewport via Viewer Overlay. The domain auto-detects when possible, otherwise defaulting to Face Corner for meshes and Point for curves. Set manually from the node's properties if needed. The Spreadsheet shows only columns for the selected domain. Note: Geometry socket must be first.

Pinning: Pin the Viewer in the Spreadsheet to keep data visible even when inactive. Pinned data persists regardless of object or selection changes.

Inputs: Add by dragging a socket into the blank socket or via Viewer Items properties.

Properties
Domain: The attribute domain for Value input. Auto chooses based on connected nodes.

Viewer Items
Socket Type: The data type for the input.
Auto Remove: Remove automatically when unlinked.

Outputs: This node has no outputs.

Examples: Visualizing Noise Texture Factor and Index Attribute as text on the default cube.

[Related references](INDEX.md).
