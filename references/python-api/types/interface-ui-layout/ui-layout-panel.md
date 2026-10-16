# bpy.types.UILayout: panel, panel_prop

panel ( idname , * , default_closed = False ) 

Creates a collapsible panel. Whether it is open or closed is stored in the region using the given idname. This can only be used when the panel has the full width of the panel region available to it. So it can’t be used in e.g. in a box or columns.

Parameters :

- idname ( str ) – Identifier of the panel (never None)

- default_closed ( bool ) – Open by Default, When true, the panel will be open the first time it is shown (optional)

Returns :

layout_header , Sub-layout to put items in, UILayout

layout_body , Sub-layout to put items in. Will be none if the panel is collapsed., UILayout

Return type :

tuple[UILayout, UILayout]
panel_prop ( data , property ) 

Similar to .panel(...) but instead of storing whether it is open or closed in the region, it is stored in the provided boolean property. This should be used when multiple instances of the same panel can exist. For example one for every item in a collection property or list. This can only be used when the panel has the full width of the panel region available to it. So it can’t be used in e.g. in a box or columns.

Parameters :

- data (AnyType) – Data from which to take the open-state property (never None)

- property ( str ) – Identifier of the boolean property that determines whether the panel is open or closed (never None)

Returns :

layout_header , Sub-layout to put items in, UILayout

layout_body , Sub-layout to put items in. Will be none if the panel is collapsed., UILayout

Return type :

tuple[UILayout, UILayout]

[Related references](INDEX.md).
