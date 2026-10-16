# bpy.types.UILayout: template_icon_view ( data , property , * , show_labels = False , scale = 6.0 , scale_popup = 5.0 )

template_icon_view ( data , property , * , show_labels = False , scale = 6.0 , scale_popup = 5.0 )

Enum. A large widget that displays icon previews.

Parameters :

- data (AnyType) – Data from which to take property (never None)

- property ( str ) – Identifier of property in data (never None)

- show_labels ( bool ) – Show enum label in preview buttons (optional)

- scale ( float ) – UI Units, Scale the button icon size (by the button size) (in [1, 100], optional)

- scale_popup ( float ) – Scale, Scale the popup icon size (by the button size) (in [1, 100], optional)

[Related references](INDEX.md).
