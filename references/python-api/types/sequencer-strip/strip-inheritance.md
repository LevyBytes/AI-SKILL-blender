# bpy.types.Strip: inheritance

## Strip(bpy_struct)

### Strip(bpy_struct)

base class — bpy_struct

subclasses —
EffectStrip, ImageStrip, MaskStrip, MetaStrip, MovieClipStrip, MovieStrip, SceneStrip, SoundStrip
class bpy.types. Strip ( bpy_struct )

One holder for a piece of media in the Video Sequence Editor.
### Inherited Properties

| Members | Members |
| --- | --- |
| bpy_struct.id_data | |
### Inherited Functions

| Members | Members |
| --- | --- |
| bpy_struct.as_pointer bpy_struct.driver_add bpy_struct.driver_remove bpy_struct.get bpy_struct.id_properties_clear bpy_struct.id_properties_ensure bpy_struct.id_properties_ui bpy_struct.is_property_hidden bpy_struct.is_property_overridable_library bpy_struct.is_property_readonly bpy_struct.is_property_set bpy_struct.items | bpy_struct.keyframe_delete bpy_struct.keyframe_insert bpy_struct.keys bpy_struct.path_from_id bpy_struct.path_from_module bpy_struct.path_resolve bpy_struct.pop bpy_struct.property_overridable_library_set bpy_struct.property_unset bpy_struct.rna_ancestors bpy_struct.type_recast bpy_struct.values |
### References

| Members | Members |
| --- | --- |
| bpy.context.active_strip bpy.context.selected_editable_strips bpy.context.selected_strips bpy.context.strip bpy.context.strips AddStrip.input_1 AddStrip.input_2 AlphaOverStrip.input_1 AlphaOverStrip.input_2 AlphaUnderStrip.input_1 AlphaUnderStrip.input_2 ColorMixStrip.input_1 ColorMixStrip.input_2 CrossStrip.input_1 CrossStrip.input_2 GammaCrossStrip.input_1 GammaCrossStrip.input_2 GaussianBlurStrip.input_1 GlowStrip.input_1 MetaStrip.strips MultiplyStrip.input_1 MultiplyStrip.input_2 SequenceEditor.active_strip SequenceEditor.display_stack SequenceEditor.meta_stack SequenceEditor.strips SequenceEditor.strips_all SpeedControlStrip.input_1 Strip.move_to_meta Strip.parent_meta | Strip.split Strip.swap StripModifier.input_mask_strip StripsMeta.new_clip StripsMeta.new_effect StripsMeta.new_effect StripsMeta.new_effect StripsMeta.new_image StripsMeta.new_mask StripsMeta.new_meta StripsMeta.new_movie StripsMeta.new_scene StripsMeta.new_sound StripsMeta.remove StripsTopLevel.new_clip StripsTopLevel.new_effect StripsTopLevel.new_effect StripsTopLevel.new_effect StripsTopLevel.new_image StripsTopLevel.new_mask StripsTopLevel.new_meta StripsTopLevel.new_movie StripsTopLevel.new_scene StripsTopLevel.new_sound StripsTopLevel.remove SubtractStrip.input_1 SubtractStrip.input_2 WipeStrip.input_1 WipeStrip.input_2 |

[Related references](INDEX.md).
