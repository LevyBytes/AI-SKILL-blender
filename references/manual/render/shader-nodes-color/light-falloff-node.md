# Light Falloff Node

## Light Falloff Node

### Light Falloff Node 

Cycles Only

The Light Falloff node offers control over intensity attenuation with distance. Physically accurate light exhibits quadratic falloff; applying alternative falloff curves enables non-realistic lighting adjustments. Be cautious: Linear or Constant falloff can amplify light with each global illumination pass, potentially causing severe overexposure with multiple bounces.

### Inputs 

Strength
Light magnitude before falloff transformation.

Smooth
Light intensity softening near sources. Values smooth out harsh highlights and reduce GI noise. Zero means no smoothing; larger values increase it. Maximum intensity equals strength divided by smooth.

### Properties 

This node has no properties.

### Outputs 

Quadratic
Quadratic light attenuation; matches physical reality when smooth is 0.0.

Linear
Linear intensity reduction creating slower decay across distance.

Constant
Constant output where distance has no effect.

### Examples 

Todo <2.8 add.

[Related references](INDEX.md).
