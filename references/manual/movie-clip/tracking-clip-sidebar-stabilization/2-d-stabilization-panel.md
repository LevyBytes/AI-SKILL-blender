# 2D Stabilization Panel

## 2D Stabilization Panel

2D stabilization removes handheld jitter.

Enable: toggle the switch AND turn on Show Stable (Clip Display pop-over). Then add tracking points.

Configure location and rotation/scale tracks; weighted averaging per group generates per-frame compensation.

For panning shots, Expected parameters (position/rotation/zoom) simulate intentional motion, restoring framing.

Activation: switch + Show Stable.

Options

2D Stabilization panel configuration.

Anchor Frame
Reference frame anchoring the stabilization; other frames adjust relative to this frame's position, orientation, and scale. Choose a frame where the subject appears optimally.

Stabilization Type

Rotation: Stabilizes detected rotation around the rotation pivot (weighted average of location tracks) in addition to position.

Scale: Compensates scale changes relative to rotation center.

Tracks for Stabilization

Location: Tracks compensating camera position jumps.

Rotation/Scale: Tracks compensating camera tilt and scale. May share location tracks but typically use distant, symmetrical points.

Autoscale: Computes minimal zoom eliminating image boundary artifacts.

Max: Limits autoscale magnitude.

Expected Position X/Y: Subtracts known shot offset (e.g., panning).

Expected Rotation: Compensates original shot rotation (e.g., tilting).

Expected Zoom: Scales the result to offset original zoom.

Influence
Controls how much compensating motion applies. Some jumps may intentionally remain uncompensated. These parameters affect only compensation motion (not deliberate Expected movements).

Interpolate
Stabilization uses sub-pixel accuracy; adjacent source pixels must combine for result pixels. Interpolation softens and degrades sharpness slightly.

Nearest: No interpolation; retains original sharpness but preserves sub-pixel jitter as 1-pixel steps.

Bilinear: Linear interpolation; quality/performance balance.

Bicubic: Highest quality; most computationally expensive.

[Related references](INDEX.md).
