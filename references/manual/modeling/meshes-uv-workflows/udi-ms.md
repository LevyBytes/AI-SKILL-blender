# UDIMs

## UDIMs

UV coordinate systems have a limitation: a single texture covers the entire model at one resolution. When geometry varies significantly in size and importance, this causes problems—smaller regions waste texture resolution while large regions lack sufficient pixel density.

UDIMs solve this by partitioning UV space across multiple texture images. Each tile is a separate texture in a grid. Within each tile, UV coordinates span from 0 to 1 (or 1 to 2, 2 to 3, etc. by column), and each tile receives its own image. Multiple textures of different resolutions can be assigned per tile—for instance, 4k for primary surface details, 2k and 1k for secondary regions.

The main tile carries index 1001. Adding tiles increments this: 1002 appears to the right, up to 1010 in the first row. Subsequent rows begin at 1011 directly above the main tile.

Start with an unwrapped model as you would for standard UV mapping. Decide on the number of textures needed—a reasonable starting point is three: 4k, 2k, and 1k resolutions. Create corresponding images.

Move UV islands to their assigned tiles and manage them like a standard layout. Once correctly positioned, add proper textures to tiles. Existing images cannot be directly placed into tiles; instead, create the tile, save it, then replace the saved file with the desired texture (either by overwriting the file or editing it in external software).

In addition to external editing, painting directly on UDIM textures is supported in both 2D and 3D painting modes.

Filenames can include special placeholders that expand based on the tile being loaded or saved. These tokens, enclosed in angle brackets, enable automatic tile identification.

`<UDIM>` becomes a four-digit code calculated as 1001 plus the u-tile index plus (v-tile index times 10). `<UVTILE>` expands to the format u(u-value)_v(v-value). For example, `texture.<UDIM>.png` might expand to `texture.1021.png`, while `texture.<UVTILE>.png` becomes `texture.u1_v3.png`.

The UDIM Tiles panel is used in the Image Editor or UV Editor to manage tiles—add new ones, delete existing ones, or fill them with generated content.

The panel shows all tiles linked to the primary 1000-index tile. Double-clicking a tile name allows renaming it for clarity.

Add Tile lets you specify a starting index and count. Tiles must begin at 1001 and typically ascend sequentially.

An optional label can be displayed in the viewport instead of the numeric index.

Fill occupies a tile with a generated image.

Remove Tile deletes a selected tile and its contents if unsaved.

Note: unfilled tiles are not saved.

[Related references](INDEX.md).
