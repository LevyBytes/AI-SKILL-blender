# Limit Distance Constraint

## Limit Distance Constraint

The Limit Distance constraint keeps an object or bone beyond, within, or exactly at a set distance from a target — that is, its location is held outside, inside, or on a sphere centered on the target. Note it has no effect on connected bones, whose position is set by their parent. Options: Target (the object or bone to stay near or away from); Distance (the limit distance, i.e. the sphere's radius, computed automatically when the first target is selected); a Reset Distance button (set it to the current owner-target distance); Clamp Region, how to constrain relative to the sphere — Inside (keep the owner within it), Outside (keep the owner out of it), or On Surface (keep the owner on it); Affect Transform (when the owner is moved by hand, restrict its Location in the Transform panel too, not only its visual position); Target/Owner (the spaces for reading the target position and applying the result); and Influence. Tip: evaluating both owner and target in a Custom Space automatically scales Distance by the space object's/bone's scale.

[Related references](INDEX.md).
