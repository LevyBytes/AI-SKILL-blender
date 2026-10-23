# Asset Catalogs

## Asset Catalogs

Asset Catalogs help you organize your assets. They resemble file directories a little, but they're entirely independent of where your blend-files sit. Assign each asset in a blend-file to its own catalog, or keep one big catalog holding every asset from every blend-file — it's up to you. Like Collections, catalogs can be nested: a main catalog can contain several nested catalogs, so you might have a "Furniture" catalog with "Tables", "Chairs", "Lamps", and other sub-catalogs. For deeper technical detail, see Asset Catalogs in the Blender Developer Documentation.

The Home Location of Assets — you may have any number of catalogs, yet an asset belongs to only one of them at a time, much like a file in a single directory (ignoring tricks like symbolic links). Catalogs themselves can be nested and rearranged by drag-and-drop; moving a catalog leaves its assets alone, they simply travel to the catalog's new spot. Selecting a catalog in the Asset Browser shows every asset in it and in its child catalogs — so in the earlier example, selecting Characters/Ellie/Poses also shows assets from Characters/Ellie/Poses/Head and Characters/Ellie/Poses/Hands.

Creating Catalogs: make new catalogs in the Asset Browser via Header ‣ Catalog ‣ New Asset Catalog; once created, double-LMB its name in the editor's Source List region to give it a more descriptive name. You can also create catalogs in that region by clicking the plus icon at the top of the Tree View.

Assigning an Asset: to assign assets to a catalog, just select them and drag them onto the catalog. Tip: assigning an asset to the "Unassigned" catalog strips it from any catalogs it was in.

Saving Catalogs: saving makes any catalog edits permanent by writing the current setup to the asset library. Save catalogs in the Asset Browser via Header ‣ Catalog ‣ Save Asset Catalog, or in the editor's Source List region by clicking the save icon at the top of the Tree View.

Components of a Catalog: each catalog has a catalog path, a UUID, and a simple name. Normally you only handle the catalog path; the rest is for internal Blender use and/or emergencies.
Catalog Path: the path sets where in the hierarchy the catalog appears. Examples like Characters/Ellie/Poses/Hand or Kitbash/City/Skyscrapers produce a corresponding catalog tree; the highlighted catalog has path Characters/Ellie/Poses/Hand.
UUID — each catalog carries a UUID, normally hidden from the UI (switch on Developer Extras plus the experimental Asset Debug Info option to reveal them). It's what gets stored in the asset and what fixes the catalog's "identity", so a catalog can be renamed or moved (its path changed) and all its assets travel along — only the catalog itself changes, not any asset blend-file.
Simple Name: every catalog may carry an optional simple name, kept beside the UUID in each asset; its point is to let a human recognize the catalog an asset was assigned to even if the catalog definition file (below) is lost. Like the UUID, it's normally hidden from the UI; enable Developer Extras in the interface preferences to show it in the Asset Browser.

Catalog Definition Files: asset catalogs live in Catalog Definition Files (CDFs). Blender 3.0 supports one CDF per asset library, stored as blender_assets.cats.txt in the library's root directory. If the file is missing, Blender creates it when catalogs are saved; when catalogs change, Blender updates that file and also writes a backup of the previous state to blender_assets.cats.txt~.
Which File to Write To: asset catalogs are saved apart from the blend-file; the catalog editor carries its own "Save" button.
Format: CDFs are fairly simple text files in UTF-8: a version indicator plus one line of text per catalog, each line colon-separated in the form {UUID}:{path}:{simple name}.
Example: a valid catalog definition file:
```text
# This is an Asset Catalog Definition file for Blender.
#
# Empty lines and lines starting with `#` will be ignored.
# The first non-ignored line should be the version indicator.
# Subsequent lines are of the format "CATALOG_UUID:catalog/path/for/assets:simple catalog name"

VERSION 1

313ea471-7c81-4de6-af81-fb04c3535d0e:catalog/without/simple/name:
ee9c7b60-02f1-4058-bed6-539b8d2a6d34:character/Ellie/poselib:character-Ellie-poselib
cd66bf52-58f4-45cb-a4e2-dc0e0ee8f3fe:character/Ellie/poselib:character-Ellie
4eb44ec6-3424-405b-9782-ca006953e799:character/Ellie/poselib/white space:character-Ellie-poselib-white space
b63ed357-2511-4b96-8728-1b5a7093824c:character/Ružena/poselib:Ružena pose library
dcdee4df-926e-4d72-b995-33106983bb9a:character/Ružena/poselib/face:Ružena face
fb698f2e-9e2b-4146-a539-3af292d44899:character/Ružena/poselib/hand:Ružena hands
```
Valid Catalog Paths - paths obey these rules:
- Every path is absolute; /a/b and a/b are the same.
- Only / as the separator (no \; think less filesystem path, more URL).
- Not empty (a valid catalog needs one).
- No empty components (so not a//b; a/b is fine).
- Invalid characters: :, , \.
- Paths are always read as UTF-8.

[Related references](INDEX.md).
