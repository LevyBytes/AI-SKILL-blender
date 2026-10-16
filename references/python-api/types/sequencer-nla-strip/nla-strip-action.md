# bpy.types.NlaStrip: action, action_frame_end, action_frame_start, action_slot, action_slot_handle, action_suitable_slots

action

The Action this strip points to

Type :

Action
action_frame_end

Final frame of the action that gets used (in [-inf, inf], default 0.0)

Type :

float
action_frame_start

Initial frame of the action that gets used (in [-inf, inf], default 0.0)

Type :

float
action_slot

Picks out which portion of the Action belongs to this strip; its name is what gets matched when a different Action is assigned

Type :

ActionSlot
action_slot_handle

A numeric handle marking which portion of the Action is meant for this NLA strip (in [-inf, inf], default 0)

Type :

int
action_suitable_slots

Action slots that would work for this NLA strip (default None, readonly)

Type :

bpy_prop_collection[ActionSlot]

[Related references](INDEX.md).
