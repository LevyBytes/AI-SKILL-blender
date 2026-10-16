# Reducing Noise: Path Tracing, The Source of the Noise, Bounces, Caustics and Filter Glossy, Light Falloff, Multiple Importance Sampling, Glass and Transparent Shadows, Light Portals

## Reducing Noise

### Reducing Noise

When rendering a final output, minimizing visual noise is a critical priority. This section explores practical techniques that, while departing from strict physical simulation, prove essential for completing animations within practical timeframes. Examine the examples at full size to appreciate the noise reduction differences.

### Path Tracing

Cycles implements path tracing combined with next event estimation. This approach has limitations for certain phenomena such as caustics, yet provides substantial advantages: it scales efficiently to detailed and large-scale environments since the renderer avoids storing structures like photon maps in memory, and maintains ray coherence for efficient image caching, outperforming strategies such as bidirectional path tracing.

The algorithm inverts the natural light flow: rays originate from the camera, pass through the scene, and terminate at light sources, rather than emanating from lights and reaching the camera. This strategy eliminates wasted rays that miss the camera entirely, but introduces a challenge—it becomes harder to locate certain light paths that contribute significantly to the final image. Light rays distribute either following the surface's BSDF or traveling directly toward known light sources.

See also

For deeper details, consult the Light Paths and Sampling documentation.

### The Source of the Noise

To grasp noise origins, consider this example. When a ray reaches the point marked by the white circle on a red dot, the second image illustrates what the diffuse shader perceives.

Finding the light reflected from this point requires averaging the color across many samples. Observe the glossy reflection on the sphere and the bright light mark on the wall—these high-intensity patches contribute disproportionately to the pixel's lighting.

| Description | Description | Description |
| --- | --- | --- |
| The scene. | Irradiance at the shading point. | The detected highlights. |

The light source location is predetermined, yet the glossy highlights it produces behave differently. Path tracing's strategy distributes rays randomly across the hemisphere, hoping to encounter all significant bright regions. If some pixels miss a bright spot while others find it, this inconsistency manifests as noise. Rendering more samples increases the likelihood of covering all important light contributors.

Certain techniques reduce this noise. By softening bright spots—making them larger yet less intense—they become easier to find and produce less noise. While not identical to the original result, the difference often proves negligible when viewed through diffuse or soft glossy reflections. An example follows using Glossy Filter and Light Falloff.

| Description | Description | Description |
| --- | --- | --- |
| Using Glossy Filter & Light Falloff. | Irradiance at the shading point. | The detected highlights. |

### Bounces

In nature, light bounces countless times due to its speed. In rendering, additional bounces introduce noise, and the Limited Global Illumination preset in the Light Paths section can help by reducing bounces for different material types. Diffuse surfaces typically manage with fewer bounces, while glossy surfaces demand more, and transmission shaders like glass typically need the most.

| Description | Description | Description |
| --- | --- | --- |
| No bounces. | Two bounces at max. | Four bounces at max. |

Equally important is avoiding colors with components at 1.0 or near it; maintain a maximum of 0.8 and increase light brightness instead. In the physical world, surfaces rarely reflect all light, though glass is a notable exception, transmitting most illumination, which is why greater bounce counts apply there. High color values produce noise because light intensity barely diminishes as it reflects between surfaces.

### Caustics and Filter Glossy

Caustics represent a well-known noise challenge, producing Fireflies. These arise when the renderer struggles to detect specular highlights viewed through soft or diffuse reflections. A No Caustics option disables glossy reflections passing through diffuse surfaces entirely. The default behavior in most renderers disables caustics automatically.

| Description | Description | Description |
| --- | --- | --- |
| Default settings. | Caustics disabled. | Filter Glossy greater than zero. |

However, No Caustics sacrifices light contribution and overlooks scenarios where sharp glossy reflections appear through soft glossy reflections. A Filter Glossy option cuts noise in these situations, sacrificing some precision. This technique softens sharp reflections by increasing shader Roughness, allowing easier detection.

The images above display three states: defaults, caustics disabled, and Filter Glossy at 1.0.

### Light Falloff

In a vacuum, light follows a 1/(distance^2) falloff law. Yet as distance approaches zero, this expression tends toward infinity, generating extremely bright spots. For indirect lighting, finding such rare, tiny, and brilliant spots becomes statistically unlikely, forming the classic recipe for Fireflies.

| Description | Description |
| --- | --- |
| Hard Falloff. | Soft Falloff. |

To mitigate this, the Light Falloff node provides a Smooth factor, reducing the maximum intensity light contributes to nearby surfaces. The images above compare default falloff against smooth set to 1.0.

### Multiple Importance Sampling

Materials using emission shaders may leverage Multiple Importance Sampling (Material Settings). Under this approach, rays are directed explicitly toward these materials rather than reaching them through random bouncing. For intense mesh lights, this substantially cuts noise. Conversely, when emission proves dim, this option diverts samples from genuinely bright sources that require directed sampling, lowering efficiency.

Optimal configuration requires experimentation; weak glowing objects may contribute only locally and benefit from disabling Multiple Importance, while mesh lights used as primary light sources usually need it active. Included is an example: emissive spheres contribute minimally, and the render achieves slightly lower noise with Multiple Importance disabled.

| Description | Description |
| --- | --- |
| Multiple Importance off. | Multiple Importance on. |

The world background holds its own Multiple Importance option (Settings). This proves most valuable for environment maps containing scattered bright points rather than uniform gradients. The renderer preprocesses to pinpoint these bright areas and sends rays directly toward them. Again, enabling this may redirect samples away from more critical light sources if unwarranted.

### Glass and Transparent Shadows

With caustics suppressed, glass shadows may appear too dim, and with filter glossy, caustics risk becoming overly soft. Construct a glass shader using Glass BSDF for direct rays and Transparent BSDF for indirect rays. Transparent BSDF suits transparent shadows, locating light straight through surfaces and delivering correctly-tinted shadows without caustic artifacts. The Light Path node determines which shader applies.

Optimized glass shader.

Left: render with dark shadows from missing caustics. Right: render using the glass shader optimization.

| Description | Description |
| --- | --- |
| Default Glass BSDF. | Optimized Glass Shader. |

### Light Portals

When rendering indoor daylight scenes where light enters mainly through windows or doors, the integrator struggles to locate these openings. Light Portals address this. Scale them to match the opening you wish to illuminate.

[Related references](INDEX.md).
