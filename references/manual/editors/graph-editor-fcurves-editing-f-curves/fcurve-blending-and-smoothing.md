# Fcurve blending and smoothing

Blend — Reference: Menu: Key ‣ Blend; Shortcut: Alt-D. Nudges the selected keyframes' values by a percentage: pick a blending operator, move the mouse left or right to set the factor, and confirm with LMB (or cancel with RMB). Several blending operators work off "neighboring keyframes," meaning they split the selection into contiguous groups and reference the unselected keys just before and after each group.
Breakdown — Reference: Menu: Key ‣ Blend ‣ Breakdown. Sets the selected keyframes to an interpolation of their neighbors.
  Factor — at -1 the keys take the left neighbor's value; at 1 the right neighbor's; in between they interpolate, 0 sitting dead center.
Blend to Neighbor — Reference: Menu: Key ‣ Blend ‣ Blend to Neighbor. Moves each selected keyframe a percentage of the way toward its left or right neighbor's value.
  Blend — negative moves each key Blend percent toward the left neighbor; positive toward the right; zero keeps the originals.
Blend to Default Value — Reference: Menu: Key ‣ Blend ‣ Blend to Default Value. Moves the selected keyframes a percentage toward the property's default value.
  Factor — how far to shift, from 0 (no change) to 1 (full reset to default).
  See also the Reset to Default operator, which resets any property to its default without keyframing.
Ease — Reference: Menu: Key ‣ Blend ‣ Ease. Bends the selected keyframes onto an S-curve. While the slider shows (after activating but before confirming with LMB), press Tab to switch which setting you're editing:
  Curve Bend — negative weights the left side, positive the right, 0 gives a balanced curve.
  Sharpness — low gives a near-straight diagonal, high gives a steep rise/drop.
Blend Offset — Reference: Menu: Key ‣ Blend ‣ Blend Offset. Shifts the selected keyframes up or down by one shared amount until the first/last one meets the left/right neighbor.
  Offset Factor — at -1 the first selected key aligns to its left neighbor; at 1 the last aligns to its right neighbor; at 0 nothing moves.
Blend to Ease — Reference: Menu: Key ‣ Blend ‣ Blend to Ease. Blends the selected keys toward an "ease in" or "ease out" curve.
  Blend — at -1 the keys follow an "ease in" curve (small changes early, large changes late); at 1 an "ease out" curve (large early, small late); at 0 nothing moves.
Match Slope — Reference: Menu: Key ‣ Blend ‣ Match Slope. Blends the selected keys toward a straight line drawn through two keys just outside the selection.
  Factor — negative uses the two keys left of the selection, positive the keys to the right, zero changes nothing.
Push Pull — Reference: Menu: Key ‣ Blend ‣ Push Pull. Moves the selected keys toward or away from the straight line through the first and last selected key.
  Factor — at 0 the keys land on the straight line.

At 1 they stay where they are; at 2 each key ends up twice the distance from that line it had before.

Shear Keys — Reference: Menu: Key ‣ Blend ‣ Shear Keys. Shears the selected keyframes — changing each value by an amount that grows the further it lies in time from a reference keyframe. The reference defaults to the leftmost selected key, but pressing D switches to the rightmost.
  Shear Factor — how much to shear; negatives push keyframes down, positives push them up.
  Direction — whether the leftmost or rightmost selected keyframe is the reference.

Scale Average — Reference: Menu: Key ‣ Blend ‣ Scale Average. Scales the selected keyframes vertically about their average value.
  Factor — at 0 the keyframes all collapse to the average value; at 1 they stay put; at 2 each ends up twice the distance from the average it had before.

Scale from Neighbor — Reference: Menu: Key ‣ Blend ‣ Scale from Neighbor. Scales the selected keyframes vertically about a keyframe just outside the selection; that pivot defaults to the left neighbor, but pressing D uses the right one.
  Factor — the scale factor.
  Reference Key — whether the left or right neighbor is the pivot.

Time Offset — Reference: Menu: Key ‣ Blend ‣ Time Offset. Shifts the selected keyframes' values so the resulting F-Curve looks like it's traveling through time; works best with dense keyframes. As the curve runs off one end of the selected time range, it wraps in at the other, offset vertically so the ends meet without a jump.
  Frame Offset — by how many frames to slide the F-Curve; the slider caps at -10 … 10, but you can type larger numbers.

Smooth — Reference: Menu: Key ‣ Smooth; Shortcut: Alt-S.
Smooth (Gaussian) — Reference: Menu: Key ‣ Smooth ‣ Smooth (Gaussian). Smooths the selected keyframes with a Gaussian kernel: click the item, move the mouse left or right to set strength, and confirm with LMB (or cancel with RMB).
  Factor — how strongly to smooth.
  Sigma — the Gaussian distribution's shape; lower values sharpen it, weighting nearby keys more, while a high value acts like a plain average filter.
  Filter Width — a wider filter takes in more keyframes for a smoother result; at width 1 it only weighs the immediate left and right neighbors.
Smooth (Legacy) — Reference: Menu: Key ‣ Smooth ‣ Smooth (Legacy); Shortcut: Alt-O. Another way to smooth the selected curves, but beware: its algorithm appears to halve the gap between each keyframe and the curve's average linear value, which smooths quite hard. The first and last keys seem never to be touched.
Butterworth Smooth — Reference: Menu: Key ‣ Smooth ‣ Butterworth Smooth. Smooths the selected keyframes with a Butterworth filter: click the item, move the mouse left or right to set the frequency, and confirm with LMB (or cancel with RMB). It's great for smoothing large amounts of data because it keeps the animation's peaks, though it can add a ripple where key values change fast.
  Frequency Cutoff — lower means smoother; there's an implicit ceiling, at half the sample rate, beyond which it no longer changes the curve, the sample rate being the scene frame rate times this operator's Samples per Frame.
  Filter order — higher makes the frequency cutoff steeper.
  Samples per Frame — before filtering, the curve is resampled at this interval to avoid errors from uneven frame spacing; if keys land on subframes (a 60fps file in a 30fps scene, say), raise this to 2.
  Blend — a 0-to-1 value blending the original curve with the smoothed one.
  Blend In/Out — how many frames at the start and end to blend between original and smoothed, which can soften jumps at the selection's edge; at value 1 it locks just the first and last frames of the selection to their originals.

[Related references](INDEX.md).
