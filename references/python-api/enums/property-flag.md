# Property Flag Items

## Property Flag Items

### Property Flag Items

`READ_ONLY` :

Read Only.

While active, the property stays uneditable.

HIDDEN :

Hidden.

For operators: keep it out of the spots where Blender would auto-insert the property, such as Adjust Last Operation. The property is also left out of presets..

`SKIP_SAVE` :

Skip Save.

For operators: the property's value is not carried over from one invocation to the next; every run begins from the default instead. The property is also left out of presets..

`SKIP_PRESET` :

Skip Preset.

Leave it out of presets.

ANIMATABLE :

Animatable.

`LIBRARY_EDITABLE` :

Library Editable.

This property stays editable even on linked data (normally read-only). Be aware that such edits are not stored in the blend file..

PROPORTIONAL :

Adjust values proportionally to each other.

`TEXTEDIT_UPDATE` :

Update on every keystroke in textedit ‘mode’.

`OUTPUT_PATH` :

Output Path.

`PATH_SUPPORTS_BLEND_RELATIVE` :

Relative Path Support.

This path accepts the relative “//” prefix, which expands to the folder holding the current “.blend” file..

`SUPPORTS_TEMPLATES` :

Variable expression support.

This path accepts the “{variable_name}” template syntax, swapping in the referenced variable's value wherever the template expression appears.

[Related references](INDEX.md).
