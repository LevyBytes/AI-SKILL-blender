# Ocean Modifier: Waves, Foam, Spray

### Waves

Scale
An overall handle on the amplitude of the waves.
It roughly stands in for how far the waves rise above or drop below zero.
Rather than merely scaling the ocean object in Z, it scales every facet of the simulation,
displacement in X and Y, plus the matching foam and normals.

Smallest Wave
A floor on how small generated waves may get.
It works rather like a low-pass filter, stripping out higher frequency wave detail.

Choppiness
How choppy the wave peaks come out.
At a choppiness of 0, the ocean surface only rises and falls along Z,
but raise it and the waves also shift sideways in X and Y, sharpening the peaks.

Wind Velocity
Wind speed in meters/second. Keep it low and the waves stay confined to smaller surface ripples.

Alignment
How strongly the wave shapes line up under the wind.
At 0, wind and waves point every which way, evenly and at random.
Push Alignment up and the wind blows more steadily in one direction,
leaving the waves looking more compressed and lined up along a single heading.

Direction
While Alignment is in use, the heading in degrees the waves line up to (measured against the local X axis).

Damping
While Alignment is in use, this sets how far inter-reflected waves are damped out.
The effect is to make the wave motion more directional, not just the wave shape.

At a Damping of 0.0, waves bounce off one another every which way; at a Damping of 1.0,
those inter-reflected waves are killed off, so only waves running with the wind remain.

### Foam

Works up extra foam data.

The Ocean texture can pull this back for use in texturing (as a mask, perhaps),
and it lets you generate foam map image sequences during baking.

Data Layer
An optional name for the vertex data layer
the Ocean Modifier uses to hold foam maps as a Color Attribute.
You need this to reach the foam data in the renderer.

Coverage
Dials how much foam blankets the waves: negative values thin it out
(leaving just the topmost peaks), positive values pile more on. Usually ranges from (-1.0 to 1.0).

Using foam Color Attributes with a named data layer.

#### Spray

Works up a map of spray direction as a Color Attribute.
That map can serve to set the velocities for spray particles.

Spray Map
The name of the Color Attribute holding the spray direction map.

Invert
Flips the spray direction map.

[Related references](INDEX.md).
