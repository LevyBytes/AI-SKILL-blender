# Viewport Display

### Viewport Display 

Reference

Panel :

Particle System ‣ Display

Rendered

Presents hair as curves.

Path

Presents the hair terminal points alone.

Steps

Tallies the segments (control point count less one) composing a hair segment. Segment interpolation bridges control points. Control point quantity matters:

- For soft body animation, control points simulate like mesh nodes, so elevated counts increase computation duration.

- For interactive editing, only control points move (though Particle Edit Mode permits control point count adjustment).

Hint

Segments

Ten Segments adequately covers extended hair. Five Segments suit shorter lengths. Two or three Segments suffice for fur.

[Related references](INDEX.md).
