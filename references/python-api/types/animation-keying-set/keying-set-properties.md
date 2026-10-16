# bpy.types.KeyingSet: properties

## KeyingSet(bpy_struct)

### KeyingSet(bpy_struct)

base class — bpy_struct
class bpy.types. KeyingSet ( bpy_struct )

A group of settings meant to be keyframed at once.
bl_description

A brief description of the keying set (default “”, never None)

Type :

str
bl_idname

When set, the Keying Set is given a custom ID; otherwise it inherits the name of the class that defines it (for instance, with a class named “`BUILTIN_KSI`_location” and no bl_idname set by the script, bl_idname becomes “`BUILTIN_KSI`_location”) (default “”, never None)

Type :

str
bl_label

(default “”, never None)

Type :

str
is_path_absolute

The Keying Set names explicit paths/settings to keyframe (i.e. it does not depend on context info) (default False, readonly)

Type :

bool
paths

The Keying Set Paths that name the settings keyframed together (default None, readonly)

Type :

KeyingSetPaths[KeyingSetPath]
type_info

The callback function definitions for built-in Keying Sets (readonly)

Type :

KeyingSetInfo
use_insertkey_needed

Add keyframes only on the F-Curves that actually need them (default False)

Type :

bool
use_insertkey_override_needed

Override the default so keyframes go only on the F-Curves that need them (default False)

Type :

bool
use_insertkey_override_visual

Override the default so keyframes are taken from ‘visual transforms’ (default False)

Type :

bool
use_insertkey_visual

Take keyframes from ‘visual transforms’ (default False)

Type :

bool

[Related references](INDEX.md).
