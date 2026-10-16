# Manage Brushes

## Manage Brushes

### Manage Brushes

Brush assets are stored in asset libraries to make them accessible from any Blender session. There are two ways of managing brush assets:

- Using asset operators: Create and update brush assets using utility operators from any Blender file. Storage is managed by Blender. Convenient for simple "on the fly" management of personal brush asset libraries.

- Using manual storage: Create and update brush assets by opening blend files within asset libraries, and managing brush asset data-blocks in there. Useful for careful curation of asset libraries, especially to prepare them for sharing with others.

### Asset Operators

Brushes can be managed through a few operators that let Blender handle the act of saving and updating the brushes in asset libraries for you. Assets managed this way will be saved in special asset system files using a .asset.blend file extension.

Note

Note that only brush assets created via Duplicate Asset can be edited further using these asset operators. For others, these operations will be grayed out, and manual management is necessary.

Brushes from the Essentials asset library cannot be edited.

Reference

Mode :

All Paint Modes

Panel :

Sidebar ‣ Tool ‣ Brush Asset
Properties ‣ Tool ‣ Brush Asset

Menu :

Asset Shelf ‣ Context Menu

Brush Asset panel in the Sidebar showing asset operators.

Duplicate Asset…
Creates a copy of the currently active brush as asset, and activates it. A popup is spawned to input some settings to use:

Name
A custom name to use for the new brush.

Library
Choose an Asset Library to store the new brush asset in. The available asset libraries are configured in the Preferences.

Catalog
Choose an Asset Catalog to assign the brush asset to. Entering a non-existent name/path will create a new catalog accordingly.

Delete Asset
Permanently remove this brush asset from the Asset Library it is stored in. This cannot be undone, so a popup will ask for confirmation.

Edit Metadata…
Spawns a popup to change some of the available asset metadata fields:

Catalog
Choose an Asset Catalog to assign the brush asset to. Entering a non-existent name/path will create a new catalog accordingly.

Author
See Asset Author.

Description
See Asset Description.

Edit Preview Image…
Opens a window with the File Browser to select an image for the asset preview.

Save Changes to Asset
Saves any changes made to the active brush to the asset library.

Revert to Asset
Discards any unsaved changes made to the brush asset.

### Manual Storage

See also

Life Cycle of an Asset
Complete description of the manual asset create, edit, share and use workflow.

It is also possible to manually manage brushes in blend-files like any other asset data-block. By marking brushes as assets and saving the file in an asset library, they become available from any Blender session. This gives full control over how assets are stored, and is particularly useful for curating asset libraries that can be shared with others.

The Mark as Asset operator used on a brush in the Outliner.

Brushes can be imported as normal data-blocks from other files (including from .asset.blend files from an asset library) through appending. In the Blender File mode of the Outliner, the brush will be listed under Brushes . Right-click the brush and select Mark as Asset . By saving the file inside of an asset library directory, the asset becomes available from all Blender sessions. If necessary, configure an asset library directory in the Preferences.

[Related references](INDEX.md).
