# Light Paths

### Surface

Direct Light
Limits maximum light intensity a surface can reflect. Reduces aliasing and fireflies at accuracy cost. Zero disables clamping. Lower values produce stronger effects.

Indirect Light
Similar to Direct Light but limits ray-traced and light-probe reflected intensity. Also restricts world lighting intensity since it counts as indirect.

Note
These options suppress fireflies and aliasing on reflective surfaces and dense volumes. However, intentionally bright highlights may also reduce. Balance firefly reduction against desired brightness retention.

### Volume

Direct Light
Same as Surface Direct Light applied to volume direct illumination.

Indirect Light
Same as Surface Indirect Light applied to volume indirect illumination.

### Intensity

Reference
Panel: Render ‣ Light Paths ‣ Intensity

Intensity multipliers scale lighting contribution in EEVEE. They do not alter ray depth, sampling, accumulation, or performance traits.

Direct Light
Scale direct lighting contribution, including light sources directly illuminating surfaces and volumes.

Higher values amplify highlights and direct illumination. Lower values weaken apparent light source strength without modifying their energy settings.

Indirect Light
Scale indirect lighting contribution, including bounced light from ray tracing and light probes.

Affects global illumination and world lighting. Strengthen or weaken perceived bounce light in a scene. Scaling occurs post-clamping, maintaining firefly suppression. Behavior resembles post-lighting compositing adjustment while remaining uniform across dithered and blended materials.

These controls adjust lighting balance in expansive environments, fine-tune indirect illumination, and balance direct versus indirect contribution without altering individual light settings.

[Related references](INDEX.md).
