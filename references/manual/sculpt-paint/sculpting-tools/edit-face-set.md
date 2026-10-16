# Edit Face Set

## Edit Face Set

### Edit Face Set

Reference

Mode :

Sculpt Mode

Tool :

Toolbar ‣ Edit Face Set

Operator :

Grow/Shrink Face Sets

Modifies the Face Set at the cursor position.

### Tool Settings

Mode
Specifies the operation to execute on the face set.

Grow Face Set :

Extends the face set perimeter by one face following mesh topology. Also accessible as a shortcut operator via Ctrl - W.

Shrink Face Set :

Contracts the face set boundary by one face following mesh topology. Also accessible as a shortcut operator via Ctrl - Alt - W.

Delete Geometry :

Removes all faces assigned to the face set.

Fair Positions :

Generates a smooth, even geometry surface from the face set. Ideal for trimming areas with excessive vertex density or situations requiring vertex preservation (such as when using Multires sculpting).

Fair Tangency :

Creates the smoothest possible surface from the face set by minimizing tangent discontinuities. Valuable for establishing smooth curves on intricate topology where standard smoothing alone is insufficient.

| Description | Description | Description |
| --- | --- | --- |
| Before fairing. | After using Fair Positions. | After using Fair Tangency. |

Strength
Determines the magnitude of the operation's effect on mesh geometry. Only available for fairing modes.

Modify Hidden
Include hidden face sets when applying the operation.

[Related references](INDEX.md).
