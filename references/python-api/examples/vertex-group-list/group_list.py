import bpy
from .drawing import draw_item, draw_filter
from .weights import filter_items_empty_vgroups
from .filtering import filter_items

class MESH_UL_vgroups_slow(bpy.types.UIList):
    # Constants (flags).
    # Be careful not to shadow FILTER_ITEM!
    VGROUP_EMPTY = 1 << 0

    # Custom properties, saved with `.blend` file.
    use_filter_empty: bpy.props.BoolProperty(
        name="Filter Empty",
        default=False,
        options=set(),
        description="Whether to filter empty vertex groups",
    )
    use_filter_empty_reverse: bpy.props.BoolProperty(
        name="Reverse Empty",
        default=False,
        options=set(),
        description="Reverse empty filtering",
    )
    use_filter_name_reverse: bpy.props.BoolProperty(
        name="Reverse Name",
        default=False,
        options=set(),
        description="Reverse name filtering",
    )
    use_filter_orderby_invert: bpy.props.BoolProperty(
        name="Reverse Order",
        default=False,
        options=set(),
        description="Reverse order filtering",
    )

    # This allows us to have mutually exclusive options, which are also all disable-able!
    def _gen_order_update(name1, name2):
        def _u(self, ctxt):
            if (getattr(self, name1)):
                setattr(self, name2, False)
        return _u
    use_order_name: bpy.props.BoolProperty(
        name="Name", default=False, options=set(),
        description="Sort groups by their name (case-insensitive)",
        update=_gen_order_update("use_order_name", "use_order_importance"),
    )
    use_order_importance: bpy.props.BoolProperty(
        name="Importance",
        default=False,
        options=set(),
        description="Sort groups by their average weight in the mesh",
        update=_gen_order_update("use_order_importance", "use_order_name"),
    )

    draw_item = draw_item
    draw_filter = draw_filter
    filter_items_empty_vgroups = filter_items_empty_vgroups
    filter_items = filter_items
