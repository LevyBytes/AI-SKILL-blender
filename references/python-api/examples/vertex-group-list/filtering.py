import bpy

def filter_items(self, context, data, propname):
    # This function gets the collection property (as the usual tuple (data, propname)), and must return two lists:
    # * The first one is for filtering, it must contain 32bit integers were self.bitflag_filter_item marks the
    #   matching item as filtered (i.e. to be shown). The upper 16 bits (including `self.bitflag_filter_item`) are
    #   reserved for internal use, the lower 16 bits are free for custom use. Here we use the first bit to mark
    #   VGROUP_EMPTY.
    # * The second one is for reordering, it must return a list containing the new indices of the items (which
    #   gives us a mapping `org_idx -> new_idx`).
    # Please note that the default UI_UL_list defines helper functions for common tasks (see its doc for more info).
    # If you do not make filtering and/or ordering, return empty list(s) (this will be more efficient than
    # returning full lists doing nothing!).
    vgroups = getattr(data, propname)
    helper_funcs = bpy.types.UI_UL_list

    # Default return values.
    flt_flags = []
    flt_neworder = []

    # Pre-compute of vertex-groups data, unfortunately this is CPU-intensive.
    vgroups_empty = self.filter_items_empty_vgroups(context, vgroups)

    # Filtering by name.
    if self.filter_name:
        flt_flags = helper_funcs.filter_items_by_name(self.filter_name, self.bitflag_filter_item, vgroups, "name",
                                                      reverse=self.use_filter_name_reverse)
    if not flt_flags:
        flt_flags = [self.bitflag_filter_item] * len(vgroups)

    # Filter by emptiness.
    for idx, vg in enumerate(vgroups):
        if vgroups_empty[vg.index][0]:
            flt_flags[idx] |= self.VGROUP_EMPTY
            if self.use_filter_empty and self.use_filter_empty_reverse:
                flt_flags[idx] &= ~self.bitflag_filter_item
        elif self.use_filter_empty and not self.use_filter_empty_reverse:
            flt_flags[idx] &= ~self.bitflag_filter_item

    # Reorder by name or average weight.
    if self.use_order_name:
        flt_neworder = helper_funcs.sort_items_by_name(vgroups, "name")
        if self.use_filter_orderby_invert:
            flt_neworder = [len(flt_neworder) - 1 - rank for rank in flt_neworder]
    elif self.use_order_importance:
        _sort = [(idx, vgroups_empty[vg.index][1]) for idx, vg in enumerate(vgroups)]
        highest_first = not self.use_filter_orderby_invert
        flt_neworder = helper_funcs.sort_items_helper(_sort, lambda e: e[1], highest_first)

    return flt_flags, flt_neworder
