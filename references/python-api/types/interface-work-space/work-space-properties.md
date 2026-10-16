# bpy.types.WorkSpace: properties

## WorkSpace(ID)

### WorkSpace(ID) 

base classes — bpy_struct, ID
class bpy.types. WorkSpace ( ID ) 

A data-block that lays out the user's working environment
active_addon 

Index of the active add-on within the Workspace add-ons filter (in [-inf, inf], default 0)

Type :

int
asset_library_reference 

Asset library currently shown in the UI; the Asset Browser tracks its own selection separately from this (default 'ALL' )

- ALL
All Libraries – Show assets from all of the listed asset libraries.

- LOCAL
Current File – Show the assets currently available in this Blender session.

- ESSENTIALS
Essentials – Show the basic building blocks and utilities coming with Blender.

- CUSTOM
Custom – Show assets from the asset libraries configured in the Preferences.

Type :

Literal[‘ALL’, ‘LOCAL’, ‘ESSENTIALS’, ‘CUSTOM’]
object_mode 

Object mode entered automatically when this workspace becomes active (default 'OBJECT' )

Type :

Literal[Workspace Object Mode Items]
owner_ids 

(default None, readonly)

Type :

wmOwnerIDs[wmOwnerID]
screens 

The screen layouts belonging to this workspace (default None, readonly)

Type :

bpy_prop_collection[Screen]
sequencer_scene 

Type :

Scene
tools 

(default None, readonly)

Type :

wmTools[WorkSpaceTool]
use_filter_by_owner 

Restrict what the UI shows according to tags (default False)

Type :

bool
use_pin_scene 

Keep track of the workspace's last scene and return to it each time the workspace is reopened (default False)

Type :

bool
use_scene_time_sync 

Drive the active scene and current time from the active scene strip (default False)

Type :

bool

[Related references](INDEX.md).
