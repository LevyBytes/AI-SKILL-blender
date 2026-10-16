# bpy.types.IDOverrideLibrary: properties

## IDOverrideLibrary(bpy_struct)

### IDOverrideLibrary(bpy_struct)

base class — bpy_struct
class bpy.types. IDOverrideLibrary ( bpy_struct )

Bundles together everything an overridden linked ID needs.
hierarchy_root

The override ID that sits at the top of the override hierarchy to which this ID belongs (readonly)

Type :

ID
is_in_hierarchy

Tells whether this override belongs to a library hierarchy or stands alone as a self-contained, independent override (default True)

Type :

bool
is_system_override

Tells whether the override is there purely to serve the hierarchy or is genuinely something the user can edit (default False)

Type :

bool
properties

List of overridden properties (default None, readonly)

Type :

IDOverrideLibraryProperties[IDOverrideLibraryProperty]
reference

The linked ID this override treats as its reference (readonly)

Type :

ID

[Related references](INDEX.md).
