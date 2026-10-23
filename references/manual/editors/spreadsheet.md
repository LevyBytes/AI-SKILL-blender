# Spreadsheet

## Spreadsheet

The Spreadsheet editor lets you inspect the active object's geometry attributes, usually to debug geometry nodes.

Header:
Show Only Selected: available only while the object is in Edit Mode; when ticked, only the selected geometry elements' data appears.
Use Filter: whether to apply the filters defined in the Sidebar (below).
View Menu:
  Toolbar (T): shows or hides the left-hand tab panel for creating and working with markers and masks.
  Sidebar (N): shows or hides the Sidebar.
  Internal Attributes: shows attributes whose names begin with a period, meant for internal use.
  Area: area controls; see the user-interface documentation.

Main Region — displays the attribute data as a spreadsheet, each column an attribute or data property and each row one element — a vertex, face, spline, or instance, say. The column names and row indices stay pinned as you scroll in either direction.
Columns resize by dragging the vertical line between them.
Double-clicking that line auto-sizes the column to its content.
Columns reorder by dragging their header.
Note: tooltips give more detail by type — Byte Color attributes show as scene-linear floats while the actual integer values appear on hover, and Matrix attribute values appear only in tooltips.

Data Set Region: on the left, this region chooses what the spreadsheet shows.
Context Path: shows the active object's name in the panel header. Click an arrow between names to hide the modifier. Click the lock icon to pin the Spreadsheet to the currently active object and data path so it stays put when you select another object; click again to unlock.
Object Evaluation State: which state of the object's data is shown: Evaluated (with all modifiers applied), Original (the raw object data, no modifiers), or Viewer Node (data from the active Viewer Node in Geometry Nodes). You can also flip between Evaluated and Viewer Node via the icon in the Viewer node's header.
  Viewer Path: shown when Object Evaluation State is Viewer Node; traces the path from the modifier to the active viewer node, with each enclosing group appearing in the path if the viewer is nested.
  Viewer Data — shown when Object Evaluation State is Viewer Node; picks which Viewer Items from the active Viewer node appear in the Spreadsheet. When a Viewer node puts out several data sets (geometry plus one or more evaluated fields, say), each becomes its own Viewer Item, and this setting selects which to show — a specific attribute, value field, or geometry component — without touching the Viewer node's connection. Note: the available viewer items track the active Viewer node and its inputs, and changing the active viewer or its connections refreshes this list on its own.
Geometry: lets you browse nested geometries (a mesh inside an instance or a geometry collection, say).
Domain: lets you pick the attribute domain to show, such as mesh vertices or curve splines; the element count for each domain sits beside its entry.
  Volume Grids — when the chosen geometry component is a Volume, the Spreadsheet details every grid it holds. Each grid is one data field — density, color, or velocity, say — and can be inspected on its own for structure and memory use. For each grid it lists:
    Grid Name: the grid data's name, like density or temperature.
    Data Type: the kind of data the grid stores, e.g. Float, Vector, or Boolean.
    Class: the grid class describing its purpose, such as Fog Volume or Level Set.
    Voxel Extent: the grid's bounding box in voxel coordinates, i.e. the voxel count along X, Y, and Z.
    Min Voxels: the grid bounding box's minimum voxel coordinates: the lowest X, Y, Z voxel indices it occupies, marking where the grid begins in voxel space.
    Voxels: the grid's total active voxel count, including every explicitly stored voxel even when held in tiles (a single leaf tile holds 512 voxels).
    Leaf Voxels: the active voxels stored in leaf nodes; unlike Voxels, this leaves out voxels belonging to higher-level tiles.
    Tiles: the grid's active-tile count; tiles are higher-level voxel containers that sparse volume formats (OpenVDB, say) use to optimize storage.
    Size: the grid's estimated memory size, covering all currently allocated voxel and tile data.
  These figures let you weigh the complexity, density, and performance cost of volumetric data from Geometry Nodes or imported volume files. Note: because volume grids are sparse, the Extent can far exceed the actual active-voxel count — only active regions sit in memory, keeping volume data efficient even across large domains.

Sidebar: here you define filters so only matching rows show; click Add Row Filter and configure the properties below.
Enabled: uncheck to switch a filter off temporarily.
Column: the column to filter on; with no column of that name, the filter grays out and is ignored.

To filter on an attribute from a different domain, use the Store Named Attribute Node to make a copy converted to the current domain, then filter on that.

Operation: numerical columns offer the comparison operators below; other columns support only Equal To.
  Equal To: shows only rows whose column value equals the filter value (within the set threshold).
  Greater Than: shows only rows whose column value exceeds the filter value.
  Less Than: shows only rows whose column value falls below the filter value.
Value: the filter value to compare each row's value against.
Threshold: how far a row's value may stray from the filter value before it's dropped.

Status Bar: reports the row and column totals plus how many rows survive filtering.

[Related references](INDEX.md).
