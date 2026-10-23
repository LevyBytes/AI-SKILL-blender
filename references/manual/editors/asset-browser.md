# Asset Browser

## Asset Browser

The Asset Browser is the principal interface for organizing and using assets. To open it, make a new area, click the Editor Type button at its top-left, and pick Asset Browser.

See also: Asset Libraries (general information on Blender's asset-library system, including creating and editing assets, and design rationale), Asset Catalogs (for organizing assets), and Pose Library (built atop the Asset Browser).

Interface — Header — Import Settings:
Import Method: decides how data is handled when an asset is brought in. It sits in the middle of the Asset Browser header whenever an asset library other than Current File or Essentials is active.
  Follow Preferences: uses the import method chosen in the File Path Preferences.
  Link: the asset is linked into the current blend-file and stays read-only; later edits to the asset file propagate to every file that links it.
  Append — the asset and all its dependencies are copied into the current file. Drag a material in three times and you get three independent copies; the same goes for an object. Here "dependencies" means everything the asset relies on — for an object that can be its mesh and materials, but also other objects pulled in by modifiers, constraints, or drivers. Because the file now owns its own copy, later edits to the asset file won't show up in the file it was appended into.
  Pack: imports the asset as linked data and packs it into the current blend-file right away, so it stays available even if the original library data changes or goes missing; handy for keeping self-contained files that don't lean on external asset-library paths.
Instance Collections – When Linking/Appending: mirrors the Instance Collections option used when appending from the file browser. Some asset types, collections among them, can be made as an instanced collection (by switching on the Instance option once collection assets have been dragged into the 3D Viewport): with these options on, an empty object is added that instances the collection, whereas with them off the whole collection hierarchy is dropped into the scene. Collection assets from the current file are always instanced.

Display Settings: tune how assets appear in the list.
Display Mode: controls how files are shown. Horizontal List lays files and folders out in a horizontal list; Thumbnails shows previews.
  Preview Size (Horizontal List): resizes the thumbnails in list views.
  Column Size (Horizontal List): the column width in horizontal list views.
  Size (Thumbnails): resizes the preview thumbnails.
Sort By:
  Name: orders the list alphabetically.
  Asset Catalog: groups assets from the same catalog together, ordered by name within each catalog, with the catalogs following the flattened catalog hierarchy.

Main Region: the central area lists the assets held in the chosen catalog. Click LMB to pick one asset; add Ctrl to add or remove an asset from the selection, or Shift to grab a range; you can also drag LMB for a box select. Its context menu offers:
  Refresh Asset Library (R): refreshes the list.
  Clear Asset: see Removing Assets.
  Clear Asset (Set Fake User): see Removing Assets.
  Open Blend File: opens the blend-file holding the asset.
  Display Size: resizes the preview thumbnails.

Asset Library Region: the left-hand region lets you choose an asset library and shows its catalogs; toggle it with T.
  Asset Library — which library's catalogs to display. All Libraries shows catalogs from every available library; Current File shows the catalogs in the current blend-file (even before it joins an asset library — see The Current File Asset Library); Essentials shows the catalogs bundled with Blender. Any libraries you added in the File Path Preferences appear here as well.
  Copy Bundle to Asset Library: appears when Asset Library is Current File and the open blend-file is an asset bundle not yet part of a library. It lets you choose a target library, then opens a File Browser at that library's root folder so you can save the file there; once saved, its assets join the library.
  Catalogs: a Tree View of the selected library's catalogs. A catalog is a group of assets; selecting one limits the listing to the assets in that catalog and its children. Double-click to rename a catalog, or drag and drop to reparent it. Add-ons and features such as the Pose Library can add custom panels here.

Asset Details Region: the right-hand region shows the active asset's metadata; toggle it with N or the gear icon in the header. Only metadata for assets stored in the open blend-file may be edited.
  Name: the asset's name; it stays unique per asset data type inside a single blend-file.
  Source: the complete path of the blend-file the asset lives in.
  Open Blend File: opens that blend-file in a fresh Blender instance; closing that instance refreshes the Asset Browser automatically.
  License: an optional name for the license the asset is distributed under; Blender itself makes no use of it.
  Copyright: an optional copyright notice; Blender itself makes no use of it.
  Description: an optional asset description; Blender itself makes no use of it.
  Author: an optional field naming the asset's author; Blender itself makes no use of it.

Preview: shows the asset's preview image (see Asset Previews).
  Load Custom Preview: opens a File Browser to pick a new image for the preview.
  Generate Preview: auto-creates a fresh preview for the asset.
  Preview: a menu of extra preview operators.
  Render Active Object: builds a preview from the 3D Viewport's active object, useful for node groups, which can't generate their own preview automatically.
  Remove Preview: strips the asset's preview.
  Capture Screenshot Preview: drag-select a rectangle over part of Blender to grab it as the asset's preview image (see Screenshot Capture for Previews).

Tags: a panel for viewing and editing an asset's tags. Tags mean nothing to Blender and are yours to choose freely; when you filter assets with the search field, those whose tags partially match the term are pulled in too.
Note: more panels may appear depending on the object's current mode and the selected asset types — see Pose Library, for example.

Using Assets: broadly, you use an asset by dragging it from the Asset Browser to wherever you want it. Objects and worlds drag into the scene; materials drag onto the object meant to wear them; geometry nodes drag onto objects to attach a Geometry Nodes Modifier. Pose assets behave differently and are covered in Pose Library.

Dragging a collection adds it as an instance — a single object standing in for the whole collection, so its contents stay out of the Outliner and can't be edited. Two ways to change that:
Run Make Instances Real to swap the object for the collection's actual contents.
Or delete the object, locate the collection in the Outliner's Blender File display mode, and choose Link to Scene from its context menu.

What happens when an asset is used depends on the Import Method. Note that once the asset is in the current file, every ordinary Blender operation becomes available — you might, say, link an object into the scene (which links its mesh and materials too), then make just the object local via Object ‣ Relations ‣ Make Local… ‣ Selected Objects while leaving the mesh and materials linked to the asset files. The result is a local, editable object whose mesh and materials still track any changes in the asset library.

Asset Previews: preview images are usually generated on their own when you flag a data-block as an asset. Objects are shot from their local -Y axis, collections from the global -Y axis (since they have no local axis). If the auto-generated preview falls short, you can swap in a custom one. For pose-asset previews, see Controlling the Look of Preview Images.

Screenshot Capture for Previews: when a particular preview is wanted, a screenshot is a quick route. The operator lives under the Preview popover (see Capture Screenshot Preview). Screenshots are only possible for editable assets, i.e. those in the Current File and Asset System Files. Once it starts, click and drag a rectangle over any portion of Blender to grab a preview image; while dragging you can shift the whole capture area or unlock its aspect ratio (the status bar's shortcut help lists the keys). Re-running the operator remembers the area you grabbed last, so a single click repeats the same screenshot.
Note: choosing an area that falls entirely inside one 3D viewport actually performs a background render of that section, which permits a transparent background but also means UI elements can't be captured.

Asset Bundles: these are blend-files that reference no other file and whose names end in _bundle.blend; any textures and other external files must be packed into the blend-file itself. You can copy an asset bundle into an asset library through the Asset Browser:
Open the asset-bundle blend-file.
Set its Asset Browser to Current File if it isn't already.
Click Copy Bundle to Asset Library.
Pick the library to copy it into.
A File Browser opens at that library's root folder; choose where the blend-file should go and click the Copy to Asset Library button.
The file is saved at your chosen spot, and any of the bundle's catalogs are folded into the target library.
Note: the words "asset" and "bundle" both see broad use, and not always with the meaning given here. Not everything billed as an "asset bundle" offers the Copy to Asset Library function — for that, the file has to meet the definition above.

[Related references](INDEX.md).
