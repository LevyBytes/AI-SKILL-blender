# blf: blf. bind_imbuf ( fontid , imbuf , * , display_name = None )

blf. bind_imbuf ( fontid , imbuf , * , display_name = None ) 

Context manager to draw text into an image buffer instead of the GPU's context.

Parameters :

- fontid ( int ) – The id of the typeface as returned by blf.load(), for default font use 0.

- imbuf (imbuf.types.ImBuf) – The image to draw into.

- display_name ( str | None ) – Ignored (formerly a color-space transform name), kept for backwards compatibility.

Returns :

The BLF ImBuf context manager.

Return type :

BLFImBufContext

[Related references](INDEX.md).
