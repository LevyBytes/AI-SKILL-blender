# bpy.types.RenderSettings: motion_blur_position, motion_blur_shutter, motion_blur_shutter_curve

motion_blur_position

Shifts the shutter's time window, which alters where the motion blur trails fall (default 'CENTER' )

- START
Start on Frame – The shutter begins opening at the current frame.

- CENTER
Center on Frame – The shutter stays open across the current frame.

- END
End on Frame – The shutter finishes closing at the current frame.

Type :

Literal[‘START’, ‘CENTER’, ‘END’]
motion_blur_shutter

Frames of elapsed time spanning shutter open to shutter close (in [0, inf], default 0.5)

Type :

float
motion_blur_shutter_curve

Curve describing how open the shutter is across time (readonly)

Type :

CurveMapping

[Related references](INDEX.md).
