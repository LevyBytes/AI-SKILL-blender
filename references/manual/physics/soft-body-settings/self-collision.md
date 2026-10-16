# Self Collision

## Self Collision

### Self Collision 

Reference

Panel :

Physics ‣ Soft Body ‣ Self Collision

Note

Self-Collision functions only when Use Edges is enabled.

When enabled, controls soft-body self-intersection prevention.
Every vertex gains an elastic virtual ball.
Vertices cannot penetrate adjacent balls.
Default options usually succeed; adjustment may occasionally help.

Calculation Type

Manual :

Ball Size sets directly.

Average :

Average edge length attached to the vertex multiplies by Ball Size. Suits evenly distributed vertices.

Minimal/Maximal :

Ball size equals smallest/largest vertex spring length multiplied by Ball Size.

Average Min Max :

Size = ((Min + Max)/2) × Ball Size.

Ball Size
Fraction of attached-edge length.
Edge length depends on the chosen algorithm.
Multiply by this factor to get the radius within which vertices avoid others.
Set to the fractional distance between vertices defining their "personal space".
Higher values include too many vertices, slowing calculation; lower values allow intersection despite insufficient time for avoidance.

Stiffness
How elastic the personal-space ball is.
High stiffness means immediate reaction when a vertex enters the space.

Dampening
Vertex reaction type.
Low values slow approaching vertices. High values repulse them.

Note

Configure other-object collisions in the Collision panel.
Soft-body and collision-object must share a layer to collide.

[Related references](INDEX.md).
