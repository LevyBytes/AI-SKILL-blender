# Canvas: Paint, Displace, Waves, Weight, Common Options

#### Paint

Paint Surface. 

Paint is the core surface outputting color and wetness. Vertex surface results show as Color Attributes.

Wetmap is grayscale: white = max wetness, black = fully dry. Typically masks rendering. "Paint effects" target wet paint only.

Dry
Disabling drying spreads paint indefinitely.

Color Dry
Defines wetness where paint colors shift toward surface "background". Lower = prevent transparent spreading; higher = better general results.

#### Displace

Displace Surface. 

This outputs intersection depth from brush objects.

Incremental
Adds new displace cumulatively on existing displace.

Max Displace
Intersection depth ceiling; excess clamps.

Displace Factor
Intersection depth multiplier. Adjust strength or use negative for bump painting.

Tip

Rough displace output? Add Smooth Modifier after Dynamic Paint.

#### Waves

Waves Surface. 

This simulates wave motion from brush intersection depth.

Open Borders
Waves cross mesh "edges" instead of reflecting.

Timescale
Adjusts sim speed without outcome shift. Lower = slower; higher = faster.

Speed
Wave travel pace on surface, also corresponding to simulation size. Half speed = surface doubles.

Damping
Wave-strength reduction. Higher = faster disappearance.

Spring
Force pulling water to "zero level".

Smoothness
Max wave-slope steepness between sim points. Eliminates "noise" from sharp-edged objects (cubes). Default catches sharpest spikes; higher values smooth further at detail cost.

Tip

Unstable wave motion near brushes? Lower wave speed, brush "wave factor", or mesh/surface resolution.

#### Weight

Weight Surface. 

Vertex-format-only surface outputting vertex weight groups for other Blender modifiers/tools.

Tip

Prefer "proximity" brushes for weight surfaces for smooth falloff.

### Common Options

Special settings exist per type. Most have Dissolve and Brush:

Dissolve
Smoothly returns the surface to original state over a Time period.

Brush Collection
Defines a specific collection for brush sources.

Influence Scale, Radius Scale
Tweaks brush parameters per surface.

[Related references](INDEX.md).
