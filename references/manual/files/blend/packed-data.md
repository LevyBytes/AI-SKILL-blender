# Packed Data

## Packed Data

Blender can wrap (incorporate) various kinds of data, normally kept outside the blend-file, inside it instead. An image texture that's an external image file, for example, can be tucked "inside" the blend-file, letting you share a whole project as one file rather than, say, an archive of the blend-file plus all its dependencies. You can tell data is packed by the little "gift box" icon beside its path. Warning — not all external files can be packed: some heavy ones, like videos from the Sequence Editor or Movie Clips, can't be packed into a blend-file.

Pack Data — Pack Resources — Reference: Panel: File ‣ External Data ‣ Pack Resources. Flags every eligible external resource the blend-file uses as packed; the actual packing happens on the next save.
Automatically Pack Resources — Reference: Panel: File ‣ External Data ‣ Automatically Pack Resources. When on, every eligible external resource — existing or added later — is automatically flagged as packed; as with Pack Resources, the file must be saved to drive to take effect. Turning it off unpacks nothing, but future external files simply stop being auto-flagged.
Selective Packing: pack a single file by clicking the little "gift box" icon to the left of its file-path widget.

Unpack Data — Unpack Resources — Reference: Panel: File ‣ External Data ‣ Unpack Resources. Unpacks every external resource stored in the blend-file.
Options:
Use files in current directory (create when necessary) — unpacks everything into the blend-file's own directory (//), sorted into proper folders (like "textures"); if the target file already exists, it uses that rather than unpacking.
Write files to current directory (overwrite existing files) — as above, but overwrites an existing target file.
Use files in original location (create when necessary) — unpacks everything to its original location; if the target already exists, it uses that rather than unpacking.
Write files to original location (overwrite existing files) — as above, but overwrites an existing target.
Disable AutoPack, keep all packed files: only turns the Automatically Pack Resources option off.
Selective Unpacking: unpack a single file by clicking the little "gift box" icon to the left of its file-path widget.
Options:
Remove Pack: just marks the file unpacked, without writing it or reloading it from drive.
Create &lt;local file path&gt; — unpacks the file to the proposed path, local to the current blend-file.
Use &lt;original file path&gt; (differs)|(identical) — if the original path still exists, marks it unpacked (it won't auto-reload from drive); (differs)/(identical) note whether the packed version and the on-drive one match.
Overwrite &lt;original file path&gt; — if the original path exists but differs from the packed version, marks it unpacked and overwrites the on-drive file with the packed one.
Create &lt;original file path&gt; — if the original path doesn't exist, marks it unpacked and writes it to drive.

Pack Linked Libraries - Reference: Panel: File ‣ External Data ‣ Pack Linked Libraries. Flags every linked library file in the current blend-file as packed; the actual packing happens on the next save.
Unpack Linked Libraries - Reference: Panel: File ‣ External Data ‣ Unpack Linked Libraries. Unpacks every linked library file used by this blend-file.

[Related references](INDEX.md).
