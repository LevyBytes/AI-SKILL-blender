# bpy.types.UILayout: template_color_picker ( data , property , * , value_slider = False , lock = False , lock_luminosity = False , cubic = False )

template_color_picker ( data , property , * , value_slider = False , lock = False , lock_luminosity = False , cubic = False )

Item. A color-wheel control for choosing colors.

Parameters :

- data (AnyType) – Data from which to take property (never None)

- property ( str ) – Identifier of property in data (never None)

- value_slider ( bool ) – Display the value slider to the right of the color wheel (optional)

- lock ( bool ) – Lock the color wheel display to value 1.0 regardless of actual color (optional)

- lock_luminosity ( bool ) – Keep the color at its original vector length (optional)

- cubic ( bool ) – Cubic saturation for picking values close to white (optional)

[Related references](INDEX.md).
