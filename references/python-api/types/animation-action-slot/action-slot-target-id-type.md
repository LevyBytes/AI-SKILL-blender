# bpy.types.ActionSlot.target_id_type

target_id_type

The type of data-block this slot is meant to animate; assignable when 'UNSPECIFIED' but otherwise read-only (default 'UNSPECIFIED')


| Value | Meaning |
| --- | --- |
| `ACTION` | Action. |
| `ARMATURE` | Armature. |
| `BRUSH` | Brush. |
| `CACHEFILE` | Cache File. |
| `CAMERA` | Camera. |
| `COLLECTION` | Collection. |
| `CURVE` | Curve. |
| `CURVES` | Curves. |
| `FONT` | Font. |
| `GREASEPENCIL` | Grease Pencil. |
| `GREASEPENCIL_V3` | Grease Pencil v3. |
| `IMAGE` | Image. |
| `KEY` | Key. |
| `LATTICE` | Lattice. |
| `LIBRARY` | Library. |
| `LIGHT` | Light. |
| `LIGHT_PROBE` | Light Probe. |
| `LINESTYLE` | Line Style. |
| `MASK` | Mask. |
| `MATERIAL` | Material. |
| `MESH` | Mesh. |
| `META` | Metaball. |
| `MOVIECLIP` | Movie Clip. |
| `NODETREE` | Node Tree. |
| `OBJECT` | Object. |
| `PAINTCURVE` | Paint Curve. |
| `PALETTE` | Palette. |
| `PARTICLE` | Particle. |
| `POINTCLOUD` | Point Cloud. |
| `SCENE` | Scene. |
| `SCREEN` | Screen. |
| `SOUND` | Sound. |
| `SPEAKER` | Speaker. |
| `TEXT` | Text. |
| `TEXTURE` | Texture. |
| `VOLUME` | Volume. |
| `WINDOWMANAGER` | Window Manager. |
| `WORKSPACE` | Workspace. |
| `WORLD` | World. |
| `UNSPECIFIED` | Unspecified – Not yet specified. When this slot is first assigned to a data-block, this will be set to the type of that data-block. |

Type: Literal['ACTION', 'ARMATURE', 'BRUSH', 'CACHEFILE', 'CAMERA', 'COLLECTION', 'CURVE', 'CURVES', 'FONT', 'GREASEPENCIL', 'GREASEPENCIL_V3', 'IMAGE', 'KEY', 'LATTICE', 'LIBRARY', 'LIGHT', 'LIGHT_PROBE', 'LINESTYLE', 'MASK', 'MATERIAL', 'MESH', 'META', 'MOVIECLIP', 'NODETREE', 'OBJECT', 'PAINTCURVE', 'PALETTE', 'PARTICLE', 'POINTCLOUD', 'SCENE', 'SCREEN', 'SOUND', 'SPEAKER', 'TEXT', 'TEXTURE', 'VOLUME', 'WINDOWMANAGER', 'WORKSPACE', 'WORLD', 'UNSPECIFIED']

[Related references](INDEX.md).
