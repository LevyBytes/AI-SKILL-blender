# Node-Based Tools

## Node-Based Tools

### Node-Based Tools

Geometry node groups can become tools invoked from menus.
The Tool Context builds such tools for access via the Non-Assets menu in the 3D Viewport.
Publishing as an asset lets you move them to custom menus, reuse across blend-files, or share.

### Tool Context

Tools have different settings than modifiers, so switch the Node Tree Sub-Type to Tool in the Geometry Node Editor header.
When Tool is active, the data-block menu shows only groups with Tool Usage enabled.

- New groups created in Tool mode auto-enable Tool Usage.
- Convert an existing modifier group: manually enable Tool Usage in the Sidebar (optionally disabling Modifier Usage) before switching to Tool mode. Configure Supported Modes & Object Types.

**Note:** Inspection features are unavailable in Tool context.

### Asset

Publish a tool as an asset: right-click the node group name and choose Mark as Asset.
The group appears in the Asset Browser's Unassigned catalog.
Move it to a catalog named after a menu to place it at that menu's end.
Save the blend-file as an asset bundle and copy into an asset library for multi-file reuse.
Share the bundle with others.

### Tool Settings

Accept user input via sockets on the Group Input node.
These appear in the Adjust Last Operation panel when the tool runs.

### Supported Modes & Object Types

Specify which modes and object types a node group supports using popover menus in the editor header.

**Important:** Mesh object shape keys are unsupported and removed if you run a node tool.

### Tool-specific Nodes

Exclusive to Tool context:

- 3D Cursor Node
- Mouse Position Node
- Viewport Transform Node
- Active Element Node
- Selection Node
- Set Selection Node
- Face Set Node
- Set Face Set Node

**Note:** Self Object returns the Active object inside a Tool node group.

### Non-supported Nodes

Modifier context only:

- Simulation Zone
- Viewer Node

[Related references](INDEX.md).
