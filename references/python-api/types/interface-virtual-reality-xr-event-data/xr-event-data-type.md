# bpy.types.XrEventData: type

type 

The XR action's kind (default 'FLOAT' , readonly)

- FLOAT
Float – Float action, representing either a digital or analog button.

- VECTOR2D
Vector2D – 2D float vector action, representing a thumbstick or trackpad.

- POSE
Pose – 3D pose action, representing a controller’s location and rotation.

- VIBRATION
Vibration – Haptic vibration output action, to be applied with a duration, frequency, and amplitude.

Type :

Literal[‘FLOAT’, ‘VECTOR2D’, ‘POSE’, ‘VIBRATION’]

[Related references](INDEX.md).
