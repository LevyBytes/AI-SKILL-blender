# Children: Common Options, Clumping, Clump Noise

## Children

### Children 

Reference

Panel :

Particle System ‣ Children

Child particles branch from individual parent particles. Establishing a relatively modest parent particle count allows physics computation on parents alone; children then mirror their progenitors. Parent rendering, child visualization, and volume adjustments all bypass physics recalculation.

When children activate, parent particles disappear from render view. Enabling parent rendering in the Render panel toggles Parent Particles display. Parents stay hidden by default because child geometry frequently diverges from parent form.

### Common Options 

Child Type

None
Children do not generate.

Simple
Children originate from parent locations.

Interpolated
Children emerge between Parent particles on mesh faces. They interpolate adjacent parental behavior. Particularly valuable for fur—even distribution becomes achievable. Select children can acquire virtual parent status, affecting neighboring particle behavior.

Display Amount

Particle count visible in the 3D Viewport.

Render Amount

Particle count for rendering output.

Length

Child path extension.

Threshold

The percentage of particles remaining unaffected by child path length adjustments.

Seed

Random number table offset for child particles, enabling variation in randomization outcomes.

### Clumping 

Reference

Panel :

Particle System ‣ Children ‣ Clumping

Use Clump Curve

Substitutes the Curve Widget for numerical parameters.

Clump

Clumping degree along child strand paths. Children may cluster at their endpoint (1.0) or originate unified at their base (-1.0).

Shape

Clump profile: inverse parabolic (0.99) or exponential (-0.99).

Twist

Use Twist Curve

#### Clump Noise 

Generates random clustering along the parental hair.

Clump Noise Size

Specifies the clustering magnitude.

[Related references](INDEX.md).
