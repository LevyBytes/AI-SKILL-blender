# bpy.types.SceneEEVEE: ray_tracing_method, ray_tracing_options

ray_tracing_method

Pick how scene-ray intersections are found (default 'SCREEN' )

- PROBE
Light Probe – Use light probes to locate the scene intersection.

- SCREEN
Screen-Trace – Trace rays against the depth buffer, falling back to light probes for invalid rays..

Type :

Literal[‘PROBE’, ‘SCREEN’]
ray_tracing_options

EEVEE settings for tracing reflections (readonly)

Type :

RaytraceEEVEE

[Related references](INDEX.md).
