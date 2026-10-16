# bpy.types.Panel: bl_options

bl_options

Per-panel-type option flags (default set())

- `DEFAULT_CLOSED`
Default Closed – Decides whether the panel starts expanded or collapsed when first created.

- `HIDE_HEADER`
Hide Header – When False, a header is drawn carrying the collapse arrow and the label (see bl_label).

- INSTANCED
Instanced Panel – Lets several panels of this kind act as a list backed by data outside the UI. Powers the panels behind the modifier and similar stacks..

- `HEADER_LAYOUT_EXPAND`
Expand Header Layout – Lets header buttons grow or shrink so they span the full layout width.

Type :

set[Literal[‘`DEFAULT_CLOSED`’, ‘`HIDE_HEADER`’, ‘INSTANCED’, ‘`HEADER_LAYOUT_EXPAND`’]]

[Related references](INDEX.md).
