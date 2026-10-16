# Retime Node

## Retime Node

The Retime node adjusts the timing of input sequences, animations, or time-based effects by offsetting, skipping, or repeating frames — for slow motion, fast-forward, looping, or rhythmic stutter within compositing. Inputs: Offset (add or subtract a constant frame offset — positive delays, negative advances); Step (skip frames by this size — 2 plays every other frame, doubling speed); Speed (scale time globally — 1.0 normal, 0.5 half, 2.0 double); Cyclic (loop the input continuously when the retimed output exceeds the original range); and Cycle Length (the frames per loop cycle when Cyclic is on). Output: Frame (the remapped frame, connectable to frame-based inputs to drive animated or sequential effects).

[Related references](INDEX.md).
