# bpy.types.SpaceNLA: properties

## SpaceNLA(Space)

### SpaceNLA(Space)

base classes: bpy_struct, Space
class bpy.types. SpaceNLA ( Space )

The space data for the NLA editor
dopesheet

Options that filter the animation data (readonly)

Type :

DopeSheet
show_local_markers

Draw action-local markers on the strips, handy for lining up timing between strips (default True)

Type :

bool
show_markers

If any are defined, give markers a dedicated strip along the editor's lower edge (default False)

Type :

bool
show_region_channels

(default False)

Type :

bool
show_region_footer

(default False)

Type :

bool
show_region_hud

(default False)

Type :

bool
show_region_ui

(default False)

Type :

bool
show_seconds

Label timing with timecode rather than frame numbers (default False)

Type :

bool
show_strip_curves

Draw the influence F-Curves on the strips (default True)

Type :

bool
use_realtime_update

While strips are being transformed, push the animation-data changes through to other views (default True)

Type :

bool

[Related references](INDEX.md).
