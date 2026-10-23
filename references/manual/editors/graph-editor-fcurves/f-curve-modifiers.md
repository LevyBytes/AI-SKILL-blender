# F-Curve Modifiers

## F-Curve Modifiers

Reference - Panel: Sidebar region ‣ Modifiers.

F-Curve modifiers work like object modifiers: they add non-destructive effects you can tweak anytime and stack to build more elaborate results. They evaluate top to bottom, and you reorder them by dragging the dots at a modifier's top-right corner. A few must come first and can't be combined — currently the Cycles and Smooth (Gaussian) modifiers.

Interface:
Name: modifiers are named for their function by default, but you can rename them.
Mute: the checkbox in a modifier's header disables it.
Delete: the cross in a modifier's header removes it.
Influence: mixes the original curve with the modified one.
Restrict Frame Range:
  Start/End: the frame on which the modifier's effect begins/ends.
  Blend In/Out: how many frames, measured from the Start/End above, the modifier takes to fade in/out.

Adding a Modifier — manage modifiers on the Sidebar's Modifiers tab: choose an F-Curve — either in the channel region or by clicking one of its keyframes — then open the Add Modifier dropdown and pick one.

Types of Modifiers:
Generator Modifier - creates a polynomial function: basic formulas that draw lines, parabolas, and more elaborate curves depending on the values used. See also the Wikipedia Page for more on polynomials.
  Mode: how the equation is expressed. Expanded Polynomial uses the form \(y = A + Bx^1 + Cx^2 + ... + Dx^n\); Factorized Polynomial uses \(y = (Ax + B)(Cx + D)\).
  Additive: adds the polynomial onto the curve instead of replacing it.
  Order: the highest power of x in the polynomial.
  Constant: the constants A, B, C… in the equation.
Built-in Function Modifier: extra formulas, each with the same shape controls. Consult a mathematics reference for detail on each.
  Type - the built-in function: Sine, Cosine, Tangent, Square Root, Natural Logarithm, or Normalized Sine: \(sin(x)/x\).
  Additive: adds the function onto the curve instead of replacing it.
  Amplitude: adjusts the Y scaling.
  Phase Multiplier: adjusts the X scaling.
  Phase Offset: adjusts the X offset.
  Value Offset: adjusts the Y offset.
Envelope Modifier — lets you reshape the curve: first define an envelope (two horizontal lines roughly matching the curve's lower and upper bounds), then add control points, each of which can push, squeeze, and stretch the envelope — and the curve with it — at a given frame.
  Reference: the value the envelope centers on.
  Min/Max: how far the envelope's starting lower/upper bound sits from the reference value.
  Add Control Point: adds a control point at the current frame.
  Point: Frame (the control point's frame) and Min/Max (how far the envelope's adjusted lower/upper bound at this frame sits from the reference value).
Cycles Modifier — makes the curve repeat. Note: it has to be the first modifier in the list, because it needs to know exactly where the keyframes sit — impossible if other modifiers run first — which is why it's incompatible with the Smooth (Gaussian) Modifier.
  Before/After Mode: No Cycles (don't repeat before/after the original), Repeat Motion (repeats with each copy's values unchanged), Repeat with Offset (repeats, shifting each copy vertically so its first keyframe meets the previous last one), Repeat Mirrored (repeats, flipping every other copy horizontally).
  Count: how many copies to make; 0 means infinite.
  Trivially Cyclic Curves: when the Cycle Mode at both ends is Repeat Motion or Repeat with Offset and no other modifier options are changed from default, the result is a simple infinite cycle. This special case gets extra support elsewhere in Blender: automatic Bézier handle placement accounts for the cycle and adjusts for a smooth transition, and the Cycle-Aware Keying option can be turned on so new keyframes respect the cycle.
Noise Modifier: perturbs the curve with a noise formula, useful for adding subtle or wild randomness to motion, like camera shake.
  Blend Type: Replace (adds noise in [-0.5, 0.5]), Add (adds noise in [0, 1]), Subtract (subtracts noise in [0, 1]), Multiply (multiplies by noise in [0, 1]).
  Scale: the noise's horizontal scale; higher values give less dense oscillation.
  Strength: the noise's vertical scale.
  Offset: offsets the noise in time.
  Phase: adjusts the noise's random seed.
  Depth: adjusts how detailed the noise is.
  Lacunarity: the gap between successive frequencies; Depth must exceed 0 for it to matter.
  Roughness: the amount of high-frequency detail; Depth must exceed 0 for it to matter.
Limits Modifier: confines the curve to set time and value ranges.
  Minimum, Maximum X: drops the original curve data left of the minimum frame and right of the maximum, replacing it with Constant extrapolation.
  Minimum, Maximum Y: clamps the curve's values, never letting them dip below the minimum or rise above the maximum.
Stepped Interpolation Modifier: gives the curve a stair-step look by sampling it every N frames and holding each sampled value, effectively lowering its frame rate so it changes less often and moves choppily.
  Step Size: how many frames to hold each step.
  Offset: how many frames to offset the sample points.

Start Frame: the frame where the effect begins.
End Frame: the frame where the effect stops.

Smooth (Gaussian) Modifier — uses Gaussian smoothing to strip detail and noise from the curve, performing the same smoothing as the Smoothing Operator. It uses linear interpolation for subframes, which can cause motion-blur-related issues. It can also be resource-heavy, with a noticeable performance hit across many F-Curves. Note: it has to be the first modifier in the list, because it needs to know exactly where the keyframes sit — impossible if other modifiers run first — so it's incompatible with the Cycles Modifier.
  Sigma: the Gaussian distribution's shape in frames; lower values sharpen the curve and reduce smoothing, larger values smooth more but are bounded by Filter Width.
  Filter Width: how many frames the filter "sees" around each keyframe; higher values allow more smoothing (a larger Sigma can then reach across more frames) but cost performance.

[Related references](INDEX.md).
