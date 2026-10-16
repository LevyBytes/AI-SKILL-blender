# Brushes

## Brushes

### Brushes

### Brush Types

Refer to Brush Type reference.

Below is a listing of accessible brush types paired with Essentials asset library brushes using those types.

Draw
Brushes: Paint

Deposits assigned weight values onto the mesh.

Blend
The brush Blend Modes establishes how the weight applies to the vertex group while painting.

Mix
Here the Weight establishes the target weight ultimately reached with continuous application at the same location. Brush strength indicates stroke count to hit the target. Note: strength = 1.0 applies target immediately; Weight = 0.0 has no effect.

Add
Adds the specified weight to vertex weighting. Brush strength determines the fraction added per stroke. Weights stay below 1.0.

Subtract
Removes the specified weight from vertex weighting. Brush strength determines the fraction removed per stroke. Weights stay above 0.0.

Lighten
Uses the specified weight as the target. Similar to Mix mode, but only affects weights beneath the target. Weights above the target stay unchanged.

Darken
Comparable to Lighten mode. Alters only weights above the target. Weights below the target stay unchanged.

Multiply
Scales vertex weighting by the specified weight. Similar to subtraction, but the removed amount relies on the Weight value itself.

Blur
Smooths vertex weighting across adjacent vertices. The Weight Value parameter is ignored here. Brush strength governs the smoothing amount.

Blur
Brushes: Blur

Smooths vertex weighting across adjacent vertices. The Weight Value parameter is ignored here. Brush strength governs the smoothing amount.

Average
Brushes: Average

Balances weights by applying the averaged result across all weights in the brush zone.

Smear
Brushes: Smear

Transfers weights by gathering them from the brush zone and "dragging" them. Comparable to finger painting.

[Related references](INDEX.md).
