# bpy.types.ActionConstraint: mix_mode

mix_mode

Method for combining existing transformations with the action channels (default '`AFTER_FULL`')

- REPLACE
Replace – Use the action channels instead of the original transformation.

- `BEFORE_FULL`
Before Original (Full) – Apply the action channels before the original transformation, as if applied to an invisible parent in Full Inherit Scale mode. Non-uniform scale and rotation combinations can create shear.

- BEFORE
Before Original (Aligned) – Apply the action channels before the original transformation, as if applied to an invisible parent in Aligned Inherit Scale mode. Full is applied to location; Split Channels is applied to rotation and scale.

- `BEFORE_SPLIT`
Before Original (Split Channels) – Apply the action channels before the original transformation, processing location, rotation and scale independently.

- `AFTER_FULL`
After Original (Full) – Apply the action channels after the original transformation, as if applied to an invisible child in Full Inherit Scale mode. Non-uniform scale and rotation combinations can create shear.

- AFTER
After Original (Aligned) – Apply the action channels after the original transformation, as if applied to an invisible child in Aligned Inherit Scale mode. Full is applied to location; Split Channels is applied to rotation and scale.

- `AFTER_SPLIT`
After Original (Split Channels) – Apply the action channels after the original transformation, processing location, rotation and scale independently.

Type: Literal['REPLACE', '`BEFORE_FULL`', 'BEFORE', '`BEFORE_SPLIT`', '`AFTER_FULL`', 'AFTER', '`AFTER_SPLIT`']

[Related references](INDEX.md).
