# F-Curve Properties

## F-Curve Properties

Active F-Curve — Reference: Panel: Sidebar region ‣ F-Curve ‣ Active F-Curve. Shows the active F-Curve's properties.
Channel Name — the name of the property the curve animates.
Data Path — the programmatic path to that property.
RNA Array Index — for a multi-value property, which element this curve drives; Location, for instance, has three values (X, Y, Z), so it can hold three curves with indices 0, 1, and 2.
Display Color — how the F-Curve's color in the Graph editor is decided. Auto Rainbow gives every curve using this setting a distinct color; Auto XYZ to RGB spots curves animating an X/Y/Z coordinate and colors them red/green/blue; User Defined lets you choose.
Handle Smoothing — how the Bézier handles are computed under the Automatic or Auto Clamped handle type.
  None — only the immediately adjacent key values feed the handle computation. This older method is simple and predictable but only produces truly smooth curves in trivial cases (notice the kinks in the middle of the red curve above).
  Continuous Acceleration — solves a system of equations to avoid or minimize acceleration jumps at each keyframe. It yields far smoother curves out of the box, but any change to key values can affect interpolation over a long stretch of curve, though the effect decays exponentially with distance; that propagation is halted by any key with Free, Aligned, or Vector handles, and by extremes with Auto Clamped handles. This mode also tends to overshoot and oscillate more with fully Automatic handles, so prefer Auto Clamped by default and switch to Automatic only where you want that behavior; adding in-between keys also tames it.
  Tip: weighing the trade-offs, Continuous Acceleration suits limited animation that leans on a few interpolated keys with little manual polish. For highly polished, high-key-rate animation, the smoothing may not be worth the disruption of wider change propagation.

Active Keyframe — Reference: Panel: Sidebar region ‣ F-Curve ‣ Active Keyframe.
Interpolation — the interpolation between the active keyframe and the next.
  Constant — the curve holds its value until the next keyframe, giving an abrupt stair-step; normally used only during the initial "blocking" stage of pose-to-pose workflows.
  Linear — the curve runs straight from one keyframe to the next, avoiding abrupt value changes (though not speed changes); two keyframes with Linear interpolation and extrapolation make an endless straight line easily.
  Bézier — the default, smooth in both value and speed.
  Note: F-Curves for properties that accept only discrete values always look stair-stepped, whatever you pick.
Easing (by strength) — a set of interpolations that specialize in speeding up or slowing down a value, easing it from rest into motion or the reverse. See also easings.net and Robert Penner's Easing Functions for explanations and live demos.
Dynamic Effects — extra easing types that fake physics-like effects such as bouncing.
  Back — with Ease In the value first pulls away from the target and then darts toward it; with Ease Out it heads for the target, overshoots, and returns. Its Back setting sets the overshoot's size and direction (above/below the curve).
  Bounce — the value bounces a few times with exponential decay, like a tennis ball dropped on the floor.
  Elastic — the value overshoots the target, rebounds and undershoots, overshoots again, and so on with ever-fading intensity until it settles. Amplitude sets how far it first overshoots; Period sets the time between oscillations.
Easing — applies only to the Easing and Dynamic Effects categories above.
  Automatic Easing — auto-picks the most common type: Ease In for the Easing interpolations, Ease Out for the Dynamic Effects.
  Ease In — the value accelerates, slow at the segment's start and faster toward the end.
  Ease Out — the value decelerates, fast at the start and slower toward the end.
  Ease In Out — slow at the start, quick through the middle, slow again toward the end.
Key Frame — the active keyframe's frame.
Value — the active keyframe's value.
Left/Right Handle Type — when the keyframe's interpolation is Bézier, the curve's shape around it depends on its handles, and each handle's type decides whether and how Blender places it automatically, and how freely you can place it by hand. Change handle types several ways: these Sidebar dropdowns, the Key ‣ Handle Type menu, or pressing V and picking from the popup. To move an automatic handle, just drag it — no need to change its type first.
  Automatic — automatic handles that yield smooth curves.
  Auto Clamped — automatic handles clamped to prevent overshoots and direction changes (S-shapes) between keyframes.
  Vector — automatic handles that produce straight segments, like linear interpolation.
  Aligned — manual handles locked together to always point opposite ways, giving a curve that's always smooth at the control point.

Free — manual handles that move independently, so they can produce a sharp change of direction.
Frame, Value — the frame and value of the active keyframe's left/right handle.

[Related references](INDEX.md).
