# bpy.types.Camera: sensor_fit, sensor_height, sensor_width

sensor_fit

Aspect scaling method (default 'AUTO' )

- AUTO
Auto – Fit to the sensor width or height depending on image resolution.

- HORIZONTAL
Horizontal – Fit to the sensor width.

- VERTICAL
Vertical – Fit to the sensor height.

Type :

Literal['AUTO', 'HORIZONTAL', 'VERTICAL']
sensor_height

Vertical sensor dimensions in millimeters (in [1, inf], default 24.0)

Type :

float
sensor_width

Horizontal sensor dimensions in millimeters (in [1, inf], default 36.0)

Type :

float

[Related references](INDEX.md).
