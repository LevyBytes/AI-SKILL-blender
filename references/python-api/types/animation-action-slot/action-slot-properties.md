# bpy.types.ActionSlot properties

active

Whether this is the current slot, may be set by assigning to action.slots.active (default False, readonly)

Type: bool
handle

A number specific to this Slot, unique within the Action. This is used, for instance, on a ActionKeyframeStrip to look up the ActionChannelbag for this Slot

([-inf, inf], default 0, readonly)

Type: int
identifier

Used when linking an Action to a data-block, to locate the proper slot handle. This is the UI name, prepended by two characters determined by the slot's ID type (default "", never None)

Type: str
name_display

The display name of the slot. This name together with the slot's data-block type is unique within its Action (default "", never None)

Type: str
select

Whether the slot is selected (default False)

Type: bool
show_expanded

Whether the slot is expanded (default False)

Type: bool

target_id_type_icon

([-inf, inf], default 0, readonly)

Type: int

[bpy.types.ActionSlot.target_id_type](action-slot-target-id-type.md).

[Related references](INDEX.md).
