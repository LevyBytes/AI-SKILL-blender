# Introduction

The Video Sequencer lets you arrange images, videos, sounds, and scenes along a timeline and merge them into a fresh video. This section only covers its UI; for usage, see the Video Editing section.

Editor Layout: the Video Sequencer is made of several regions, spelled out in the next sections; the combined Sequencer & Preview view type appears in Figure 1.
Header: holds menus and buttons for working with the editor; it shifts a little with the chosen view type (below).
Footer: holds menus and buttons for animation playback.
Preview: shows the Sequencer's output at the Playhead's time.
Sequencer: shows a timeline for managing the strip montage.
Sidebar: shows the active strip's properties, split into panels and tabs; toggle with N.
Toolbar: shows a list of tools; toggle with T.

View Types: the Video Sequencer has three view types, switched via the View Type selector (Figure 1, top left).
Sequencer: the timeline and strip properties.
Preview: the preview window and preview properties.
Sequencer & Preview: both the preview and the timeline together with their properties.
Tip: rather than a single Video Sequencer in Sequencer & Preview mode, it's often handier to keep one in Sequencer mode and another in Preview mode, because Sequencer & Preview is missing most Preview tools; Blender's default Video Editing workspace sets up this layout for you.

Performance — playback can be sped up in a few ways. The biggest win is letting the Video Sequencer cache generated frames; there are two cache levels — a memory cache (on by default, and enlargeable if RAM allows) and a disk cache (slower but roomier) — both configurable in the Preferences. Another route is Strip Proxies: lower-resolution and/or lower-quality copies of source images and videos that load faster than the originals.

Preview mode shows how the finished video will look and also offers tools for moving, rotating, and scaling images, plus scopes for analyzing color distribution.

You can pan with MMB and zoom with the Wheel or NumpadPlus / NumpadMinus, or use the gizmos. Pressing Home resets the view, filling the editor's area with the preview.

Playback Controls: this region holds controls and options for playback, keying, auto keyframing, and transport. They let you control how animations preview and sync with audio, add and manage keyframes via keying sets and auto keying, navigate the timeline with playback and transport controls, and set frame ranges and preview chosen segments. See also the Playback Controls documentation for the full footer rundown.

This section describes Blender's asset library system, introduced in Blender 3.0 and set to grow over upcoming releases.

See also: Asset Browser (the primary interface for arranging and using assets), Asset Catalogs (for organizing assets), and Pose Library (built atop the Asset Browser).

What is an Asset? — an asset is a data-block that carries meaning. A blend-file is itself a database of many data-blocks — objects, textures, materials, and so on — and to reuse or share them, the data needs meaning: what is this, and what's it for? Assets are curated data-blocks meant for easy reuse. Note: the general word "asset" often also covers other file types — images, sounds, videos, etc. — which Blender doesn't currently support as assets; see Future Development.

What is an Asset Library? — it's a directory on your drive that you register in the Preferences as a library. Registering means giving the library a name (like "Sprite Fright") and an on-drive location (like /home/sybren/projects/sprite-fright/assets). Once registered, you can pick it in the Asset Browser; all its blend-files are scanned for assets, and those assets all appear there. Note: loading a library the first time can take a while, but later loads are much faster — Blender builds an index of every asset in a library and keeps it current as files change, storing the indices in the Local Cache Directory. The blend-files can sit directly in the library's top level or in any subdirectory; the on-drive organization is entirely yours, and whichever blend-file holds them, each asset can be given a catalog (see Asset Catalogs).

Asset Types — assets split broadly into primitive and preset, depending on the data-block type. Primitive assets are data-blocks linked or appended into the current file — objects, materials, worlds — you drag them from the Asset Browser either into the scene (for objects and worlds) or onto an existing object (for materials). Preset assets are data-blocks that get loaded and then applied to something or activated: a pose asset, say, loads from its blend-file and applies the pose to the active armature, while a brush asset is loaded into the current file and activated for painting or sculpting without being saved in the file. The asset-type definition will broaden in future; see Future Development.
Supported Assets:
- Material (Primitive): a Material data-block applied to objects; dragging it onto an object replaces the material slot.
- Collection (Primitive): a set of objects you can link or append into a scene, its internal hierarchy preserved and usable instanced or for modular scene building.
- Object (Primitive): a standard Object asset dragged into the scene; it may hold mesh, curve, light, or other data.
- Brush (Preset): a Brush asset for sculpting, texture painting, or vertex painting; activating it makes it the current brush but doesn't store it permanently in the file.
- Node Group (Primitive): a Node Group asset dragged into compatible node editors (Geometry Nodes, Shader Editor, Compositor); a reusable chunk of node logic.
- World (Primitive): a World asset that sets ambient lighting and the background; dragged into the viewport it replaces the current world, and it can equally be appended as a data-block.
- Scene (Primitive): a complete Scene asset, with its cameras, lights, and linked objects; scenes preview by rendering the active camera in Solid mode (so they need an active camera), and dragging one into a window (other than the Asset Browser) imports or links the scene and makes it that window's active scene.
- Pose Action (Preset): a Pose Asset built on an Action data-block; applying it loads the pose and lays it on the selected or active armature, shifting bone transforms while leaving the source action untouched.

The Current File Asset Library: to help manage assets in the current blend-file, set the Asset Browser to the Current File asset library; this always shows the current file's assets even when the file isn't saved in an asset library, and it lets you create and use assets in one file for small single-file projects. When the current file is part of an asset library you can of course also see its assets there; the ones in the current file carry an icon and are the only editable ones.

Life Cycle of an Asset: this section covers creating, editing, sharing, and using assets.
Creating an Asset: first make the thing you want to turn into an asset: the object, material, world, or your character's pose. The next step depends on the asset type (above). For primitive assets, use Mark as Asset, found in the data-block selector, the Outliner, and (for objects) the 3D Viewport's Object menu; it auto-generates a preview, which you can swap for an image of your own via the folder button beside the preview in the Asset Browser's Asset Details region.

For preset assets there's a dedicated button per type — for poses, a Create Pose Asset button in the Action editor; brush assets are made with Duplicate Asset from existing brush assets. Once an asset is made, be sure the current blend-file is itself saved inside your asset library; Blender won't copy the asset into the library for you.

Editing Assets — since assets are ordinary data-blocks with a little metadata attached, you can edit them as you would any Blender data — open the file and change the object, material, world, and so on. For pose assets it's the same — with the pose library file open, click Assign Action to assign the pose action to the selected armature, then use all the animation tooling to edit the pose, remove or add keys, and so on. Asset metadata is edited via the Asset Browser.

Sharing Assets — because assets simply live in blend-files, you pass them on by passing on their blend-file; just remember to bundle the Asset Catalog Definition File as well. There's currently no built-in way to pull selected assets out and save them (with their catalog definitions) into a separate blend-file — that could be an add-on.

Using Assets: assets are used from the Asset Browser. The pose library goes further, adding an Asset View to the 3D Viewport; see Use from 3D Viewport.

Removing Assets: asset metadata is erased with the Clear Asset operator, available in data-block selectors, the Asset Browser, and (for objects) the 3D Viewport menu.
Clear Asset: strips the asset metadata (catalog, description, author, tags), turning an asset back into a plain data-block; the usual removal rules then apply, so if a mesh object still sits in the scene, Clear Asset won't remove it from the scene (see Life Time). The preview stays inside the data-block rather than being removed.
Clear Asset (Set Fake User): does the same as Clear Asset and then marks the data-block as protected, so it's no longer an asset yet won't be lost when the blend-file is saved.

Bundled Assets: Blender ships with many assets out of the box in the "Essentials" library, including: Hair node groups, the Smooth By Angle Node Group, and Brushes (Mesh Sculpt, Curve Sculpt, Texture Paint, Vertex Paint, Weight Paint).

Asset System Files (.asset.blend Extension) — some asset types can be edited without opening a blend-file inside an asset library; Blender saves these to libraries in special .asset.blend files, managed entirely by the asset system and holding a single asset plus its dependencies. You can still save a normal file with the .asset.blend extension — that won't be treated as an asset system file, since Blender tells the difference. Asset system files have one more quirk: you can open but not save them; Save As still works to spin off a new, normal blend-file from one, so the contained assets can't be edited without opening the file itself, and Blender shows clear warnings that asset system files can't be changed and saved the usual way. They're special because the asset system may need to regenerate them, which would lose any extra user changes — so to prevent that data loss they're protected from user edits. Currently only brush assets support this.

Design Limitations — Blender may not write to any blend-file other than the one currently open, or the special .asset.blend files above, so editing an asset means opening its blend-file — luckily just one click away, both in the Asset Browser's Source List region and in the asset context menu.

Future Development: this section sketches interesting directions for further work; though not exhaustive, it may clarify Blender's current Asset Browser functionality.
Non-Data-Block Assets: non-Blender assets like image or audio files will likely be supported in a future version, with their metadata kept in XMP sidecar files as other software does; importers (USD, glTF, FBX, …) could add their file types as assets this way too, and it should become possible to enrich an asset with a Python script that runs when the asset is used.
Cross Blend-File Editing — as noted, Blender itself may not write to blend-files other than the open one, which keeps complexity down (a reliable undo system is hard when manipulating other files) but gets in the way of mass-updating assets spread across blend-files. Since there's already tooling that edits blend-files outside Blender (see Blender Asset Tracer), an external tool for such cross-file edits is possible — perhaps via Blender's application templates system, or as an add-on, since the rule applies to Blender itself, not its add-ons.
Asset Pushing — Note: the Brush assets introduced in Blender 4.3 include support for the asset-pushing concept described here, which may reach more asset types later. Asset pushing means getting assets into the library while you're working on a file and want to copy an asset from it into the library. It looks deceptively simple, and sometimes is, but often turns complex: pushing an object into an external library — should it copy the materials too? The texture images those materials reference? Objects referenced by custom properties, constraints, or modifiers? And into which files? One big assets.blend, individual blend-files, or a directory per asset type? Blender shouldn't be making such calls for you.

For specific cases these are all solvable, which is why the pose library was built as an add-on enabled by default; studios with particular needs can disable it and build their own, since the building blocks all live in Blender's core and needn't be copied for this, and add-ons can write to other blend-files, so they can make the decisions for users.

Asset pushing is desirable, but because of the questions above it's unclear how to implement it well in a way that still leaves artists in control of their assets.

[Related references](INDEX.md).
