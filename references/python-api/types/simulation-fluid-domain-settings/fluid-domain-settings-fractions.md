# bpy.types.FluidDomainSettings: fractions_distance, fractions_threshold

fractions_distance

Sets the spacing kept between fluid and obstacle; larger values push fluid further from obstacles while smaller ones let it creep inside them (in [-5, 5], default 0.5)

Type :

float
fractions_threshold

Sets how much fluid an obstacle cell may hold; larger values flag a boundary cell as obstacle more readily and lessen the boundary smoothing (in [0.001, 1], default 0.05)

Type :

float

[Related references](INDEX.md).
