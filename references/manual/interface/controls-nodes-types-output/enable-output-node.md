# Enable Output Node

## Enable Output Node

The Enable Output node toggles the visibility and value of a Node Group output socket, so a group output can be shown or hidden by an input value or condition. Inputs: Enable (a Boolean controlling whether the connected output socket is visible and active — when False, the group's matching output is hidden) and Value (the value passed to the output when enabled, of any supported type per the node's Data Type). Properties: Data Type (the type of the Value input and output, e.g. Float, Vector, Color, Geometry). Output: Value (the same data as the Value input when Enable is True; when False, the output is disabled and unavailable to the group output).

The Enable Output node toggles visibility and value of node-group output sockets, conditionally showing/hiding outputs based on input conditions. Enable (boolean field) controls socket visibility/activity; when False, the socket hides. Value is output when enabled; supports any data type. Data Type selects the output type. When enabled, Value outputs match input; when disabled, the output hides and unavailable to group output.

Enable Output Node

Toggles visibility and value of a Node Group output socket. Conditionally shows or hides outputs based on input values.

Inputs
Enable: Boolean field controlling socket visibility and activity. When False, the group's output hides.
Value: The data passed to the output when enabled. Type depends on the Data Type property.

Properties
Data Type: The format of the Value input and output (Float, Vector, Color, Geometry, etc.).

Outputs
Value: Passes through the Value input when Enable is True. Disables when Enable is False.

[Related references](INDEX.md).
