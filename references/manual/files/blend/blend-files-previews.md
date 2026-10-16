# Blend-Files Previews

## Blend-Files Previews

A blend-file can hold previews, both of itself and of some of its data-blocks. You can stop any previews being written on save with the Save Preview Images setting in the Preferences' Save & Load section.

Blend-File Preview — Blender saves a small preview of the current scene in the blend-file by default, which appears in the File Browser's Thumbnail view. During installation, Blender also adds a small tool to your OS so your system file browser can show these previews as thumbnails too.
macOS — the Blender Thumbnail extension can be switched off in System Settings under "Login Items & Extensions", in the Quick Look category.

Data-Blocks Previews — Blender auto-generates previews for some data types, mainly shading-related ones (images, textures, materials, lights, world shaders). It can also keep previews for scenes, collections, and objects, though those you generate by hand. These previews then feed the File Browser's Thumbnail view when you link or append data-blocks.
Refresh Data-Block Previews — Reference: Menu: File ‣ Data Previews ‣ Refresh Data-blocks Previews. Refreshes every auto-generatable (shading-related) data-block preview in the current blend-file; you still need to save the file to write them to drive.
Batch Generate Previews — Reference: Menu: File ‣ Data Previews ‣ Batch Generate Previews. Generates some data-block types' previews (you choose which in its options) across one or more blend-files on your drive; don't run it on the file currently open in Blender. This is currently the only way to generate and store previews for scenes, collections, and objects in blend-files, and since it involves a lot of rendering — even at small sizes — it can take a while.
Scenes — generates previews of scenes and their collections.
Collections — generates previews of object collections.
Objects — generates previews of objects.
Materials & Textures — covers materials, textures, images, and the rest of the internal data.
Trusted Blend Files — when on, any Python scripts and drivers the file may carry run automatically; turn it on only if you made the file yourself or trust whoever gave it to you not to have slipped in malicious code. See Python Security.
Save Backups — keeps a backup copy (blend1-file) of each file when saving alongside generated previews.
Clear Data-Block Previews — Reference: Menu: File ‣ Data Previews ‣ Clear Data-blocks Previews. Clears all previews, a generic type, or a specific data-block type, in the current blend-file; you still need to save to clear them from drive.
Batch Clear Previews — Reference: Menu: File ‣ Data Previews ‣ Batch Clear Previews. Clears some data-block types' previews (you choose which) across one or more blend-files on your drive; don't run it on the file currently open in Blender.
Scenes — clears previews of scenes and their collections.
Collections — clears previews of object collections.
Objects — clears previews of objects.
Materials & Textures — clears previews for materials, textures, images, and other internal data.
Trusted Blend Files — as above; runs the file's Python scripts and drivers automatically, so enable it only for files you trust (see Python Security).
Save Backups — keeps a backup copy (blend1-file) of each file when saving alongside cleared previews.

[Related references](INDEX.md).
