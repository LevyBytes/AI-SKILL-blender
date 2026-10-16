# bpy.types.Camera: panorama_type

panorama_type

Projection mode for panoramic rendering (default '`FISHEYE_EQUISOLID`' )

- EQUIRECTANGULAR
Equirectangular – Spherical camera for environment maps, also known as Lat Long panorama.

- `EQUIANGULAR_CUBEMAP_FACE`
Equiangular Cubemap Face – Single face of an equiangular cubemap.

- MIRRORBALL
Mirror Ball – Mirror ball mapping for environment maps.

- `FISHEYE_EQUIDISTANT`
Fisheye Equidistant – Ideal for fulldomes, ignore the sensor dimensions.

- `FISHEYE_EQUISOLID`
Fisheye Equisolid – Similar to most fisheye modern lens, takes sensor dimensions into consideration.

- `FISHEYE_LENS_POLYNOMIAL`
Fisheye Lens Polynomial – Defines the lens projection as polynomial to allow real world camera lenses to be mimicked.

- `CENTRAL_CYLINDRICAL`
Central Cylindrical – Projection onto a virtual cylinder from its center, similar as a rotating panoramic camera.

Type :

Literal['EQUIRECTANGULAR', '`EQUIANGULAR_CUBEMAP_FACE`', 'MIRRORBALL', '`FISHEYE_EQUIDISTANT`', '`FISHEYE_EQUISOLID`', '`FISHEYE_LENS_POLYNOMIAL`', '`CENTRAL_CYLINDRICAL`']

[Related references](INDEX.md).
