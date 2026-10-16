# bpy.types.ImageTexture: extension

extension

What happens to the image beyond its original bounds (default 'REPEAT' )

- EXTEND
Extend – Carry the image's edge pixels outward.

- CLIP
Clip – Limit to the image size and make pixels outside it transparent.

- `CLIP_CUBE`
Clip Cube – Limit to a cube-shaped region around the image and make pixels outside it transparent.

- REPEAT
Repeat – Tile the image across both horizontally and vertically.

- CHECKER
Checker – Tile the image in a checkerboard arrangement.

Type :

Literal[‘EXTEND’, ‘CLIP’, ‘`CLIP_CUBE`’, ‘REPEAT’, ‘CHECKER’]

[Related references](INDEX.md).
