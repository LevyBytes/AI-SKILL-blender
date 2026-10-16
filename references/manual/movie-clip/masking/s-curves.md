# S-Curves

## S-Curves

### S-Curves

The curve underlying a mask spline looks like a Bézier curve but isn't exactly one.
Feathering is what gives a mask its soft edges.
What was needed was a curve that supported feathering and kept the feather glued to the curve as you edited it,
to make animating it easier. The result is called an S-curve.

On top of the handles, each control point also carries points that lay out the feather between
that point and the next one along the spline.
Every feather point lives in UW space,
where U is the position along the spline segment and W (weight) is the distance separating the main spline from the feather points.

S-Curve explained.

The upshot is that you can deform the main spline almost however you like,
and the feather refreshes on its own to match.

Take pure rotation of the spline, for example:
the feather wouldn't budge. Move one point's feather, and
the rest stretch uniformly along that segment,
keeping the overall shape close to what an artist would expect.

### Primitives

Reference

Mode :

Mask Mode

Tool :

Add

Shortcut :

Shift - A

Two primitives are on offer: a Bézier Circle and a Square with vector handles.

[Related references](INDEX.md).
