# Introduction

### Introduction 

Hair-type particle systems model strand-like structures: hair, fur, grass, quills, and similar forms.

Particle hair systems example. Used for the grass and fur. 

### Growing 

Hair creation starts with specifying strand count and initial length.

Particle paths are pre-calculated in advance. Hair capabilities match particle capabilities: a hair's length corresponds to a particle's 100-frame lifetime path.
Rather than rendering each animation frame separately, control points with interpolated segments represent the path.

### Styling 

Hair appearance changes through styling adjustments. Base hair alterations use Physics Settings.

Advanced styling employs Children, adding supplementary strands with distinct shape properties.

Interactive hair sculpting occurs in Particle Edit Mode, where particle settings suspend and brushes enable combing, trimming, lengthening operations.

### Animating 

Hair becomes dynamic through the cloth solver, documented in the Hair Dynamics page.

### Rendering 

Cycles provides specialized hair BSDFs for rendering: Hair BSDF and Principled Hair BSDF.

Hair also serves as input for the Particle Instance Modifier, enabling mesh deformation along curves—useful for thick strands, grass, feathers, and similar structures requiring specialized appearance.

[Related references](INDEX.md).
