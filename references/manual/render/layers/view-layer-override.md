# View Layer Override

## View Layer Override

### View Layer Override

Reference

Panel :

Properties ‣ View Layer ‣ Override

View Layer overrides enable conditional replacement of select scene-wide configuration for one particular view layer.
This method helps create alternate renderings of identical layouts, for instance with varied surface properties, illumination,
or quality parameters, while preserving initial scene information unchanged.

Overrides take effect exclusively during layer rendering and don't apply globally.

Material Override
Replaces materials throughout the layer with a universal material option.
Typical uses include monochrome renderings or illumination tests where texture and shader detail obstructs the analysis.

Tip

Choose a simple diffuse surface for studying light distribution or geometry without texture or shader distraction.

World Override
Substitutes the scene's world parameters (such as background tone or HDRI environment) for the chosen layer.

This option facilitates testing varied
environmental illumination configurations
or positioning objects against neutral backgrounds for later composition.

Samples
Permits the layer to employ divergent sampling count compared to overall scene configuration.
The Layer Samples parameter
governs this behavior in the Cycles rendering engine. The Samples override activates at all times in EEVEE.

Using fewer samples for utility or background passes cuts time,
while prioritizing higher samples for hero visual passes.

[Related references](INDEX.md).
