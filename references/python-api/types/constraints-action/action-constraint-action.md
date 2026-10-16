# bpy.types.ActionConstraint: action, action_slot, action_slot_handle, action_suitable_slots

action

The constraining action

Type: Action
action_slot

The slot identifying which subset of the Action applies to this strip; its name is used to locate the slot when a new Action is assigned

Type: ActionSlot
action_slot_handle

A number identifying which subset of the Action applies to this Action Constraint ([-inf, inf], default 0)

Type: int
action_suitable_slots

The set of action slots suitable for this NLA strip (default None, readonly)

Type: bpy_prop_collection[ActionSlot]

[Related references](INDEX.md).
