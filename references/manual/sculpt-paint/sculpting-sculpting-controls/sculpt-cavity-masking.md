# Controls: Cavity, Geometry at surface peaks gets skipped.

Cavity
Geometry at surface peaks gets skipped.
While geared toward painting,
it works for standard sculpting too.

Factor
General intensity of cavity protection. Default is 0.5,
but 0.2 with a Custom Curve yields better outcomes.

Blur
Repetitions of cavity mask smoothing. 0 provides raw cavity masking.
Over 6 progressively diminishes visibility and speed.
Capped at 10, though typing raises the limit to 25.

Custom Curve
Refine cavity masking with a custom curve.
Beneficial for small recesses or flat areas alone.
Or modify intensity distribution in particular ranges.

Create Mask
Executes Mask From Cavity with current settings.
Renders the current auto-mask or permits further editing.

Cavity (Inverted)
Matches "Cavity" yet reversed.
Valleys and surface hollows don't activate.
Cannot combine with Cavity; shares its configuration.
Toggle to quickly flip cavity protecting.

View Normal
Only geometry with surface normals facing the viewer is affected.
Matches the "Front Faces Only" setting in the
Brush Setting, narrowing to visible areas.
This version supplies more flexibility and operates on sculpt as a whole.

Occlusion
Update View Normal to only affect geometry not hidden by other faces.
This mode conflicts with other Limit and Falloff controls.
Substantially slower performance results.

Limit
Sets the angular window of affected geometry. 90° covers all visible.

Falloff
Broadens the Limit slider's angular scope with smooth transition.
Extends perceived limits further.

Area Normal
Parallels View Normal yet derives the direction from the surface normal at stroke/tool origin.
Permits any direction for affected geometry.
Employs identical Limit and Falloff as View Normal auto-masking.

[Related references](INDEX.md).
