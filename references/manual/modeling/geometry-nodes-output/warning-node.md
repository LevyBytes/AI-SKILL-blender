# Warning Node

## Warning Node

Warning Node

Outputs a custom message in the Geometry Nodes modifier's Warnings panel. Lets node groups communicate expectations, assumptions, and error conditions about inputs—required ranges, missing data, unsupported configs.

Warnings propagate through parent node groups by default, controlled via the Propagation setting on each node.

Inputs
Show: Controls whether the warning displays. When disabled, it suppresses.
Message: Text describing incorrect inputs, required conditions, or other info for users.

Properties
Warning Type: Severity affecting the icon shown.
  Info: Informational, no problem indicated.
  Warning: Potential issue that may cause unexpected results.
  Error: Invalid configuration likely producing incorrect results.

Outputs
Show: Passes the Show input through, forwarding the warning state to other nodes.

[Related references](INDEX.md).
