# bpy.types.XrEventData: controller_location, controller_location_other, controller_rotation, controller_rotation_other

controller_location 

World-space position of the controller aim tied to the action (array of 3 items, in [-inf, inf], default (0.0, 0.0, 0.0), readonly)

Type :

mathutils.Vector
controller_location_other 

Aim position of the other user path during bimanual actions (array of 3 items, in [-inf, inf], default (0.0, 0.0, 0.0), readonly)

Type :

mathutils.Vector
controller_rotation 

World-space orientation of the controller aim tied to the action (array of 4 items, in [-inf, inf], default (0.0, 0.0, 0.0, 0.0), readonly)

Type :

mathutils.Quaternion
controller_rotation_other 

Aim orientation of the other user path during bimanual actions (array of 4 items, in [-inf, inf], default (0.0, 0.0, 0.0, 0.0), readonly)

Type :

mathutils.Quaternion

[Related references](INDEX.md).
