# bpy.ops.uv.export_layout

bpy.ops.uv. export_layout ( * , filepath = '' , export_all = False , export_tiles = 'NONE' , modified = False , mode = 'PNG' , size = (1024, 1024) , opacity = 0.25 , check_existing = True ) 

Writes the UV layout out to a file

Parameters :

- filepath ( str ) – filepath, (optional, never None)

- export_all ( bool ) – All UVs, Export all UVs in this mesh (not just visible ones) (optional)

- export_tiles ( Literal [ 'NONE' , 'UDIM' , 'UV' ] ) – Export Tiles, Choose whether to export only the [0, 1] range, or all UV tiles (optional)

- NONE
None – Write out only the UVs that fall in the [0, 1] range.

- UDIM
UDIM – Write tiles using the UDIM numbering scheme: 1001 + u_tile + 10*v_tile.

- UV
UVTILE – Write tiles using the UVTILE numbering scheme: u(u_tile + 1)_v(v_tile + 1).

- modified ( bool ) – Modified, Exports UVs from the modified mesh (optional)

- mode ( Literal [ 'SVG' , 'EPS' , 'PNG' ] ) – Format, File format to export the UV layout to (optional)

- SVG
Scalable Vector Graphic (.svg) – Save the UV layout as a vector SVG file.

- EPS
Encapsulated PostScript (.eps) – Save the UV layout as a vector EPS file.

- PNG
PNG Image (.png) – Save the UV layout as a bitmap image.

- size ( Sequence [ int ] ) – Size, Dimensions of the exported file (array of 2 items, in [8, 32768], optional)

- opacity ( float ) – Fill Opacity, Set amount of opacity for exported UV layout (in [0, 1], optional)

- check_existing ( bool ) – check_existing, (optional)

Returns :

Result of the operator call.

Return type :

set[Literal[Operator Return Items]]

File :

addons_core/io_mesh_uv_layout/__init__.py:139

[Related references](INDEX.md).
