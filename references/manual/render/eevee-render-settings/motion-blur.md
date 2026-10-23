# Motion Blur

### Limitations

- Orthographic Cameras do not support camera motion blur.

- Light motion is disregarded in motion blur calculations.

Motion Blur: Temporal Shutter

Reference
Panel: Render ‣ Motion Blur

Blender renders animations as still image sequences by default. While suitable for stop-motion and time-lapses, this diverges from reality; fast motion exhibits directional blur, visible in film frames and photographs.

Note
Viewport motion blur during animation playback uses a simpler algorithm than final render. Viewport Renders use the same algorithm.

Position
Controls when the shutter opens relative to the current frame.

Start on Frame:
Shutter begins opening at the current frame.

Center on Frame:
Shutter is fully open at the current frame.

End on Frame:
Shutter closes at the current frame.

Shutter
Duration (in frames) between shutter open and close.

Bleeding Bias
Used by post-process blur to prevent background blur onto foreground surfaces. Lower values reduce foreground contamination.

Max Blur
Intended as optimization by limiting the pixel distance across which blur is computed.

Steps
Accumulation blur accuracy control; higher counts increase render duration. More steps improve quality.

Note
Multiple time steps round the render sample count up to the next Steps multiple, ensuring even sample distribution. This can lower jitter camera depth of field quality. Increase viewport or render samples to restore quality.

EEVEE splits rendering into multiple time steps and accumulates results, called Accumulation Motion Blur. This approach is precise but requires numerous steps for smooth gradients. Combined with post-process blur for inter-step gaps, each step demands full scene re-evaluation, adding overhead. Increasing steps also allows reducing Max Blur as post-process blur covers less distance.

Shutter Curve
Enable custom shutter curve.

### Example

| No motion blur applied. | Post-process blur only. |
| --- | --- |
| 4 time steps without post-process blur. | 4 time steps with post-process blur. |
| 32 time steps without post-process blur. | 32 time steps with post-process blur. |

[Related references](INDEX.md).
