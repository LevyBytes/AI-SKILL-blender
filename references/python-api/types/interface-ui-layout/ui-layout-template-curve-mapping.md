# bpy.types.UILayout: template_curve_mapping ( data , property , * , type = 'NONE' , levels = False , brush = False , use_negative_slope = False , show_tone = False , show_presets = False )

template_curve_mapping ( data , property , * , type = 'NONE' , levels = False , brush = False , use_negative_slope = False , show_tone = False , show_presets = False )

Item. A curve-mapping control, useful for things like light falloff curves.

Parameters :

- data (AnyType) – Data from which to take property (never None)

- property ( str ) – Identifier of property in data (never None)

- type ( Literal [ 'NONE' , 'VECTOR' , 'COLOR' , 'HUE' ] ) – Type, Type of curves to display (optional)

- levels ( bool ) – Show black/white levels (optional)

- brush ( bool ) – Show brush options (optional)

- use_negative_slope ( bool ) – Use a negative slope by default (optional)

- show_tone ( bool ) – Show tone options (optional)

- show_presets ( bool ) – Show preset options (optional)

[Related references](INDEX.md).
