# Link Data

## Link Data

### Link Data

Reference

Mode :

Object Mode

Menu :

Object ‣ Link/Transfer Data

Shortcut :

Ctrl - L

Performs multiple assignments: including objects in a scene, giving objects matching data or modifiers, and so on.

When two objects link to the same data, modifications to one appear in the other. If you prefer each object to have separate data, use Making Single User to decouple them.

Link Objects to Scene
Incorporates the selected objects into the specified scene. Objects can exist in multiple scenes simultaneously and show the same position/animation across all.

Link Object Data
Swaps the object data of the selected objects with that of the active object.

Link Materials
Swaps the materials of the selected objects with those of the active object.

Link Animation Data
Swaps the actions and tracks of the selected objects with those of the active object.

Link Collections
Transfers the selected objects to the same collections as the active object.

Link Instance Collection
Swaps the instance collection of the selected objects with that of the active object.

Link Fonts to Text
Swaps the font of the selected text objects with that of the active text object.

Copy Modifiers
Swaps the modifiers of the selected objects with those of the active object.

Copy Constraints
Swaps the constraints of the selected objects with those of the active object.

Copy Grease Pencil Effects
Swaps the visual effects of the selected Grease Pencil objects with those of the active object.

Copy UV Maps
Swaps the active UV map of each selected mesh object with the active UV map of the active object. If a selected object lacks UV maps, one is created.

All objects must have matching geometry and face ordering. Use Sort Elements to ensure the latter; this operator is most applicable when the destination is a modified copy of the source. Try Transfer Mesh Data for other scenarios.

Transfer Mesh Data
See Transfer Mesh Data.

Transfer Mesh Data Layout
See Transfer Mesh Data Layout.

Link Receivers to Emitter
Incorporates the selected objects into the Light Linking collection of the active light object.

Link Blockers to Emitter
Incorporates the selected objects into the Shadow Linking collection of the active light object.

[Related references](INDEX.md).
