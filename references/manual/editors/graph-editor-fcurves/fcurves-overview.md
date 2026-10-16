# Introduction

Blender lets you animate almost any property, from an object's X coordinate to a material's transparency. How a property's value evolves over time is described by a function curve, or F-Curve.

A crucial trait of F-Curves is interpolation, which spares you from setting a value on every single frame — wildly impractical. Instead you place a few values on key frames and let the curve work out the rest.

In the example curve, two keyframes (the black dots) sit at frame 0 with value 0 and frame 25 with value 10; the curve fills in the other frames automatically, giving value 2 at frame 5, for instance.

Direction of Time — F-Curves resemble Curve objects in that they interpolate among user-placed control points. But since their job is to yield one value per frame, there's a key catch: they can't be closed or doubled back on themselves — they always press onward to the right. Try to drag one control point past another to make the curve go left, and it simply swaps the points' order to stop you.

[Related references](INDEX.md).
