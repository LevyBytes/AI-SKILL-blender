# Speaker Objects: Cone, Animation, Custom Properties

### Cone 

Directional speaker behavior settings.

Picture a cone emanating from the speaker's origin, aligned with the speaker's forward direction. Audio propagates directionally via inner and outer cone zones. Cone angles define their opening spread, where 360° creates a fully open cone with no directionality.

- Inside the inner cone : Maximum volume.

- Between the inner and outer cone : Linear interpolation of volume.

- Outside the outer cone : Volume follows the Outer Cone Volume setting.

Angle Outer
The outer cone opening angle in degrees. Beyond this boundary, Outer Cone Volume dictates the output level.

Angle Inner
The inner cone opening angle in degrees. Full volume is maintained within this region.

Outer Cone Volume
Loudness outside the outer cone. Smaller values increase directionality.

### Animation 

Controls animation metadata for scene-wide properties, including active Actions and their designated Slot.

See Manually Assigning Actions and Slots for further information.

### Custom Properties 

Define and organize custom attributes to store data on the action's data block. Refer to the Custom Properties page for complete details.

[Related references](INDEX.md).
