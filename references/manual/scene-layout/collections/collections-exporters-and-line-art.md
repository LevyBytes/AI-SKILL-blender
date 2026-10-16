# Collections: Exporters, Line Art, Custom Properties

### Exporters

Each collection supports export to various file formats. These exporters are globally available (see Importing & Exporting Files), but this panel simplifies repeated exports. For instance, when iterating on glTF game assets or using Blender in studio production for USD asset creation.

Supported formats include:

- Alembic

- Universal Scene Description

- Wavefront OBJ

- Stanford PLY

- FBX

- glTF 2.0

Exporter List
A list view of all enabled exporters for the active collection. Selecting an exporter shows its options in the panel below.

(Add Exporter)
Opens a menu for selecting an exporter to add.

(Remove Exporter)
Removes the selected exporter.

Export All
Exports all configured exporters for the active collection.

Tip

Use File ‣ Export All Collections to export all exporters for all collections.

### Line Art

Usage
Determines how the collection loads into Line Art. Child objects may override this setting in Object Properties.

Include :

Generate feature lines for this collection.

Occlusion Only :

Collection objects cause occlusion to existing lines with their geometry remaining hidden.

Exclude :

Collection objects do not load into Line Art.

Intersection Only :

Collection objects generate intersection lines only with geometry remaining hidden.

No Intersection :

Include this collection without generating intersection lines.

Force Intersection :

Generate intersection lines regardless of object intersection settings.

Collection Mask
Applies custom intersection masking to collection faces. Intersection masks filter lines through the Line Art modifier. Consult Collection Masks for more information.

Mask
Intersection lines from this collection carry this mask value.

Intersection Priority
Specifies an intersection priority value for this collection. Intersection lines belong to the object with the greater priority value.

### Custom Properties

Define and manage custom properties to store data within the collection's data block. Consult the Custom Properties page for details.

[Related references](INDEX.md).
