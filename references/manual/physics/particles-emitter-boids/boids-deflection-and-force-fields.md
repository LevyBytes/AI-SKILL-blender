# Boids: Deflection, Force Fields, Boid Brain, Goal Rule, Avoid Rule

### Deflection 

Boids navigate around deflector geometries via Collision rule weighting. This works optimally with convex profiles (concave surface support requires further refinement).

### Force Fields 

Like other physics classifications, Boids responds to external force field influence.

Moreover, specialized Boid force fields pair with Boid physics. These effectors function as predators (positive Strength) that boids attempt to evade or objectives (negative Strength) that boids attempt to locate, based on the Boid Brain Avoid and Goal protocols respectively.

### Boid Brain 

Reference

Panel :

Particle System ‣ Physics ‣ Boid Brain

The Boid Brain panel configures how boid particles interact. Behavioral direction comes from a rule sequence. Memory constraints limit information processing. Remaining rules become disregarded once capacity gets exceeded.

Top-to-bottom rule parsing defines hierarchy (earliest rules take precedence). Arrow buttons on the right permit sequence reordering.

Rule Evaluation

Three evaluation paradigms govern rule processing:

Average

All rules receive equal weighting.

Random

Each boid selects a random rule.

Fuzzy

Implements fuzzy decision logic. Top-to-bottom traversal continues until a rule exceeds the Rule Fuzziness activation point. The metric represents rule compliance commitment (1 means strict adherence, 0 means no adherence). Multiple concurrent contradictory rules trigger simultaneous compliance per individual weight.

Note

Boids attempt rule adherence with maximum effort, though some may dominate others contextually. As example: evasion of a predator might overshadow Collision, Separate, and Flock adherence, permitting wall/object penetration despite contrary instructions—essentially a "panic override."

In Air

This rule applies during airborne states.

On Land

This rule applies during non-airborne states.

### Goal Rule 

Navigate toward objective.

Object

Designates the goal target. Absent assignment defaults to negatively-charged Boid force fields as goal markers.

Predict

Anticipates goal displacement.

### Avoid Rule 

Elude "predators".

Object

Designates the avoidance target. Absent assignment defaults to positively-charged Boid force fields as threat identifiers.

Predict

Anticipates threat displacement.

Fear Factor

Escape occurs if danger surpasses this threshold.

[Related references](INDEX.md).
