# Usual draw item function.
def draw_item(self, context, layout, data, item, icon, active_data, active_propname, index, flt_flag):
    # Just in case, we do not use it here!
    self.use_filter_invert = False

    # assert(isinstance(item, bpy.types.VertexGroup)
    vgroup = item
    # Here we use one feature of new filtering feature: it can pass data to draw_item, through flt_flag
    # parameter, which contains exactly what filter_items set in its filter list for this item!
    # In this case, we show empty groups grayed out.
    if flt_flag & self.VGROUP_EMPTY:
        col = layout.column()
        col.enabled = False
        col.alignment = 'LEFT'
        col.prop(vgroup, "name", text="", emboss=False, icon_value=icon)
    else:
        layout.prop(vgroup, "name", text="", emboss=False, icon_value=icon)
    icon = 'LOCKED' if vgroup.lock_weight else 'UNLOCKED'
    layout.prop(vgroup, "lock_weight", text="", icon=icon, emboss=False)

def draw_filter(self, context, layout):
    # Nothing much to say here, it's usual UI code...
    row = layout.row()

    subrow = row.row(align=True)
    subrow.prop(self, "filter_name", text="")
    icon = 'ZOOM_OUT' if self.use_filter_name_reverse else 'ZOOM_IN'
    subrow.prop(self, "use_filter_name_reverse", text="", icon=icon)

    subrow = row.row(align=True)
    subrow.prop(self, "use_filter_empty", toggle=True)
    icon = 'ZOOM_OUT' if self.use_filter_empty_reverse else 'ZOOM_IN'
    subrow.prop(self, "use_filter_empty_reverse", text="", icon=icon)

    row = layout.row(align=True)
    row.label(text="Order by:")
    row.prop(self, "use_order_name", toggle=True)
    row.prop(self, "use_order_importance", toggle=True)
    icon = 'TRIA_UP' if self.use_filter_orderby_invert else 'TRIA_DOWN'
    row.prop(self, "use_filter_orderby_invert", text="", icon=icon)
