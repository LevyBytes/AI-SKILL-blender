# 3D Viewport: Invisible Limit Zooming In, Solutions, Tools, Invalid Selection

### Invisible Limit Zooming In

Zoom feels blocked sometimes. Blender orbits around a pivot.

Useful for multi-angle object viewing (like wheel pottery). But awkward for scene exploration or inner modeling.

#### Solutions

- Employ View Dolly.

- Use Walk/Fly Navigation.

- Auto Depth + Zoom to Mouse Position ensure distance to cursor point.

- Zoom Region resets the pivot meanwhile.

- Reposition around cursor Alt - MMB . Uses cursor location as your center.

- Get an NDOF (3D mouse), covered in peripherals settings.

### Tools

### Invalid Selection

Certain setups cause selection failure. Edit Mode vertex/edge/face picking shows erratic picks.

OpenGL-based picking requires correct GPU driver communication.

Attempted remedies:

Disable Multisampling
Most frequent cause.

Known issues exist on some cards with multisampling.

Access graphics settings and toggle multisampling off.

Change Anti-Aliasing Sample Settings
OpenGL setup affects which sample modes function.

Trial-and-error finds working setups.

Upgrade Graphics Driver
OpenGL questions need recent drivers.

Prevalent but unsolved on many versions.

[Related references](INDEX.md).
