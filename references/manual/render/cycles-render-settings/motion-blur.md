# Motion Blur

## Motion Blur

### Motion Blur

Reference

Panel :

Render ‣ Motion Blur

Standard Blender renders animations as still frames. While appropriate for stop-motion or time-lapse, real-world cameras capture moving subjects as blurred in their trajectory direction in both video and stills.

Motion blur example.
(blend-file)

Position
Specifies when the shutter activates relative to the current frame.

Start on Frame :

Shutter begins opening at the current frame.

Center on Frame :

Shutter is completely open at the current frame.

End on Frame :

Shutter fully closes at the current frame.

Shutter
Duration (in frames) from shutter open to fully closed. Example: 1.0 shutter time blurs across a single frame.

Rolling Shutter
Emulates a Rolling Shutter effect.

None :

No rolling shutter.

Top-Bottom :

Rolling shutter moves from image top to bottom.

Rolling Shutter Duration
Balances pure rolling shutter effect (zero value) against pure motion blur (one value).

Note

If scenes contain particles or physics simulations, bake them prior to rendering for correct and consistent motion blur.

See also

Individual object settings customize motion blur. Find these in the Object tab of the Properties. Consult object configuration for particulars.

### Shutter Curve

Curve controlling shutter opening and closing. X represents time; Y=0 indicates fully closed, Y=1 fully open. The default maps instantaneous open and close.

[Related references](INDEX.md).
